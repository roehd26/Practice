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


# 숫자 자료형 (2-1) (7:26)

# print(5)
# print(-10)
# print(3.14)
# print(1000)

# print(5+3)
# print(2*8)
# print(3*(3+1))

# 문자열 자료형 (2-2) (11:42)

# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ" * 9)

# boolean 자료형 (2-3) - 참 / 거짓 (13:08)

# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 > 10))

# 변수 (2-4) (15:06)

# 애완동물을 소개해 주세요~

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

# 주석 (2-5) (22:08)
# 코드내에 포함은 되어 있지만 실행은 되지 않는 것 - 개발자와의 소통, 설명이 더 필요할 때

''' 이렇게
하면
여러문장이
주석처리 됩니다
'''
# "crtl + /" 를 하면 일괄적으로 주석이 설정이 된다

# 퀴즈 #1 (23:58)
# Quiz) 변수를 이용하여 다음 문장을 출력하시오.

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

# 간단한 수식 (3-2) (33:23)

# print(2 + 3 * 4) # 14
# print((2 + 3) * 4) # 20
# number = 2 + 3 * 4 # 14
# print(number)
# number = number + 2 # 16
# print(number)
# number += 2 #18
# print(number)
# number *= 2 # 36
# print(number)
# number /= 2 # 18.0
# print(number)
# number -= 2 #16.0
# print(number)

# number %= 5 # 1.0
# print(number)

# 숫자 처리 함수 (3-2) (36:25)

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

# 랜덤 함수 (3-4) (39:00)

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

# 퀴즈 #2 (44:10)

# Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건 1: 랜덤으로 날짜를 뽑아야 함
# 조건 2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건 3: 매월 1~3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정 되었습니다.

# from random import *

# date = randrange(4, 29)
# print("오프라인 스터디 모임 날짜는 매월", date, "일로 선정 되었습니다.")

# # Answer

# date = randint(4, 28)
# print("오프라인 스터디 모음 날짜는 매월 " + str(date) + "일로 선정 되었습니다.")

# 문자열 (4-1) (46:57)

# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이선은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)


# 슬라이싱 (4-2) (48:25)

# jumin = "990120-1234567"

# print("성별: " + jumin[7])
# print("연: " + jumin[0:2]) # 0 부터 2 직전까지 (0, 1)
# print("월: " + jumin[2:4])
# print("일: " + jumin[4:6])

# print("생년월일: " + jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7 자리: " + jumin[7:]) # 7번째 부터 끝까지
# print("뒤 7 자리 (뒤에 부터): " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지 - 맨 뒷자리는 -1번째가 된다

# 문자열 처리 함수 (4-3) (55:10)

# python = "Python is Amazing"
# print(python.lower()) # 모든 문자가 소문자로
# print(python.upper()) # 모든 문자가 대문자로
# print(python[0].isupper()) #python의 0번째 문자가 대문자 인지 True/False

# print(len(python)) # 문자열 길이
# print(python.replace("Python", "Java")) # python문자를 찾아 Java로 바꾼다

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1) # 앞에서 찾은 5 번째 n 그 다음 부터 n을 찾기 시작 
# print(index)

# print(python.find("n"))
# print(python.find("Java")) # 내가 찾는 값이 문자열에 포함되어 있지 않은 경우는 -1 반환 - 있다면 0 반환
# # print(python.index("Java")) # python에는 Java가 없기 때문에 오류를 내고 프로그램 종료 - Java가 있다면 위치를 표시해 줌

# print(python.count("n")) # 문자열에 n이 몇개 있는지

# 문자열 포맷 (4-4) (1:00:55)

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

# 탈출 문자 (4-5) (1:09:17)

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

# 퀴즈 #3 (1:15:50)
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

# print("{0}의 비밀 번호는 {1}입니다." .format(webpage, password))

# Answer
# url = "http://naver.com"
# my_str = url.replace("http://", "") # 규칙1
# # print(my_str)
# my_str = my_str[:my_str.index(".")] # 규칙2 my_str[0:5] -> 0 ~ 5 직전까지, (0, 1, 2, 3, 4)
# # print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀 번호는 {1}입니다." .format(url, password))

# 리스트 - 순서를 가지는 객체의 집합 (5-1) (1:22:30)

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

# 사전 자료형 (5-2) (1:31:40) - 단어와 뜻이 있는 사전 처럼, 사전 자료형도 키와 value로 나온다.

# cabinet = {3:"유재석", 100:"김태호"} # 예) 목욕탕에 손님이 와서 cabinet의 key를 사용
# print(cabinet[3]) # 출력 하려면 키값을 넣으면 됨
# print(cabinet[100])
# print(cabinet.get(3))

# print(cabinet[5]) #없는 key 값을 넣으면 프로그램은 오류가 나면서 종료되고, 뒤의 내용도 안나옴
# print(cabinet.get(5)) #get을 이용해서 없는 값을 출력하려 하면 "None" 이 리턴 되고 프로그램은 계속 진행이 된다
# print(cabinet.get(5, "사용 가능")) # 없는 값을 찾을 경우 기본값을 설정하고 싶을 때
# print("hi")

# print(3 in cabinet) # True 사전 자료형 안에 값이 있는지 확인하는 기능
# print(5 in cabinet) # False

# cabinet = {"A-3":"유재석", "B-100":"김태호"} # Key를 정수형이 아닌 srting으로 사용 해도 됨
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# print(cabinet.get("A-3"))

# # 새 손님 - 값을 업데이트 하거나 추가
# print(cabinet)
# cabinet["A-3"] = "김종국" # 기존의 값은 지워지고 새로운 값이 들어감, 유재석 -> 김종국
# cabinet["C-20"] = "조세호" # 새로운 Key와 값이 추가, C-20에 이미 값이 있다면 업데이트가 됨
# print(cabinet)

# # 간 손님 - key를 삭제
# del cabinet["A-3"]
# print(cabinet)

# # key들만 출력
# print(cabinet.keys())

# # value들만 출력
# print(cabinet.values())

# # key, value 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)

# 튜플 (5-3) (1:40:46) - 리스트와 다르게 내용을 변경이나 추가를 할 수 없지만, 속도가 리스트 보다 빠르다

# 돈가스 집
# menu = ("돈가스", "치즈가스")
# print(menu[0])
# print(menu[1])

# menu.add("생선가스") - error 발생 - AttributeError: 'tuple' object has no attribute 'add'

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# name, age, hobby = "김종국", 20, "코딩" # 튜플 형식으로 변수 선언
# print(name, hobby)

# 세트 (5-4) (1:43:20)

# 집합 (set)
# 중복 안됨, 순서 없음

# my_set = {1,2,3,3,3,2,1} # 중괄호는 사전에서도 썼었지만, key와 value를 같이 썼음, 세트에서는 그냥 값만 나열 하면 됨
# print(my_set) #세트는 중복을 허용하지 않기 때문에 뒤에 반복 되는 내용은 무시

# java = {"유재석", "김태호","양세형"} # java를 할 줄 아는 개발자
# python = set(["유재석", "박명수"]) # python을 할 줄 아는 개발자

# print(type(java))
# print(type(python))

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
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

# reply = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(reply)

# chicken = sample(reply, 1)
# print(chicken)
# # reply2 = reply - chicken # 원래 문자열에서 선택한 내용을 어떻게 제외 하는지?
# coffee = sample(reply, 3)

# print("-- 당첨자 발표--")
# print("치킨 당첨자:", chicken)
# print("커피 당첨자", coffee)
# print("--축하합니다--")

# Answer

# from random import *
# users = range(1,21) # 1부터 21 직전(20)까지 숫자를 생성, 하지만 타입이 range이기 때문에 list의 함수를 쓸 수 없음
# # print(type(users))
# users = list(users)
# # print(type(users))

# print(users)
# shuffle(users)
# print(users)

# winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피

# print("-- 당첨자 발표--")
# print("치킨 당첨자: {0}" .format(winners[0]))
# print("커피 당첨자: {0}" .format(winners[1:]))
# print("--축하합니다--")

# if (6-1) (1:57:33)

# weather = "미세먼지"
# if 조건:
#     실행 명령문

# weather = input("오늘 날씨는 어때요? ")

# if weather == "비" or weather =="눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요?"))
# if 30<= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp <30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp and temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# for (6-2) (2:05:11)

# print("대기번호: 1")
# print("대기번호: 2")
# print("대기번호: 3")
# print("대기번호: 4")

# randrange() 참고
# for waiting_no in range(1, 6): # 1,2,3,4,5 - 6 직전까지
#     print("대기번호: {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0} 커피가 준비 되었습니다.".format(customer))

# while (6-3) (2:09:33)

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기 처분 되었습니다.")

# # 무한 루프에 빠지는 경우 - 빠져 나오기 위해서는 Ctrl + C 누름
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

# continue 와 break (6-4) (2:15:00)

# 수업중 순서대로 책을 읽고 있는데 2, 5번 학생이 결석인 경우
# absent = [2, 5, 8] # 결석
# no_book = [9] # 책을 깜빡했음
# for student in range(1, 11): #1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue # continue 이후의 명령을 더이상 실행시키지 않고, 다음 반복 조건으로 계속 진행
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break # break는 지금 상황에서 바로 반복문을 종료
#     print("{0}, 책을 읽어봐".format(student))

# 한 줄 for () (2:19:11)

# 출석 번호가 원래 1 2 3 4 이지만, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
# student = [1,2,3,4,5]
# print(student)
# student = [i+100 for i in student] # i에 100을 더한 값을 넣을텐데, i는 student에 있는 값을 하나씩 불러오면서, 거기에 100을 더한 값을 리스트로 바꿔서 student에 저장
# print(student)

# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

# 퀴즈 #5
# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2: 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭 해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간: 15분)
# [ ] 2번째 손님 (소요시간: 50분)
# [O] 3번째 손님 (소요시간: 5분)
# ...
# [ ] 50번째 손님 (소요시간: 16분)

# 총 탑승 승객: 2 분

# from random import *
# customer = range(1,51)
# customer = list(customer)
# # print(customer, type(customer))

# # time = randrange(5,51)
# # print(time, type(time))

# total = 0

# for cust in customer:
#     time = randrange(5,51)
#     if time >= 5 and time <= 15 :
#         total += 1
#         print("[O] {0}번째 손님 (소요시간: {1}분)".format(cust, time))
#     else:
#         print("[ ] {0}번쨰 손님 (소요시간: {1}분)".format(cust, time))
# print("총 탑승 승객: {0} 분".format(total))

# range로 난수 생성시 자료 타입은 range -> list로 바꿔줘야 하고, randrange로 난수 생성시는 int형으로 바로 비교 연산 할 수 있음

# # Answer

# from random import *
# cnt = 0 # 총 탑승 승객 수
# for i in range(1, 51): # 1~50 이라는 수 (승객)
#     time = randrange(5, 51) # 5분 ~ 50분 소요 시간
#     if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님(매칭 성공), 탑숭 승객 수 증가 처리
#         print("[O] {0}번쨰 손님 (소요시간: {1}분".format(i, time))
#         cnt += 1
#     else: # 매칭 실패한 경우
#         print("[ ] {0}번쨰 손님 (소요시간: {1}분".format(i, time))

# print("총 탑승 승객: {0} 분".format(cnt))

# 함수 (7-1) (2:28:35)

# def open_account(): # 함수 정의 시에는 "def + 함수 이름() + :"
#     print("새로운 계좌가 생성 되었습니다.")

# # 함수는 정의만 해 두는 것으로 실제로 호출 하기 전까지는 실행 하지 않는다.

# open_account() # 함수 호출

# 전달값과 반환값 (7-2) (2:30:10)

# def open_account():
#     print("새로운 계좌가 생성 되었습니다.")

# def deposit(balance, money):
#     print("새로 {0}원이 입금 되었습니다. 총 잔액은 {1}원 입니다.".format(money, balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("{0}원이 인출 되었습니다. 총 잔액은 {1}원입니다.".format(money, balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
#         return balance


# open_account()
# deposit(10000, 2000)
# withdraw(1000, 3000)


# def open_account(): # 함수 정의 시에는 "def + 함수 이름() + :"
#     print("새로운 계좌가 생성 되었습니다.")

# def deposit(balance, money): # 입금
#     print("입금이 완료 되었습니다. 잔액은 {0} 원 입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): # 출금
#     if balance >= money: # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원 입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원 입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money): #저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission # 여러개의 값을 튜플 형식으로 반환

# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원 입니다.".format(commission, balance))

# 기본값 (7-3) (2:37:50) # 기본값을 설정하는 방법

# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang)) # 역 슬래쉬(\)를 사용하면 두줄의 내용을 한줄로 이어 준다.

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# # 같은 학교 같은 학년 같은 반 같은 수업

# def profile(name, age=17, main_lang="파이썬"): # 함수가 호출 될때 값을 전달 받지 못하면 기본값을 사용한다.
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang)) # 역 슬래쉬(\)를 사용하면 두줄의 내용을 한줄로 이어 준다.

# profile("유재석", 19, "자바")
# profile("김태호")

# 키워드 값 (7-4) (2:41:32) 

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# #함수에서 전달 받는 매개변수의 값을 키워드를 이용해서 함수를 호출 해 주면, 그 키워드에 해당하는 값이 순서가 뒤섞여 있어도 잘 전달 됨
# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")

# 가변인자 (7-5) (2:43:05)

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0} \t나이: {1} \t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름: {0} \t나이: {1} \t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print() # 마지막에 줄 바꿈을 위해서 print 문만 넣음

# profile("유재석", 20, "Python", "Java","C", "C++", "C#")
# profile("김태호", 20, "Kotlin", "Swift") # Kotlin - 안드로이드 개발 언어, Swift - iOS 개발 언어

# 지역변수와 전역변수 (7-6) (2:47:56)

# gun = 10

# def checkpoint(Soldiers): #경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - Soldiers
#     print("[함수 내] 남은 총: {0}".format(gun)) # 전역 공간에 있는 gun의 값도 변경된다

# def checkpoint_return(gun, soldiers): # 전역 변수를 매개 변수로 받기는 하지만 지역에서 계산되어 값을 반환한다.
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))
#     return gun # 반환 되는 값을 다시 전역 변수에 저장하면 값이 변경 되지만 다른 변수에 저장 하면 전역 변수의 값은 그대로 유지된다.

# print("전체 총: {0}".format(gun))
# gun = checkpoint_return(gun, 3) # 2명이 경계 근무 나감, 함수를 호출 하는 곳에서 변경 값을 받아서 저장
# print("남은 총: {0}".format(gun)) # 함수 내에서 전역 변수에 대해 변경이 있으면 함수 이후에도 그 값이 남아 있음

# 함수내에서 전역 변수의 값을 바로 사용하는 방법은 지양하고, 함수 호출 후 넘겨준 전역 변수 값을 계산 후, 리턴 되는 값을 사용 하는 것을 권장

# 퀴즈 #6 (2:53:57)

# Quiz) 표준 체중을 구하는 프로그램을 작성하시오.

# * 표준 체중: 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자: 키(m) x 키(m) x 22
# 여자: 키(m) x 키(m) x 21

# 조건1: 표준 체중은 별도의 함수 내에서 계산
#  * 함수명: std_weight
#  * 전달값: 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점 둘째 자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# height = 168
# gender = "여자"

# def std_weight(height, gender):
#     if gender == "여자":
#         return height * height * 21
#     else:
#         return height * height * 22
    
# weight = round(std_weight(height / 100, "남자"), 2)

# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# def std_weight (height, gender):
#     weight = 0
#     if gender == "남자":
#         weight = height * 0.01 * height * 0.01 * 22
#     elif gender == "여자":
#         weight = height * 0.01 * height * 0.01 * 21
#     return weight

# gender = "여자"
# height = 160
# weight = std_weight(height, gender)

# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# # Answer
# def std_weight (height, gender): # 키 m 단위 (실수), 성별 "남자" / "여자"
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 18134 # cm 단위
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2) # 소수점 2째 자리 까지 표시 
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# 위의 내 답처럼 weight 이라는 변수를 써서 돌려 받을 때는 소수점 2자리 까지만 나옴, round를 사용하지 않으면 계산된 대로 표시

# 표준 입출력 (8-1) (2:59:00)

# print("Python", "Java", "Javascript", sep=",", end="?") 
# # sep = separate - 각 문자열 구분할 때 (기본은 빈칸), end = 문장의 끝부분을 물음표로 바꿔 달라(기본은 줄바꿈)
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력으로 처리
# print("Python", "Java", file=sys.stderr) # 표준 에러 처리 - 필요하면 따로 에러 처리를 해서 코드를 수정할 수 있음

# 시험 성적 (출력 포맷)
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): # 사전 자료형의 key 와 value를 쌍으로 tuple로 보내 줌 - items 를 사용하면 key 와 value가 pair로 나옴
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # subject는 총 8칸의 공간을 확보한 상태에서 왼쪽으로 정렬을 하라는 의미, score는 4칸의 공간을 확보해서 오른쪽으로 정렬 

# 은행 대기 순번표
# 001, 002, 003, ...

# for num in range(1,21):
#     # print("대기번호: " + str(num))
#     print("대기번호: " + str(num).zfill(3)) # zfill - 3 만큼의 공간을 확보하고 값을 채워 넣는데, 값이 없는 부분은 0으로 채움

# answer = input("아무 값이나 입력하세요") # 사용자 입력을 통해서 값을 받게 되면 항상 문자열 형태로 저장이 된다. - 숫자를 입력해도 출력시 str로 감싸지 않아도 됨
# print(type(answer))
# print("입력하신 값은" + answer + "입니다.")

# 다양한 출력 포맷 (8-2) (3:10:12)

# # 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10 자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수 일땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸을 _로 채움
# print("{0:_<10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(1000000000000000))
# # 3자리 마다 콤마를 찍어주기, +-부호도 붙이기
# print("{0:+,}".format(100000000000000))
# print("{0:+,}".format(-100000000000000))
# # 3자리 마다 콤마를 찍어주기, +-부호도 붙이고, 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기
# print("{0:^<+30,}".format(100000000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시 (아래 같은 경우 소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))

# {숫자:채울문자|정렬방향|부호|자릿수|콤마추가}

# 파일 입출력 () (3:17:45)

# score_file = open("score.txt", "w", encoding="utf8") # utf8은 한글을 쓰기 위해 정의함
# print("수학: 0", file=score_file)
# print("영어: 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학: 80") 
# score_file.write("\n코딩: 100") #.write로 적을 떄는 줄바꿈이 따로 없어서 지정해 주어야 한다.
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") # 다음줄로 이동하지 않으려면 end를 사용
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()

# pickle () (3:26:26) - 프로그램 상에서 우리가 사용하고 있는 데이터를 파일 형태로 저장

# import pickle
# profile_file = open("profile.pickle", "wb") # pickle사용을 위해서는 항상 binary 타입을 정의해야 한다. 
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with () (3:30:25)

# import pickle

# with open("profile.pickle", "rb") as profile_file: 
#     print(pickle.load(profile_file)) # 열었던 파일에 대해 close할 필요 없이 with 문을 탈출 하면서 자동으로 종료

#일반적인 파일을 with를 이용해서 쓰고 읽음
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

# 퀴즈 #7 ()

# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - x 주차 주간보고 - 
# 부서:
# 이름:
# 업무 요약:

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.
# 조건: 파일 명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.

# for week in range(1,51):
#     with open("{0}주차.txt".format(week),"w", encoding="utf8") as report_file: # "w"가 있어서 다시 실행을해도 덮어 쓰기를 한다.
#         report_file.write(" - {0}주차 주간보고 - \n부서: \n이름: \n업무 요약:".format(week))

# Answer
# for i in range(1,51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write(" - {0}주차 주간보고 - ".format(i))
#         report_file.write("부서:")
#         report_file.write("이름:")
#         report_file.write("업무 요약:")

# 클래스 () (3:38:08) - 붕어빵 틀처럼 계속 찍어서 만들 수 있음 - 서로 연관이 있는 변수와 함수의 집합

# # 마린: 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린" #유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{0}유닛이 생성 되었습니다.".format(name))
# print("체력 {0}, 공격력{1}\n".format(hp,damage))

# # 탱크: 공격 유닛, 탱ㅋ크, 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0}유닛이 생성 되었습니다.".format(tank_name))
# print("체력 {0}, 공격력{1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0}유닛이 생성 되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력{1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0}: {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# 일반 유닛
# class Unit:
#     def __init__(self, name, hp, damage): 
#         self.name = name # 멤버 변수 초기화
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

# marine1 = Unit("마린", 40, 5) # 마린과 탱크는 Unit클래스의 instance라고 한다
# marine2 = Unit("마린", 40, 5) # self를 제외하고 동일한 갯수의 변수를 던져 줘야 한다.
# tank = Unit("탱크", 150, 35) # init함수에 정의된 변수를 똑같이 보내 주어야만 객체를 만들 수 있다.

# __init__ () (3:47:03) # 파이썬에서 쓰이는 생성자 - 객체가 만들어질 때 자동으로 만들어지는 부분

# 멤버 변수 () (3:48:30) - 클래스 내에 정의된 변수, 위의 예로 self.name, self.hp, self.damage 그 변수로 초기화, 연산 가능

# # 레이스: 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage)) # wraith1후에 '.'을 찍으면 쓸 수 있는 멤버 변수가 나타남 - 멤버 변수에 접근 가능

# # 마인드 컨트롤: 상대방 유닛을 내것으로 만드는 것 (빼앗음)
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True # 외부에서 객체의 변수를 추가 할당 해서 쓸 수 있음 - 단 wraith2에만 사용 가능 - 확장을 한 객체에만 적용 가능

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태 입니다.".format(waith2.name))

# 메소드 () (3:53:06) - 메소드 앞에는 항상 self를 적어 준다고 이해한다. "self.변수"를 통해서 자기 자신에게 접근한다. 
# "self.변수"는 Class 자기 자신에 있는 멤버 변수의 값을 쓰는 것
# 아래 attack과 damaged라는 메소드를 만든 예제 참고

# # 공격 유닛
# class AttackUnit:
#     def __init__(self, name, hp, damage): 
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))
    
#     def attack(self, location):
#         print("{0}: {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

# # 셀프는 자기 자신, 클래스 내에서 메소드 앞에는 항상 self를 무조건 적어 준다. self.xxx를 통해서 자기 자신의 변수에 접근 가능

#     def damaged(self, damage):
#         print("{0}: {1} 데이지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0:
#             print("{0}: 파괴되었습니다.".format(self.name))

# # # 파이어뱃: 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")

# # #공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# 상속 () (3:59:29) - 이미 정의된 클래스의 내용을 그대로 이용

# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp): 
#         self.name = name # 멤버 변수 초기화
#         self.hp = hp

# # 공격 유닛 - Unit이라는 클래스를 상속 받아서 AttackUnit이라는 클래스를 만듬 
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage): 
#         Unit.__init__(self, name, hp)
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0}: {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0}: {1} 데이지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0:
#             print("{0}: 파괴되었습니다.".format(self.name))

# # 메딕: 의무병

# # # 파이어뱃: 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# 다중 상속 () (4:02:53) - 여러곳에서 상속을 받음

# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp): 
#         self.name = name # 멤버 변수 초기화
#         self.hp = hp

# # 공격 유닛 - Unit이라는 클래스를 상속 받아서 AttackUnit이라는 클래스를 만듬 
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage): 
#         Unit.__init__(self, name, hp)
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0}: {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0}: {1} 데이지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <=0:
#             print("{0}: 파괴되었습니다.".format(self.name))

# # 드랍쉽: 공중 유닛, 수송기, 마린/파이어뱃/탱크 등을 수송. 공격 X

# #날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location):
#         print("{0}: {1} 방향으로 날아갑니다. [속도 {2}]"\
#             .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스 - AttackUnit과 Flyable 두 클래스를 상속 받아서 초기화를 해줌
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage) # 상속 받은 멤버 변수 초기화
#         Flyable.__init__(self, flying_speed) # 상속 받은 멤버 변수 초기화

# # 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# 연산자 오버로딩 () (4:10:08) - 자식 클래스에서 정의한 메소드를 쓰고 싶을 때, 메소드를 새롭게 정의해서 사용하는 것
# 상속하는 클래스에 변화(변수 추가)가 생기면 상속 받는 클래스의 변수에도 같이 추가를 해줘야 한다.

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): 
        self.name = name # 멤버 변수 초기화
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}: {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

# 공격 유닛 - Unit이라는 클래스를 상속 받아서 AttackUnit이라는 클래스를 만듬 
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): # Unit 클래스에 speed정보가 추가 되어 Unit을 사용하는 곳에도 Speed정보를 추가 해 주어야 한다.
        Unit.__init__(self, name, hp, speed) # 상속 받은 멤버 변수 초기화
        self.damage = damage
        
    def attack(self, location):
        print("{0}: {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0}: {1} 데이지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <=0:
            print("{0}: 파괴되었습니다.".format(self.name))

#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0}: {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스 - AttackUnit과 Flyable 두 클래스를 상속 받아서 초기화를 해줌
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 상속 받은 멤버 변수 초기화 - 지상 speed는 0으로 처리
        Flyable.__init__(self, flying_speed) # 상속 받은 멤버 변수 초기화

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌처: 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌처", 80, 10, 20)

# 배틀크루저: 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시") # 지상 유닛의 move 함수는 Unit 클래스 내의 move 함수
#battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시") # 공중 유닛으로 만들면(FlyableAttackUnit) Unit클래스의 move함수가 아닌, 재정의 된 FlyabltAttackUnit의 move함수가 호출 됨

# pass () (4:17:03)


