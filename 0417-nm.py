import time
import random

capital = ["Beijing, Seoul, Kathmandu, Tokyo, Paris"]
capital = capital[0].split(", ")
correct = 0

for i in range(3):
    print("*** problem", i + 1, "***")
    n = random.randint(0, len(capital) - 1)
    word = capital[n]
    print(word)
    user = input()
    if user == word:
        print("Correct!")
        correct += 1
    else:
        print("Wrong!")
success = round(correct / 3, 2)
score = round(correct / 3 * 100, 2)
print("Success rate:", success)
print("Score:", int(score))