print(abs(-5))
print(pow(4, 2))
print(max(5, 12))
print(min(5, 12))
print(round(3.14))
print(round(4.99))

from math import *

print(floor(4.99))  ##버림
print(ceil(3.14))  ##올림
print(sqrt(16))  # 제곱근

from random import *

print(random() * 10)  # 0.0~10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0~ 10 미만의 임의 값 생성
print(int(random() * 10))  # 0~ 10 미만의 임의 값 생성
print(int(random() * 10))  # 0~ 10 미만의 임의 값 생성
print(int(random() * 10) + 1)  # 1~ 10 미만의 임의 값 생성
print(int(random() * 10) + 1)  # 1~ 10 미만의 임의 값 생성
print(int(random() * 10) + 1)  # 1~ 10 미만의 임의 값 생성
print(int(random() * 10) + 1)  # 1~ 10 미만의 임의 값 생성

# 로또값
print(int(random() * 45) + 1)  # 1~45 이하의 임의의 값 생성

print(randrange(1, 46))  # 1~46미만의 임의의 값 생성

print(randint(1, 45))  # 1~45이하의 임의의 값 생성

print("오프라인 스터디 모임 날짜는 매월 " + str(randint(4, 28)) + "일로 선정되었습니다")

sentence = '나는 소년입니다 '
print(sentence)
sentence2 = '파이썬은 쉬워요'
print(sentence2)

##슬라이싱##
jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("년 : " + jumin[0:2])  # 0부터 2직전까지
print("월 :" + jumin[2:4])  # 0부터 4직전까지
print("일 :" + jumin[4:6])  # 0부터 4직전까지
print("생년월일 : " + jumin[0:6])
print("뒤 7자리 : " + jumin[-7:])  # 뒤에서 7자리

python="Python is Amaizing"
print(python.find("Java"))
print(python.count("n"))

print("a","b")
print("나는 %d살"%20)

print("나는 {}살입니다".format(20))
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))
print("나는 {age}살이며 {color}색을 좋아해요".format(age=20,color="파랑"))

print("저는 \"나도 코딩\" 입니다")

print("Red Apple\rPine")

url="http://naver.com"
url="http://google.com"
url=url.replace("http://","")
url=url[:url.index(".")]
print(url)
password=url[:3]+str(len(url))+str(url.count("e"))+"!"
print(password)




