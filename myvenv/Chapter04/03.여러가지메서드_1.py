class Unit:
    """
    속성 : 이름, 체력, 방어막, 공격력
    클래스 속성 : 전체 유닛개수
    """
    count = 0
    def __init__(self, name, hp, shield, demage):
        self.name = name
        self.hp = hp
        self.shield = shield
        self.demage = demage
        Unit.count += 1
        print(f'{self.name}(이)가 생성되었습니다.')
    
    def __str__(self):
        return f'[{self.name}] 체력 : {self.hp} 방어막 : {self.shield} 공격력 : {self.demage}'

    # 인스턴스 메서드 (instance method)
    # 인스턴스 속성에 접근할수 있는 메서드
    def hit(self, demage):
        if demage >= self.shield:
            demage -= self.shield
            self.hp -= demage
            if self.hp < 0 :
                self.hp = 0
            self.shield = 0
        else:
            self.shield -= demage
    
    # 클래스 메서드 (class method)
    # 클래스 속성에 접근하는 메서드
    @classmethod
    def print_count(cls):
        print(f"생성된 유닛갯수: [{cls.count}]")
            

probe = Unit('프로브', 20,20, 5)
zealot = Unit('질럿', 100,60, 16)
dragoon = Unit('드라군', 100,80, 120)


probe.hit(16)
print(probe)
probe.hit(16)
print(probe)
probe.hit(16)
print(probe)

Unit.print_count()

print(dir(probe))