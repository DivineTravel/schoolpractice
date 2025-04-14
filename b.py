a=10
b=5
print(a != b*2)
print(a == b*2)

c = 3>5
d = True
e = 3<5
print(c and d)
print(not c and d)
print(c or d)

# (), **, * / // %, + -, < <= > >= == !=, not, and, or

x = True
y = False
z = True

r1 = x or y and z
r2 = (x or y) and z
print(r1, r2)

x2 = 4
y2 = 2
r = (x2 + y2) * 3 > 12 and y2 - 1 == 1
print(r)
