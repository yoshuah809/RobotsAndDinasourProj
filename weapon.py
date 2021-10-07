class Weapon():
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
   
    @staticmethod
    def build_arsenal():
        return [ Weapon("M14", 25), 
                 Weapon("Fire Cracker", 20),
                 Weapon("Sword", 50)]



                
              