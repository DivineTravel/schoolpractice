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