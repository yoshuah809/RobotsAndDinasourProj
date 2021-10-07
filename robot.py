from weapon import Weapon
import random


class Robot():
    def __init__(self, name, weapons):
        self.name = name
        self.health = 100
        self.weapon = None
        self.weapons = weapons
        self.assign_weapon()
        


    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power

    def assign_weapon(self):
        if self.weapons is None or len(self.weapons) == 0 :
            return
        rand_number = random.randint(0, len(self.weapons) -1)
        self.weapon =self.weapons[rand_number]
     
     
    def __str__(self) -> str:
        str1 = F"{self.name}  Health - {self.health}"
        return str1

    