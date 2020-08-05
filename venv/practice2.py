# 리스트 []

# 지하철 칸별로 10명, 20명, 30명

#subway1 = 10
#subway2 = 20
#subway3 = 30

subway=[10,20,30]
print(subway)
subway=["유재석","조세호","김환승"]
print(subway.index("조세호"))

#하하 추가
subway.append("하하")
print(subway)

# 정형돈을 유재석과 조세호 사이에 삽입
subway.insert(1,"정형돈")
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
subway.pop()
print(subway)

subway.append("유재석")
print(subway)
# 같은 이름의 사람 몇번 나왔는지 갯수 확인
print(subway.count("유재석"))

#정렬도 가능
num_list=[5,2,4,3,1]
print(num_list)
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)
num_list.clear()
print(num_list)

#리스트는 다양한 자료형 함께 사용
mixed_list = ["조세호",20,True]
num_list = [1,2,3]
print(mixed_list)
num_list.extend(mixed_list)
print(num_list)

# 변수 = {key:value}
cabinet={3:"유재석",100:"김환승"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#주의할점
print(cabinet.get(5))
print("hi")
#key를 통한 데이터를 임시로 출력 가능
print(cabinet.get(5,"사용가능"))

print( 3 in cabinet)
print( 5 in cabinet)

cabinet = {"A-3":"유재석","B-100":"김환승"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

#Key 들만 출력
print(cabinet.keys())
#value 들만 출력
print(cabinet.values())
#key,value 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)

#집합(set)
#중복 x 순서 없음 !!
my_set={1,2,3,3}
print(my_set)

java={"유재석","김태호","양세형"}
python=set(["유재석","박명수"])
#교집합 (java와 python)
print(java&python)
print(java.intersection(python))

#합집함
print(java | python)
print(java.union(python))

#차집함(java는 할수있지만 파이썬은 할줄 모르는 개발자)
print(java-python)
print(java.difference(python))

#python 할줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 잊은 개발자
java.remove("김태호")
print(java)




