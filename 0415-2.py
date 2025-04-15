import turtle

pop = ["basic", "caramell", "garlic"]
soda = ["cola", "orange", "grape"] 

for i in pop:
    for j in soda:
        print(i,j)

a = 1
while a < 10:
    print(a)
    a = a+1

b = 0
while b < 6:
    a = 0
    while a < 4:
        turtle.fd(100)
        turtle.left(90)
        a = a + 1
    turtle.right(60)
    b = b + 1