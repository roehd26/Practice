
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

from random import * # random 라이브러리에서 모든 걸 사용한다.

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

python = "Python is Amazing"
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
print("나는 {}살 입니다." format(20))

