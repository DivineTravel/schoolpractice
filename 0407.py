import time

a = [[1,2,3],4,5,[6,[7,8],[9,0]]]
print(a[3][1])
print(a[3][2][1])

name = input("Enter your name: ")
time.sleep(0.1)
age = int(input("Enter your age: "))
time.sleep(0.1)
price = float(input("Enter the price: "))
time.sleep(0.1)
print("Please wait...")
time.sleep(1)
print("Hello", name)
print("You are", age, "years old.")
print("The price is", price)
time.sleep(1)
n1 = 2
n2 = 5
sum = n1 + n2
userInput = input(f"What is the sum of {n1} + {n2}? ")
try:
    intU = int(userInput)
    if intU == sum:
        print("Correct")
    else:
        print("Incorrect")
except ValueError:
    print("Please enter a valid number")