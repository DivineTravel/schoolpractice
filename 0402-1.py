import random

L = ["손더스, 강수린, 김민채, 김보은, 김아윤"]
E = [100, 99, 98, 97, 96]
L = L[0].split(", ")
b = random.randint(0, 4)

print(L)
print()
print(L[b], E[b])
print()
print(L[2:4])
print(E[:3])

E.append(1000)
L.insert(2, "신지혜")
print(E, L)
L.remove("손더스")
L.sort(reverse=True)
E.sort(reverse=True)
print(E,L)
E.pop()
E.pop()
print(E)
print(len(L), len(E))
