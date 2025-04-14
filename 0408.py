import time

# Check height limit for a ride
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
time.sleep(1)

# Ticket price calculation advanced
a1 = int(input("enter the age of the first person"))
a2 = int(input("enter the age of the second person"))
a3 = int(input("enter the age of the third person"))
try:
    if a1 <= 18:
        p1 = 40000
    elif a1 >= 65:
        p1 = 30000
    else:
        p1 = 50000
    if a2 <= 18:
        p2 = 40000
    elif a2 >= 65:
        p2 = 30000
    else:
        p2 = 50000
    if a3 <= 18:
        p3 = 40000
    elif a3 >= 65:
        p3 = 30000
    else:
        p3 = 50000
    total_price = p1 + p2 + p3
    print("The total price is", total_price, "won")
except ValueError:
    print("Enter a valid input")
time.sleep(1)

# Ticket Price calculation advanced 2 (improved)
def calPrice(age):
    if age <= 18:
        return 40000
    elif age >= 65:
        return 30000
    else:
        return 50000

def validAge(prompt):
    while True:
        try:
            age = int(input(prompt))
            if age >= 0:  
                return age
            else:
                print("Please enter a valid age (non-negative).")
        except ValueError:
            print("Invalid input. Please enter a valid integer for age.")
try:
    age1 = validAge("Enter the age of the first person: ")
    age2 = validAge("Enter the age of the second person: ")
    age3 = validAge("Enter the age of the third person: ")

    price1 = calPrice(age1)
    price2 = calPrice(age2)
    price3 = calPrice(age3)

    total = price1 + price2 + price3
    print("The total price is", total, "won")
except Exception as e:
    print(f"An error occurred: {e}")
time.sleep(1)

print("End of program")
