import random
import time

t = time
a = [1, 100, "hello", True, 3>5]
print(a)
b = random.randint(0, 4)
print(a[b], type(a[b]))
print(a[1:4])
print()

t.sleep(1)

def f(x, y):
    return x + y
print(f(3, 5))
print()

t.sleep(1)
print()
print("1/4/2025 3:00 PM")
t.sleep(1)
print()
t.sleep(1)
print("견뎌내기 힘들 정도로")
t.sleep(1)
print("무력감이 나를 덮친다")
t.sleep(1)
print()
t.sleep(1)
print("설명할 수 없을 만큼")
t.sleep(1)
print("서있기조차 힘이 든다")
t.sleep(1)
print()
t.sleep(1)
print("금방이라도 쓰러져서")
t.sleep(1)
print("어딘가 기대고만 싶다")
t.sleep(1)
print()


k = [4,2,65,67,90,1000]
k[5] = k[0]+k[1]
k[4] = k[2]>k[3]
print(k)
print()

dessert = ["cake", "ice cream", "coffee"]
dessert.append("pie")
dessert.append("milk")
print(dessert)
dessert.insert(2, "fruit")
dessert.insert(0, "juice")
dessert.remove("cake")
dessert.sort()
