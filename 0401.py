import random
a = [1, 100, "hello", True, 3>5]
print(a)
b = random.randint(0, 4) # 0부터 4까지의 정수 중 하나를 무작위 출력 (안해도 됨)
print(a[b], type(a[b]))
print(a[1:4])
print()

k = [4,2,65,67,90,1000]
k[5] = k[0]+k[1]
k[4] = k[2]>k[3]
print(k)

dessert = ["cake", "ice cream", "coffee"]
dessert.append("pie")
dessert.append("milk")
print(dessert)
dessert.insert(2, "fruit")
dessert.insert(0, "juice")
dessert.remove("cake")
dessert.sort()
