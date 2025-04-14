# 연산자 축약
# x+=y -> x=x+y, x-=y -> x=x-y, x*=y -> x=x*y, x/=y -> x=x/y 등

a = 10 # 수치형
b = 'Hello' # 문자열
c = 3.14 # 실수
d = 3 > 45 # 불형
e = 5 <= 2+3 # 불형


print(int(c))
print(float(c))
print(d)
print(e)
print(type(a), int(a), type(b), b, type(c), float(c), type(d), d, type(e), e)
print(a//c, a%c)
print(a//int(c), a%int(c))
print(not a+c > e)
print(a+c>0 and e)
print(d or e)

# 현재 시각 출력 (안해도됨..그냥 내가 심심해서 해봄)
import time
ct = time.localtime(time.time())
print(f"Current Time: {ct.tm_hour}:{ct.tm_min}:{ct.tm_sec}")
