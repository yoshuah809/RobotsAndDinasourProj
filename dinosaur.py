class Dinosaur():
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 0


    def attack(self, robot):
        pass    


    def __str__(self) -> str:
      return self.name