class aespa:
    def __init__(self, name, members, songs):
        self.name = name
        self.members = members
        self.songs = songs

    def say(self):
        members_str = ", ".join(self.members)
        songs_str = ", ".join(self.songs)
        print(f'{self.name}의 멤버는 {members_str}이며 \n대표곡은 {songs_str}등이 있다. \n수수수 수퍼노바 노바 캔스탑 하이퍼 스텔라')


class Redvelvet:
    def __init__(self, name, members, favorite):
        self.name = name
        self.members = members
        self.favorite = favorite

    def say(self):
        members_str = ", ".join(self.members)
        print(f"{self.name}에는 {members_str}가 있는데 나의 최애는 {self.favorite}다.")


class SM:
    def __init__(self, aespa_info, redvelvet_info):
        # 제공된 정보를 사용하여 aespa와 Redvelvet 인스턴스를 생성
        self.aespa_group = aespa(*aespa_info)
        self.redvelvet_group = Redvelvet(*redvelvet_info)

    def introduce_aespa(self):
        self.aespa_group.say()

    def introduce_redvelvet(self):
        self.redvelvet_group.say()


# 두 그룹에 대한 필요한 정보를 사용하여 SM 클래스의 인스턴스를 생성
sm_entertainment = SM(
    aespa_info=('에스파', ['카리나', '윈터', '닝닝', '지젤'], ['NextLevel', 'BlackMamba', 'SuperNova']),
    redvelvet_info=('레드벨벳', ['아이린', '슬기', '예리', '조이', '웬디'], '슬기')
)

# 이제 두 그룹을 소개하는 메서드를 호출할 수 있습니다
sm_entertainment.introduce_aespa()
print()
sm_entertainment.introduce_redvelvet()