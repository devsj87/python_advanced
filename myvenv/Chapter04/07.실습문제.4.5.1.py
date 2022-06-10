# 실습문제 4.5.1
# Player 클래스를 구현해 보자.
# 1) 속성 : 닉네임, 미네랄, 가스, 유닛리스트 [프로브, 프로브, 질럿]

class Player:

    unit_list = []

    def __init__(self, nickname, mineral, gas):
        self.nickname = nickname
        self.mineral = mineral
        self.gas = gas

    def product(self, unit):
        if self.mineral < unit.mineral:
            print("미네랄이 부족합니다.")
        elif self.gas < unit.gas:
            print("가스가 부족합니다.")
        else:
            Player.unit_list.append(unit.name)
            print(f"[{unit.name}] 생산을 시작합니다.")

class Probe:
    name = "프로브"
    mineral  = 50
    gas = 0
    hp = 20
    shield = 20
    demage = 5

    def __init__(self):
        pass
    

class Zealot:
    name = "질럿"
    mineral  = 100
    gas = 0
    hp = 100
    shield = 60
    demage = 16

    def __init__(self):
        pass

class Dragon:
    name = "드라군"
    mineral  = 125
    gas = 50
    hp = 100
    shield = 80
    demage = 20

    def __init__(self):
        pass
   

player = Player("Bisu", 500, 200)

player.product(Zealot())
player.product(Dragon())
print(player.unit_list)


