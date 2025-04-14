import turtle
# 사각형 그리기
t = turtle.Pen("turtle")
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)


name = '홍길동'
age = 15
phone = '010-1234-5678'
# 이름, 나이, 폰번호 각각 출력
print(name, age, phone)
# 이름 100번 출력
print(name*100)

# 문자열에서 특정 부분만 출력
print('I am useless'[0:4])
print('I am useless'[5:13])
# 문자열의 글자 수 출력
print(len('Expected'),len('n'),len('helloworld'))

