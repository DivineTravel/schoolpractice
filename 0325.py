
h = 1.7
w = 60
bmi = w / (h ** 2)
p = print

p(bmi)
p(18.5 <= bmi < 23)
p()
if bmi < 16:
    p("Severe thinness")
if 16 <= bmi < 18.5:
    p("Moderate thinness")
if 18.5 <= bmi < 25:
    p("Normal Weight")
if 25 <= bmi < 30:
    p("Overweight")

import random
r = random
a = r.randint(100, 155)
b = r.randint(60, 100)

p("수축기 혈압:", a, "이완기 혈압:",b)
p("정상 혈압", a < 120 and b < 80)
p("주의 혈압", 120 <= a < 130 and 80 > b)
p("고혈압 전 단계", 140 > a >= 130 or 90 > b >= 80)
p("고혈압", a >= 140 or b >= 90)
p()
if a < 120 and b < 80:
    p("정상 혈압")
if 120 <= a < 130 and 80 > b:
    p("주의 혈압")
if 140 > a >= 130 or 90 > b >= 80:
    p("고혈압 전 단계")
if a >= 140 or b >= 90:
    p("고혈압")

