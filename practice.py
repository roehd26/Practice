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

# if () (1:57:33)

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

# for () (2:05:11)

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

# while () (2:09:33)

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

# continue 와 break () (2:15:00)

# 수업중 순서대로 책을 읽고 있는데 2, 5번 학생이 결석인 경우
# absent = [2, 5] # 결석
# no_book = [7] # 책을 깜빡했음
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

# # range로 난수 생성시 자료 타입은 range -> list로 바꿔줘야 하고, randrange로 난수 생성시는 int형으로 바로 비교 연산 할 수 있음

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

# 함수 () (2:28:35)

# def open_account(): # 함수 정의 시에는 "def + 함수 이름() + :"
#     print("새로운 계좌가 생성 되었습니다.")

# # 함수는 정의만 해 두는 것으로 실제로 호출 하기 전까지는 실행 하지 않는다.

# open_account() # 함수 호출

# 전달값과 반환값 () (2:30:10)

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

# 기본값 () (2:37:50) # 기본값을 설정하는 방법

# def profile(name, age, main_lang):
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang)) # 역 슬래쉬(\)를 사용하면 두줄의 내용을 한줄로 이어 준다.

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# # 같은 학교 같은 학년 같은 반 같은 수업

# def profile(name, age=17, main_lang="파이썬"): # 함수가 호출 될때 값을 전달 받지 못하면 기본값을 사용한다.
#     print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang)) # 역 슬래쉬(\)를 사용하면 두줄의 내용을 한줄로 이어 준다.

# profile("유재석")
# profile("김태호")

# 키워드 값 () (2:41:32) 

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# #함수에서 전달 받는 매개변수의 값을 키워드를 이용해서 함수를 호출 해 주면, 그 키워드에 해당하는 값이 순서가 뒤섞여 있어도 잘 전달 됨
# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")

# 가변인자 (7-5) (2:43:05)

# # def profile(name, age, lang1, lang2, lang3, lang4, lang5):
# #     print("이름: {0} \t나이: {1} \t".format(name, age), end=" ")
# #     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름: {0} \t나이: {1} \t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "Python", "Java","C", "C++", "C#")
# profile("김태호", 20, "Kotlin", "Swift")

# 지역변수와 전역변수 (7-6) (2:48:00)

# gun = 10

# def checkpoint(Soldiers): #경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - Soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))

# def checkpoint_return(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))
#     return gun

# print("전체 총: {0}".format(gun))
# gun = checkpoint_return(gun, 2) # 2명이 경계 근무 나감
# print("남은 총: {0}".format(gun)) # 함수 내에서 전역 변수에 대해 변경이 있으면 함수 이후에도 그 값이 남아 있음

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

def std_weight (height, gender):
    weight = 0
    if gender == "남자":
        weight = height * 0.01 * height * 0.01 * 22
    elif gender == "여자":
        weight = height * 0.01 * height * 0.01 * 21
    return weight

gender = "여자"
height = 160
weight = std_weight(height, gender)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# Answer
def std_weight (height, gender): # 키 m 단위 (실수), 성별 "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2) # 소수점 2째 자리 까지 표시 
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# 위의 내 답처럼 weight 이라는 변수를 써서 돌려 받을 때는 소수점 2자리 까지만 나옴, 
# 아래 youtube의 정답처럼 계산식으로 바로 돌려 받을 경우는 소수점 3자리 까지 나옴 - round로 소수점 자리 표시

# 표준 입출력 (8-1) (2:59:00)


