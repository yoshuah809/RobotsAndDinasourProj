from dinosaur import Dinosaur
from robot import Robot
from fleet import Fleet
from herd import Herd
from weapon import Weapon

class Battlefield ():

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.display_welcome()
    
    def run_game(self):

        Robocop = Robot("Robocop", Weapon.build_arsenal())
        Lancer = Robot("Lancer", Weapon.build_arsenal())
        Terminator = Robot("Terminator", Weapon.build_arsenal())
        
        self.fleet.create_fleet(Robocop)
        self.fleet.create_fleet(Lancer)
        self.fleet.create_fleet(Terminator)


        Raptor = Dinosaur("Raptor", 10)
        Triceraptor = Dinosaur("Triceraptor", 8)
        Oviraptor =Dinosaur("Oviraptor", 9)

        self.herd.create_herd(Raptor)
        self.herd.create_herd(Triceraptor)
        self.herd.create_herd(Oviraptor)

        running = True

        while running:
            pass

    def display_welcome(self):
        print("Welcome to The Robots and Dinosaurs Battlefield")
        option = int(input("Please Select 1 if you want to choose Robot or 2 for Dinosaur: "))
        if option == 1 or option == 2:
            print(f'You have Selected: %s' % option)
        else:
            self.display_welcome()
        return


    def display(self):
        pass

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_oponent_options(self):
        pass

    def show_robo_oponent_options(self):
        pass

    def display_winner(self):
        pass