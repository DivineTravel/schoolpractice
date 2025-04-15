s = int(input())
if s >= 80:
    print("A")
elif s >= 60:
    print("B")
else:
    print("C")

def calgrade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'E'
def validscore(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100: 
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid score.")
score = validscore("Enter your score: ")
grade = calgrade(score)
print("Your grade is:", grade)

height = int(input("Enter your height in cm: "))
try:
    if height < 100:
        print("You are too short")
    elif height <= 130:
        print("You can ride with an adult")
    elif height <= 195:
        print("You can ride alone")
    else:
        print("You are too tall")
except ValueError:
    print("Enter a valid input")

