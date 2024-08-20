import random

class ANIMAL():
    def __init__(self):
        pass

    def shit(self):
        print("shit shit shit")

class HUMAN(ANIMAL):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def eat(self):
        print("eat eat eat!")

    def sleep(self):
        print("sleep sleep sleep!")

class QA:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    # def eat(self):
    #     print("qa qa qa !")

    def report(self):
        print("{0} start {1} report".format(self.name, 1))
        pass

    def test(self):
        print("{} start test".format(self.name))
        pass

class OVERDARE_QA(HUMAN, QA):
    def __init__(a, name, age):
        a.name = name
        a.age = age
        pass

    def same(self, a):
        print("{} same".format(a))

    # def eat(self):
    #     print("overdare overdare overdare!!")
    #     pass

    def overshare(self):
        pass

a = "helloworld"

print("{} first {} {} second".format(1, 2, "3"))


OVERDARE_QA.same("helloworld", 2)

sungjaekim = OVERDARE_QA("김성재", "37")
sungjaekim.eat()
sungjaekim.report()
sungjaekim.test()

sungjaekim.shit()

lee = OVERDARE_QA("이현호", "33")
lee.eat()
lee.report()
lee.test()
