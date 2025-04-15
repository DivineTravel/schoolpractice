import turtle

t = turtle.Pen("turtle")

for b in range(6):
    for a in range(4):
        t.fd(100)
        t.left(90)
    t.right(60)

for c in range(10):
    for d in range(5):
        t.fd(100)
        t.left(72)
    t.right(36)
turtle.done()

for dan in range(2,10):
    print(f"{dan}단")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan*i}")
    print()