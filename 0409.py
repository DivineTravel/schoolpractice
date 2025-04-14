a = int(input())
try:
    if a % 2 == 0:
        print('짝수')
    else:
        print('홀수')
except ValueError:
    print("Enter a valid input")

n = int(input())
try:
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")
except ValueError:
    print("Enter a valid input")


