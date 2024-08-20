# .format

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

# 각 변수에 이름을 저장
ss = "김성재"
ppl = ["이현호", "이현주"]
cpl = ["최민철", "임준석"]

# 모든 사람의 이름을 리스트로 결합
# ss만 []로 묶은 이유는 ppl과 cpl은 list로 묶여있지만 ss는 혼자여서 그렇다.
all_names = [ss] + ppl + cpl

# 랜덤하게 한 사람의 이름을 선택
random_name = random.choice(all_names)

fish = "회"
pig = "갈비"

# 선택된 랜덤한 이름을 포함하여 출력
print(f"{random_name}가 지금 먹고 싶은건 {fish}와 {pig}다.")