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
        

class newjeans:
    def __init__(self, name, members, nationality):
        self.name = name
        self.members = members
        self.nationality = nationality
        
    def say(self):
        members_str = ", ".join(self.members)
        nationality_str = ", ".join(self.nationality)
        print(f"{self.name}는 뉴진스, 멤버는 {members_str}로 구성되어 있고,\n국적은 {nationality_str}이다.")

class kpop:
    def __init__(self, aespa_info, redvelvet_info, newjeans_info):
        # 제공된 정보를 사용하여 aespa와 Redvelvet 인스턴스를 생성
        self.aespa_group = aespa(*aespa_info)
        self.redvelvet_group = Redvelvet(*redvelvet_info)
        self.newjeans_group = newjeans(*newjeans_info)

    def introduce_aespa(self):
        self.aespa_group.say()

    def introduce_redvelvet(self):
        self.redvelvet_group.say()
        
    def introduce_newjeans(self):
        self.newjeans_group.say()


# 두 그룹에 대한 필요한 정보를 사용하여 SM 클래스의 인스턴스를 생성
group_info = kpop(
    aespa_info=('에스파', ['카리나', '윈터', '닝닝', '지젤'], ['NextLevel', 'BlackMamba', 'SuperNova']),
    redvelvet_info=('레드벨벳', ['아이린', '슬기', '예리', '조이', '웬디'], '슬기'),
    newjeans_info=('뉴진스', ['민지', '다니엘', '혜인', '하니', '혜린'], ['대한민국', '호주/대한민국', '대한민국', '대한민국', '호주/베트남', '대한민국'])
)

# 이제 두 그룹을 소개하는 메서드를 호출할 수 있습니다
group_info.introduce_aespa()
print()
group_info.introduce_redvelvet()
print()
group_info.introduce_newjeans()