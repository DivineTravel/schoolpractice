import time

# Check height limit
height = float(input("Enter your height in cm: "))
try:
    if height < 140:
        print("더블스핀 놀이기구 탑승 불가")
    elif height >= 140:
        print("더블스핀 놀이기구 탑승 가능")
except ValueError:
    print("Enter a valid height")
time.sleep(1)

a = input("Expressway or Normal Road?")
try:
    if a == "Expressway":
        limit = 100
    else:
        b = input("Child Protection Area? (yes/no)")
        if b == "yes":
            limit = 30
        else:
            limit = 50
    print("Speed limit is", limit,"km/h")
except ValueError:
    print("Enter a valid input")
time.sleep(1)

# Ticket price calculation
Age = int(input("Enter your age: "))
ppl = int(input("Enter the number of people: "))
try:
    if Age <= 18:
        print("The ticket price is",40000*ppl,"won")
    elif Age >= 65:
        print("The ticket price is",30000*ppl,"won")
    else:
        print("The ticket price is",50000*ppl,"won")
except ValueError:
    print("Enter a valid input")
