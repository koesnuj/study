#.format, class 
SS = "김성재"
PPL = ["이현호", "이현주"]
CPL = ["최민철", "임준석"]

PPL_str = ", ".join(PPL)
CPL_str = ", ".join(CPL)

#PPL과 CPL을 UPL로 묶음
UPL = f"{PPL_str}, {CPL_str}"

#SS와 UPL을 QA로 묶음
QA = f"{SS}, {PPL[0]}와 {PPL[1]}, {CPL[0]}과 {CPL[1]}"

print("SS {}, PPL {}, CPL {}".format(SS, PPL_str, CPL_str))
print("UPL은 {}".format(UPL))
print("QA는 {}".format(QA))

print()

#f-string
fish = "회"
pig = "갈비"

print(f"내가 지금 먹고 싶은건 {fish}와 {pig}다.")
print()


#random.choice 함수
import random

ss = "김성재"
ppl = ["이현호", "이현주"] #모든 사람의 이름을 리스트로 결합
cpl = ["최민철", "임준석"]

#ss만 []로 묶은 이유는 ppl과 cpl은 list로 묶여있지만 ss는 혼자여서 그렇다.
all_names = [ss] + ppl + cpl

#랜덤하게 사람의 이름을 선택
random_name = random.choice(all_names)

liquor = "술"
meat = "고기"

#선택된 랜덤한 이름을 포함하여 출력
print(f"{random_name} 님을 위해 {liquor}과 {meat}를 대령하라.")
print()

#Class
class QA:
    def __init__(self, name, lead, new0325):
        self.name = name
        self.lead = lead
        self.new0325 = new0325
    def yell(self):
        print(f"QA 챕터의 인원은 {', '.join(self.name)}이고 챕터장은 {self.lead}지만, 나는 오버데어의 {self.new0325}다.")
QAC = QA(["김성재", "이현호", "이현주", "최민철", "임준석"], "김성재", "이현호") #name에 해당하는 인원들은 []리스트로 묶고, lead와 new0325에 해당하는 사람은 ""문자열로 묶었다.

QAC.yell()
print()
 
class Aespa:
    def __init__(self, name, members, songs):
        self.name = name
        self.members = members
        self.songs = songs
    def music(self):
        members_str = ", ".join(self.members)
        songs_str = ", ".join(self.songs)
        print(f'{self.name}의 멤버는 {members_str}이며 대표곡은 {songs_str}이다. 수수수 수퍼노바 노바 캔스탑 하이퍼 스텔라')
        
aespa = Aespa('에스파', ['카리나', '윈터', '닝닝', '지젤'], ['NextLevel', 'BlackMamba', 'SuperNova'])

aespa.music()
print()

class Redvelvet:
    def __init__(self, name, members, favorite):
        self.name = name
        self.members = members
        self.favorite = favorite
    def like(self):
        members_str = ", ".join(self.members)
        print(f"{self.name}에는 {members_str}가 있는데 나의 최애는 {self.favorite}다.")
        
redvelvet = Redvelvet('레드벨벳', ['아이린', '슬기', '예리', '조이', '웬디'], "슬기")

redvelvet.like()
print()
