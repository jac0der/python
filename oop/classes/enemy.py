class Enemy:
    
    # instance variable assigned to all objects 
    hp = 200

    name = 'battaw'

    # define and initialize atkl and atkh for each new object
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print("atk is", self.atkl)

    def getHp(self):
        print("Hp is", self.hp)

    def getName(self):
        return self.name

enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(75, 90)
enemy2.getAtk()
enemy2.getHp()

"""
    k is 40
    Hp is 200
    atk is 75
    Hp is 200
"""