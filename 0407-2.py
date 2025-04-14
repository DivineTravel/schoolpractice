adult = 50000
child = 30000
n = int(input("Enter the number of adults: "))
m = int(input("Enter the number of children: "))
total = adult * n + (child * 0.8) * m 
print("Total price:", total)

currentYear = 2025
birthYear = int(input("Enter the year you were born: "))
age = currentYear - birthYear
print("You are", age, "years old.")
