class Aespa:
    def __init__(self, name, members, songs):
        self.name = name
        self.members = members
        self.songs = songs

    def music(self):
        members_str = ", ".join(self.members)
        songs_str = ", ".join(self.songs)
        print(f'{self.name}의 멤버는 {members_str}이며 \n대표곡은 {songs_str}이 있다. \n수수수 수퍼노바 노바 캔스탑 하이퍼 스텔라')

class Redvelvet:
    def __init__(self, name, members, favorite):
        self.name = name
        self.members = members
        self.favorite = favorite

    def like(self):
        members_str = ", ".join(self.members)
        print(f"{self.name}에는 {members_str}가 있는데 나의 최애는 {self.favorite}다.")

class sm(Aespa, Redvelvet):
    def __init__(self, name, members, songs, favorite):
        Aespa.__init__(self, name, members, songs)
        Redvelvet.__init__(self, name, members, favorite)

# 예제 사용
sm_group = sm('에스파', ['카리나', '윈터', '닝닝', '지젤'], ['NextLevel', 'BlackMamba', 'SuperNova'], "슬기")

sm_group.music()
print()
sm_group.like()
print()