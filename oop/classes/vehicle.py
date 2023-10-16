class Vehicle:

    # define instance variables for objects
    speed = 0
    cost = 0

    # define constructor
    def __init__(self, make, model):
        self.mk = make
        self.mdl = model

    # define instance  methods for objects
    def getMake(self):
        print(self.mk)

    def getModel(self):
        print(self.mdl)

    def getSpeed(self):
        print(self.speed)

    def getCost(self):
        print(self.cost)


car1 = Vehicle('toyota', 'corolla-cross')
car1.getMake()
car1.getModel()
car1.speed = '220 km'
car1.cost = 6000000
car1.getSpeed()
car1.getCost()

print('\n')

car2 = Vehicle('mitsubishi', 'lancer')
car2.getMake()
car2.getModel()
car2.speed = '220 km'
car2.cost = 3000000
car2.getSpeed()
car2.getCost()