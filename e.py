import time

ct = time.localtime(time.time())
print(f"Current Time: {ct.tm_hour}:{ct.tm_min}:{ct.tm_sec}")

# x+=y -> x=x+y, x-=y -> x=x-y, x*=y -> x=x*y, x/=y -> x=x/y, etc

a = 10 # 수치형
b = 'Hello' # 문자열
c = 3.14 # 실수
d = 3 > 45 # 불형
e = 5 <= 2+3
g = ct.tm_hour


print(int(c))
print(float(c))
print(d)
print(e)
print(type(a), int(a), type(b), b, type(c), float(c), type(d), d, type(e), e)
print(a//c, a%c)
print(a//int(c), a%int(c))
print(not a+c > g)
print(a+c>0 and e)
print(d or e)


id = "Shin"
E = "235"