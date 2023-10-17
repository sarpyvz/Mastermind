import random


class Candidate:
    def __init__(self,val,pscore,nscore):
        self.v = val
        self.p = pscore
        self.n = nscore

    def __str__(self):
        return f"{self.v} ({self.p},{self.n})"

    def check_plus_pos(self, guessval):
        count = 0
        cv = str(self.v)
        guessval = str(guessval)
        for i in range(0,len(cv)):
            if cv[i] == guessval[i]:
                count += 1
        return count

    def check_neg_pos(self, guessval):
        count = 0
        cv = str(self.v)
        guessval = str(guessval)
        for i in range(0,len(cv)):
            for j in range(0,len(guessval)):
                if cv[i] == guessval[j] and cv[i] != guessval[i]:
                    count += 1
        return count

    def consistent(self, guess):
        if self.check_plus_pos(guess.v) == guess.p and self.check_neg_pos(guess.v) == guess.n:
            return True
        else:
            return False

    # def is_consistent(self, guess) -> bool:
    #     return bool(self.check_plus_pos(guess.v) == guess.p and self.check_neg_pos(guess.v) == guess.n)


class CodeMaker:
    def __init__(self,n):
        self.n = n
        self.guess_list = []
        self.start = 10**(n-1)

    def __str__(self):
        a = 0
        s = ""
        for i in range(len(self.guess_list)):
            a +=1
            s += f"Guess#{i+1}:{self.guess_list[i]} "
        return s

    def add_guess(self,guess):
        self.guess_list.append(guess)

    def consistent(self,candidate):
        a = 0
        for guess in self.guess_list:
            if Candidate.check_plus_pos(candidate,guess) == candidate.p and Candidate.check_neg_pos(candidate,guess) == candidate.n:
                a += 1
                if a == len(self.guess_list):
                    #self.start = candidate + 1
                    return True
            else:
                return False

    def propose_guess(self):
        for val in range(self.start,10**self.n):
            count = 0

            for guess in self.guess_list:
                #guess_ = Candidate(guess,guess.p,guess.n)
                #value = Candidate(val,Candidate.check_plus_pos(val, val),Candidate.check_neg_pos(guess,val))
                #value =
                value = Candidate(val,self.check_plus_pos(guess,val),self.check_neg_pos(guess,val))
                if value.consistent(guess):
                    count += 1
                    if count == len(self.guess_list):
                        self.start = value.v + 1
                        return Candidate(val,value.p,value.n)
            if len(self.guess_list) == 0:
                self.start += 1
                return Candidate(val,0,0)

    def check_plus_pos(self, guessval, val):
        count = 0
        cv = str(val)
        guessval = str(guessval)
        for i in range(0,len(cv)):
            if cv[i] == guessval[i]:
                count += 1
        return count

    def check_neg_pos(self, guessval, val):
        count = 0
        cv = str(val)
        guessval = str(guessval)
        for i in range(0,len(cv)):
            for j in range(0,len(guessval)):
                if cv[i] == guessval[j] and cv[i] != guessval[i]:
                    count += 1
        return count


class CodeBreaker:
    def __init__(self,n):
        self.n = n
        self.secret_code = None

    def generate(self,n):
        self.secret_code = random.randint(10**(n-1),10**n-1)
        return self.secret_code

    def setscore(self,guess):
        guess.p = Candidate.check_plus_pos(guess,self.secret_code)
        guess.n = Candidate.check_neg_pos(guess,self.secret_code)


class MasterMind:
    def __init__(self):
        self.n = int(input())
        self.CMkr = CodeMaker(self.n)
        self.CBrk = CodeBreaker(self.n)
        self.secret_code = self.CBrk.generate(self.n)

    def playGame(self):
        while True:
            guess = self.CMkr.propose_guess()
            print(self.CMkr)
            if CodeMaker.consistent(self.CMkr,guess):
                self.CMkr.add_guess(guess)
            elif guess == self.secret_code:
                print(f"Found secret_code {guess}")
                break



random.seed (20)
def main():
    my_game = MasterMind()
    my_game.playGame()
main()
