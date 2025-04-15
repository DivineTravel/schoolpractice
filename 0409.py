# 짝수/홀수 판별
a = int(input())
try:
    if a % 2 == 0:
        print('짝수')
    else:
        print('홀수')
except ValueError:
    print("Enter a valid input")

# 양수/음수/0 판별
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


