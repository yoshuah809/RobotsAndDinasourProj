from robot import Robot

class Fleet():
    def __init__(self):
        self.robots = []

    def create_fleet(self, Robot):
        self.robots.append(Robot)
        #print(f'{Robot} was added to Fleet')

    

    