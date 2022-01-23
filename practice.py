# Git에 추가 하려면 

# git init - 초기화, 프로젝트 처음에만 한번
# git add . - 추가할 파일 더하기 - 파일이 하나라면 . 대신에 파일명 넣기
# git status - 상태확인
# git commit -m "first/second commit" - Rivision/history 관리
# git remote add origin https://github.com/roehd26/Practice.git - github repository와 내 로컬 프로젝트와 연결 (Github에서 복사해서 붙여와야 함)
# git remote -v - 잘 연결 되었는지 확인
# git push origin master - Github로 올리기 (master 자리에는 branch 이름이 들어가면 됨, branch 이름이 main이라 하면 git push origin main이라고 써야함)

# Github에 계속 업데이트 하는 법

# git add . - 추가할 파일 더하기
# git commit -m "first commit" - 히스토리 만들기
# git push origin master - Github로 올리기


# 숫자 자료형 ()

# print(5)
# print(-10)
# print(3.14)
# print(1000)

# print(5+3)
# print(2*8)
# print(3*(3+1))

# 문자열 자료형 ()

# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ" * 9)

# boolean 자료형 () - 참 / 거짓

# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 > 10))

# 변수 ()

#애완동물을 소개해 주세요~

# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >= 3

# print("우리집 " + animal + "의 이름은 " + name + "에요")
# hobby = "공놀이" # 변수는 문자 중간에 선언할 수도 있다
# #print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요") # 정수형의 경우는 +를 포함한 print문에서 쓰이기 위해서는 str로 감싸줘야 한다. 정수형을 문자형으로 바꿔 준다
# print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요") # +가 아닌 콤마로도 여러 문장을 합칠 수 있다. - str없이도 정수형/boolean 출력 가능, 콤마가 들어가면 빈칸이 하나씩 들어감
# print(name + "는 어른일까요? " + str(is_adult)) # boolean형도 정수형과 똑같이 str로 감싸줘야 한다.

# 주석 ()
# 코드내에 포함은 되어 있지만 실행은 되지 않는 것 - 개발자와의 소통, 설명이 더 필요할 때

''' 이렇게
하면
여러문장이
주석처리 됩니다
'''
# "crtl + /" 를 하면 일괄적으로 주석이 설정이 된다

# 퀴즈 #1
# Quiz) 변수를 이용하여 다음 문장을 출력하시오.quit

# 변수명
#  : Station

# 변수값
#  : "사당", "신도림", "인천공항" 순서대로 입력

#  출력문장
#  : xx 행 열차가 들어오고 있습니다.

# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다.")

# 연산자 ()

# print(1+1) # 2
# print(3-2) # 1
# print(5*2) # 10
# print(6/3) # 2

# print(2**3) # 2^3 = 8
# print(5%3) # 나머지 구하기 2
# print(10%3) # 1
# print(5//3) # 몫 구하기 1
# print(10//3) # 3

# print(10 > 3) # True
# print(4 >=7) # False
# print(10 < 3) # False
# print(5 <= 5) # True

# print(3==3) # True
# print(4==2) # False
# print(3 + 4 == 7) # True

# print(1 != 3) #True
# print(not(1 !=3)) # False

# print((3>0) and (3 < 5)) # True
# print((3 > 0) & (3 < 5)) # True

# print((3 > 0) or (3 > 5)) # True
# print((3 > 0) | (3 > 5)) # True

# print(5 > 4 > 3) # True
# print(5 > 4 > 7) # False

# 간단한 수식 ()

# print(2 + 3 * 4) # 14
# print((2 + 3) * 4) # 20
# number = 2 + 3 *4 # 14
# print(number)
# number = number + 2 # 16
# print(number)
# number += 2 #18
# print(number)
# number *= 2 # 36
# print(number)
# number /= 2 # 18
# print(number)
# number -= 2 #16
# print(number)

# number %= 5 # 1
# print(number)

# 숫자 처리 함수 ()

# print(abs(-5)) # 5
# print(pow(4, 2)) # 4^2 = 4*4 = 16
# print(max(5, 12)) # 12
# print(min(5, 12)) # 5
# print(round(3.14)) # 3
# print(round(4.99)) # 5

# from math import * #  math 라이브러리에서 모든 걸 사용한다.
# print(floor(4.99)) # 내림 4
# print(ceil(3.14)) # 올림 4
# print(sqrt(16)) # 제곱근 4

# 랜덤 함수 ()

# from ipaddress import NetmaskValueError
# from random import * # random 라이브러리에서 모든 걸 사용한다.

# print(random()) # 0.0 ~ 1.0 미만의 임의의 값을 생성
# print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값을 생성

# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 정수값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 정수값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 정수값 생성

# print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성

# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

# print(randint(1, 45)) # 1 ~ 45이하의 임의의 값 생성 - 양 끝의 숫자 포함
# print(randint(1, 45)) # 1 ~ 45이하의 임의의 값 생성 - 양 끝의 숫자 포함
# print(randint(1, 45)) # 1 ~ 45이하의 임의의 값 생성 - 양 끝의 숫자 포함
# print(randint(1, 45)) # 1 ~ 45이하의 임의의 값 생성 - 양 끝의 숫자 포함
# print(randint(1, 45)) # 1 ~ 45이하의 임의의 값 생성 - 양 끝의 숫자 포함
# print(randint(1, 45)) # 1 ~ 45이하의 임의의 값 생성 - 양 끝의 숫자 포함

# 퀴즈 #2 (45:00)

# Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건 1: 랜덤으로 날짜를 뽑아야 함
# 조건 2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건 3: 매월 1~3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정 되었습니다.

# date = randrange(4, 29)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정 되었습니다.")

# date = randint(4, 28)


# 문자열 ()

# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이선은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)


# 슬라이싱 ()

# jumin = "990120-1234567"

# print("성별: " + jumin[7])
# print("연: " + jumin[0:2]) # 0 부터 2 직전까지 (0, 1)
# print("월: " + jumin[2:4])
# print("일: " + jumin[4:6])

# print("생년월일: " + jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7 자리: " + jumin[7:]) # 7번째 부터 끝까지
# print("뒤 7 자리 (뒤에 부터): " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지 - 맨 뒷자리는 -1번째가 된다

# 문자열 처리 함수 () (55:00)

# python = "Python is Amazing"
# print(python.lower()) # 모든 문자가 소문자로
# print(python.upper()) # 모든 문자가 대문자로
# print(python[0].isupper()) #python의 0번째 문자가 대문자 인지 True/False

# print(len(python)) # 문자열 길이
# print(python.replace("Python", "Java")) # python문자를 찾아 Java로 바꾼다

# index = python.index("n")
# print(index)
# index = python.index("n", index +1) # 앞에서 찾은 5 번째 n 그 다음 부터 n을 찾기 시작 
# print(index)

# print(python.find("n"))
# print(python.find("Java")) # 내가 찾는 값이 문자열에 포함되어 있지 않은 경우는 -1 반환 - 있다면 0 반환
# print(python.index("Java")) # python에는 Java가 없기 때문에 오류를 내고 프로그램 종료 - Java가 있다면 위치를 표시해 줌

# print(python.count("n")) # 문자열에 n이 몇개 있는지

# 문자열 포맷 () (1:00:55)

# print("a" + "b")
# print("a", "b")

# 방법 1
# print("나는 %d살 입니다." % 20) # % 뒤의 값을 문자열에 넣겠다 - d는 정수를 의미
# print("나는 %s을 좋아해요." % "파이썬") # s는 문자열을 의미
# print("Apple은 %c로 시작해요." % "A") # c는 문자 하나만 의미

# %s
# print("나는 %s살 입니다." % 20) # % 뒤의 값을 문자열에 넣겠다 - d는 정수를 의미
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
# print("나는 {}살 입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨간", age = 20))

# 방법 4 (v3.6 이상)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출 문자 () (1:09:17)

# print("백문이 불여일견\n백견이 불여일타") # \n: 줄바꿈

# 저는 "나도코딩" 입니다.
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")
# print("저는 \'나도코딩\'입니다.")

# # \\: 문장 내에서 \
# print("C:\\Users\\MTCA\\Desktop\\PythonWorkSpace>")

# # \r: 커서를 맨 앞으로 이동
# print("Red Apple\rPine") # PineApple

# # \b: 백스페이스 (한 글자 삭제)
# print("Redd\bApple") # RedApple

# # \t: 탭
# print("Red\tApple") # Red   Apple

# 퀴즈 #3
# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1: http:// 부분은 제외 => naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제회 => Never
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 +"!" 로 구성
#                 (nav)              (5)           (1)             (!)

# 예) 생성된 비밀번호: nav51!

# webpage = "http://naver.com"

# index = webpage.index("/") + 2
# dot = webpage.index(".")
# site = webpage[index:dot]

# print(site)

# letter = site[:3] 
# leng = len(site)
# enumber = site.count("e")

# password = str(letter) + str(leng) + str(enumber) + "!"

# print(password)

# Answer
# url = "http://naver.com"
# my_str = url.replace("http://", "") # 규칙1
# # print(my_str)
# my_str = my_str[:my_str.index(".")] # 규칙2
# # my_str[0:5] -> 0 ~ 5 직전까지, (0, 1, 2, 3, 4)
# # print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀 번호는 {1}입니다." .format(url, password))

# 리스트 - 순서를 가지는 객체의 집합 (1:22:30)

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하") #append를 하면 항상 맨 뒤에 붙음
# print(subway)

# # 정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1, "정형돈") # insert (추가할 위치, "추가할 이름")
# print(subway)

# #지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# #다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
# print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# 사전 자료형 () (1:31:40)

# cabinet = {3:"유재석", 100:"김태호"} # 예) 목욕탕에 손님이 와서 cabinet의 key를 사용
# print(cabinet[3]) # 출력 하려면 키값을 넣으면 됨
# print(cabinet[100])
# print(cabinet.get(3))

# print(cabinet[5]) #없는 key 값을 넣으면 프로그램은 오류가 나면서 종료되고, 뒤의 내용도 안나옴
# print(cabinet.get(5)) #get을 이용해서 없는 값을 출력하려 하면 "None" 이 출력 되고 프로그램은 계속 진행이 된다
# print(cabinet.get(5, "사용 가능"))
# print("hi")

# print(3 in cabinet) # True 사전 자료형 안에 값이 있는지 확인하는 기능
# print(5 in cabinet) # False

# cabinet = {"A-3":"유재석", "B-100":"김태호"} # Key를 정수형이 아닌 srting으로 사용 해도 됨
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님 - 값을 업데이트 하거나 추가
# print(cabinet)
# cabinet["A-3"] = "김종국" # 기존의 값은 지워지고 새로운 값이 들어감, 유재석 -> 김종국
# cabinet["C-20"] = "조세호" # 새로운 Key와 값이 추가
# print(cabinet)

# # 간 손님 - key를 삭제
# del cabinet["A-3"]
# print(cabinet)

# # key들만 출력
# print(cabinet.keys())

# # value들만 출력
# print(cabinet. values())

# # ket, value 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)

# 튜플 () (1:40:46) - 리스트와 다르게 내용을 변경이나 추가를 할 수 없지만, 속도가 리스틉 보다 빠르다

# 돈가스 집
# menu = ("돈가스", "치즈가스")
# print(menu[0])
# print(menu[1])

# menu.add("생선가스") - error 발생 - AttributeError: 'tuple' object has no attribute 'add'

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩") # 튜플 형식으로 변수 선언
# print(name, age, hobby)

# 세트 () (1:43:24)

# 집합 (set)
# 중복 안됨, 순서 없음

# my_set = {1,2,3,3,3} # 중괄호는 사전에서도 썼었지만, key와 value를 같이 썼음, 세트에서는 그냥 값만 나열 하면 됨
# print(my_set) #세트는 중복을 허용하지 않기 때문에 뒤에 반복 되는 내용은 무시

# java = {"유재석", "김태호","양세형"} # java를 할 줄 아는 개발자
# python = set(["유재석", "박명수"]) # python을 할 줄 아는 개발자

# # 교집합 (java와 python을 모두 할 수 있는 개발자)
# print(java & python) # 유재석만 출력
# print(java.intersection(python))

# # 합집합 (java 할 수 있거나 python을 할 수 있는 개발자)
# print(java | python)
# print(java.union(python)) # 순서는 보장 되지 않음

# # 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java 를 잊었어요
# java.remove("김태호")
# print(java)

# 자료구조의 변경 () (1:48:44)

# 커피숍 메뉴에 대해

# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))  # {'커피', '주스', '우유'} <class 'set'>

# menu = list(menu)
# print(menu, type(menu))  # ['커피', '주스', '우유'] <class 'list'>

# menu = tuple(menu)
# print(menu, type(menu))  # ('커피', '주스', '우유') <class 'tuple'>

# menu = set(menu)
# print(menu, type(menu))  # {'커피', '주스', '우유'} <class 'set'>

# 퀴즈 #4 (1:50:47)

# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3: random 모듈의 shuffle과 sample을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자: 1
# 커피 당첨자: [2, 3, 4]
# -- 축하합니다 --

# (활용 예제)
from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

# reply = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(reply)

# chicken = sample(reply, 1)
# print(chicken)
# # reply2 = reply - chicken
# coffee = sample(reply, 3)

# print("-- 당첨자 발표--")
# print("치킨 당첨자:", chicken)
# print("커피 당첨자", coffee)
# print("--축하합니다--")

# Answer

from random import *
users = range(1,21) # 1부터 21 직전(20)까지 숫자를 생성, 하지만 타입이 range이기 때문에 list의 함수를 쓸 수 없음
# print(type(users))
users = list(users)
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피

print("-- 당첨자 발표--")
print("치킨 당첨자: {0}" .format(winners[0]))
print("커피 당첨자: {0}" .format(winners[1:]))
print("--축하합니다--")

# if () (1:57:33)
