import time
import turtle

for x in range(10):
    turtle.forward(100)
    turtle.right(36)

for a in [1, 2, 3]:
    print(a)
for b in 'hello':
    print(b)
for c in range(1,4):
    print(c)

d = int(input("Multiplication table: "))
for n in range(1, 10):
    print(f"{d} x {n} = {d*n}")

# 5초 타이머
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Time Up!')
t = 5
countdown(int(t))

# 100이하의 5의 배수 출력
for number in range(5, 100, 5):
    print(number)

