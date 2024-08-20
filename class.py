# .format, class 
import random

SS = "김성재"
PPL = "이현호 , 이현주"
CPL = "최민철 , 임준석"

# PPL과 CPL을 UPL로 묶음
UPL = f"{PPL}, {CPL}"

# SS와 UPL을 QA로 묶음
QA = ", ".join([SS, PPL, CPL])

print("SS {}, PPL {}, CPL {}".format(SS, PPL, CPL))
print("UPL {}".format(UPL))
print("QA {}".format(QA))


# f-string

fish = "회"
pig = "갈비"

print(f"내가 지금 먹고 싶은건 {fish}와 {pig}다.")

# random.choice 함수

# 모든 사람의 이름을 리스트로 결합
ss = "김성재"
ppl = ["이현호", "이현주"]
cpl = ["최민철", "임준석"]

# ss만 []로 묶은 이유는 ppl과 cpl은 list로 묶여있지만 ss는 혼자여서 그렇다.
all_names = [ss] + ppl + cpl

# 랜덤하게 사람의 이름을 선택
random_name = random.choice(all_names)

liquor = "술"
meat = "고기"

# 선택된 랜덤한 이름을 포함하여 출력
print(f"{random_name} 님을 위해 {liquor}과 {meat}를 대령하라.")

# Class
class QA:
    def __init__(self, name, lead, new0325):
        self.name = name
        self.lead = lead
        self.new0325 = new0325
    def say(self):
        print(f"QA 챕터의 인원은 {', '.join(self.name)}이고 챕터장은 {self.lead}지만, 나는 오버데어의 {self.new0325}다.")
QAC = QA(["김성재", "이현호", "이현주", "최민철", "임준석"], "김성재", "이현호") #name에 해당하는 인원들은 []리스트로 묶고, lead와 new0325에 해당하는 사람은 ""문자열로 묶었다.

QAC.say()


        
class Aespa:
    def __init__(self, name, members, songs):
        self.name = name
        self.members = members
        self.songs = songs
    def say(self):
        members_str = ", ".join(self.members)
        songs_str = ", ".join(self.songs)
        print(f'{self.name}의 멤버는 {members_str}이며 대표곡은 {songs_str}이다. 수수수 수퍼노바 노바 캔스탑 하이퍼 스텔라')
        
aespa = Aespa('에스파', ['카리나', '윈터', '닝닝', '지젤'], ['NextLevel', 'BlackMamba', 'SuperNova'])

aespa.say()

class Redvelvet:
    def __init__(self, name, members, favorite):
        self.name = name
        self.members = members
        self.favorite = favorite
    def say(self):
        members_str = ", ".join(self.members)
        print(f"{self.name}에는 {members_str}가 있는데 나의 최애는 {self.favorite}다.")
        
redvelvet = Redvelvet('레드벨벳', ['아이린', '슬기', '예리', '조이', '웬디'], "슬기")

redvelvet.say()

