import random

# 기본 동물 클래스 정의
class ANIMAL():
    def __init__(self):
        pass  # 초기화 메서드, 여기서는 아무런 작업도 하지 않음

    def shit(self):
        print("shit shit shit")  # 'shit' 행동을 출력하는 메서드

# HUMAN 클래스는 ANIMAL 클래스를 상속받음
class HUMAN(ANIMAL):
    def __init__(self, name, age):
        self.name = name  # 사람의 이름을 저장
        self.age = age  # 사람의 나이를 저장
        pass  # 초기화 메서드, 여기서는 속성만 설정하고 있음

    def eat(self):
        print("eat eat eat!")  # 'eat' 행동을 출력하는 메서드

    def sleep(self):
        print("sleep sleep sleep!")  # 'sleep' 행동을 출력하는 메서드

# QA 클래스 정의
class QA:
    def __init__(self, name, age):
        self.name = name  # QA의 이름을 저장
        self.age = age  # QA의 나이를 저장
        pass  # 초기화 메서드, 여기서는 속성만 설정하고 있음

    # 주석 처리된 'eat' 메서드, 사용되지 않음
    # def eat(self):
    #     print("qa qa qa !")

    def report(self):
        print("{0} start {1} report".format(self.name, 1))  # QA의 보고를 시작하는 메서드
        pass

    def test(self):
        print("{} start test".format(self.name))  # QA의 테스트를 시작하는 메서드
        pass

# OVERDARE_QA 클래스는 HUMAN과 QA 클래스를 다중 상속받음
class OVERDARE_QA(HUMAN, QA):
    def __init__(a, name, age):
        a.name = name  # 이름을 설정
        a.age = age  # 나이를 설정
        pass  # 초기화 메서드, 여기서는 속성만 설정하고 있음

    def same(self, a):
        print("{} same".format(a))  # 'same'이라는 행동을 출력하는 메서드

    # 주석 처리된 'eat' 메서드, 사용되지 않음
    # def eat(self):
    #     print("overdare overdare overdare!!")
    #     pass

    def overshare(self):
        pass  # 'overshare' 메서드, 현재는 아무 작업도 하지 않음

# 간단한 포맷 문자열 출력 예제
a = "helloworld"

print("{} first {} {} second".format(1, 2, "3"))  # 포맷된 문자열 출력

# OVERDARE_QA 클래스의 'same' 메서드 호출
OVERDARE_QA.same("helloworld", 2)

# OVERDARE_QA 객체 생성 및 메서드 호출
sungjaekim = OVERDARE_QA("김성재", "37")
sungjaekim.eat()  # 'eat' 메서드 호출
sungjaekim.report()  # 'report' 메서드 호출
sungjaekim.test()  # 'test' 메서드 호출
sungjaekim.shit()  # 상속받은 'shit' 메서드 호출

# 다른 OVERDARE_QA 객체 생성 및 메서드 호출
lee = OVERDARE_QA("이현호", "33")
lee.eat()  # 'eat' 메서드 호출
lee.report()  # 'report' 메서드 호출
lee.test()  # 'test' 메서드 호출