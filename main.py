from dinosaur import Dinosaur
from robot import Robot
from fleet import Fleet
from herd import Herd


Robocop = Robot("Robocop")
Lancer = Robot("Lancer")
Terminator = Robot("Terminator")

Raptor = Dinosaur("Raptor", 10)
Triceraptor = Dinosaur("Triceraptor", 8)
Oviraptor =Dinosaur("Oviraptor", 9)

fleet1 = Fleet()
herd1 = Herd()

fleet1.create_fleet(Robocop)
fleet1.create_fleet(Lancer)
fleet1.create_fleet(Terminator)

herd1.create_herd(Raptor)
herd1.create_herd(Triceraptor)
herd1.create_herd(Oviraptor)

for a in herd1.dinosaur:
    print(a)


for i in fleet1.robots:
    print (i)

fleet1.robots[0].attack(Raptor)
Robocop.attack(Triceraptor)

for a in herd1.dinosaur:
    print(a)
