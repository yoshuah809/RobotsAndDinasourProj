class Robot():
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.weapon = None


    def attack(self, dinosaur):
        pass

    
    def __str__(self) -> str:
        return self.name