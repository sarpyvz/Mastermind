import random

n = int(input())
secret_code = random.randint(10**(n-1), 10**n-1)

pos_list=[]
neg_list = []
guess_list = []


def calculate_posscore(candidate, guess):
    s = 0
    candidate = str(candidate)
    guess = str(guess)
    for i in range(0, len(guess)):
        if candidate[i] == guess[i]:
            s += 1
    return s


def calculate_negscore(candidate, guess):
    y = 0
    candidate = str(candidate)
    guess = str(guess)
    for i in range(0, len(guess)):
        for x in range(0, len(guess)):
            if candidate[i] == guess[x]:
                y -= 1
    return y


def consistent(aga, guesdekiler):
    if calculate_posscore(aga, secret_code) >= calculate_posscore(guesdekiler,secret_code) and calculate_negscore(aga,secret_code) == calculate_negscore(guesdekiler, secret_code):
        return True


for aga in range(1000, 10000):
    for x in guess_list:
        if aga == 1000:
            guess_list.append(aga)
            pos_list.append(calculate_posscore(aga, secret_code))
            neg_list.append(calculate_negscore(aga, secret_code))

        if consistent(aga, x):
            guess_list.append(aga)
            pos_list.append(calculate_posscore(aga, secret_code))
            neg_list.append(calculate_negscore(aga, secret_code))
    if calculate_posscore(aga, secret_code) == 4:
        print(f"Found the secret code {secret_code}")
        break

for i in guess_list:
    print(i)

print(guess_list)
print(f"Number of digits in correct position: {pos_list}")
print(f"Number of digits in incorrect position: {neg_list}")
