# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스", "주스"}
print(menu, type(menu))

menu = list(menu)
menu.append("주스")
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

# Quiz
from random import *

# 범위 정해서 반복하는 함수 range
users = range(1, 21)
users = list(users)
shuffle(users)
print(users)
print(sample(users, 1))

winners = sample(users, 4)
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))

# 분기
weather = input("오늘 날씨는 어때요?")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("날씨가 맑아요")

temp = int(input("기온은 어때요?"))
if temp >= 30:
    print("너무 더워요. 나가지 마세요")
elif temp >= 10 and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지마세요")
