class Robot():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = 10


    def attack(self, dinosaur):
        dinosaur.health -= self.weapon

    
    def __str__(self) -> str:
        str1 = F"{self.name}  Health - {self.health}"
        return str1