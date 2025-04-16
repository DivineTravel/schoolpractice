i = 1
while i < 6:
    print("옥련여고")
    i += 1

while 1:
    n = input("Type Q or q to exit: ")
    if n == 'Q' or n == 'q':
        break

total = 0
count = 0
for num in range(1, 101):
    if num % 2 != 0:
        continue
    total += num
    count += 1
print(total, count)

import random
n = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
while guess != n:
    if guess < n:
        print("Higher")
    else:
        print("Lower")
    guess = int(input("Guess again: "))
print("Correct!")

f = random.randint(1, 10)
g = int(input("Guess a number between 1 and 10: "))
tries = 1
for x in range(10):
    if g == f:
        print("Correct!")
        break
    elif g < f:
        print("Higher")
    else:
        print("Lower")
    g = int(input("Guess again: "))
    tries += 1
print("You tried", tries, "times")