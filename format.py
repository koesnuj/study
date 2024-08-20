# .format

SS = "김성재"
PPL = "이현호, 이현주"
CPL = "최민철, 임준석"

# PPL과 CPL을 UPL로 묶음
UPL = PPL + ", " + CPL

# SS와 UPL을 OVERDARE로 묶음
OVERDARE = SS + ", " + UPL

print("SS QA {}, PPL QA {}, CPL QA {}".format(SS, PPL, CPL))
print("UPL QA {}".format(UPL))
print("OVERDARE {}".format(OVERDARE))


# f-string

fish = "회"
pig = "갈비"

print(f"지금 먹고 싶은건 {fish}와 {pig}다.")
