from prototype_1 import Prototype
from copy import deepcopy
'''
class Concrete(Prototype):
    def clone(self):
        return deepcopy(self)
'''
class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = "knight"

        file_name = "{}_{}.dat".format(self.unit_type, level)
        with open(file_name, 'r') as parameter_file:
            lines = parameter_file.read().split("\n")
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return "Type: {0}\n" \
                "Life: {1}\n" \
                "Speed: {2}\n" \
                "Attack Power: {3}\n" \
                "Attack Range: {4}\n" \
                "Weapon: {5}".format(
                    self.unit_type,
                    self.life,
                    self.speed,
                    self.attack_power,
                    self.attack_range,
                    self.weapon)

    def clone(self):
        return deepcopy(self)

class Archer(Prototype):
    def __init__(self, level):
        self.max_level = 2
        self.unit_type = "archer"
        self.level = level
        file_name = "{}_{}.dat".format(self.unit_type, level)
        with open(file_name, 'r') as parameter_file:
            lines = parameter_file.read().split("\n")
            self.name = "William"
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return "Type: {0}\n" \
            "Life: {1}\n" \
            "speed: {2}\n" \
            "attack_range: {3}\n" \
            "attack_power: {4}\n" \
            "weapon: {5}\n" \
            "name: {6}\n" \
            "level: {7}".format(
                self.unit_type,
                self.life, 
                self.attack_power, 
                self.attack_power, 
                self.attack_range, 
                self.weapon,
                self.name,
                self.level)

    def upgrade(self):
        level = self.level + 1
        if level <= self.max_level:
            self.level = level
            file_name = "{}_{}.dat".format(self.unit_type, level)
            with open(file_name, 'r') as parameter_file:
                lines = parameter_file.read().split("\n")
                self.name = "William"
                self.life = lines[0]
                self.speed = lines[1]
                self.attack_power = lines[2]
                self.attack_range = lines[3]
                self.weapon = lines[4]
        else:
            print(self.level)
            print("[MAX LEVEL already!!!]")

    def clone(self):
        return deepcopy(self)

class Barracks(object):
    def __init__(self):
        self.units = {
            "knight": {
                1: Knight(1),
                2: Knight(2),
            },
            "archer":{
                1:Archer(1),
                2:Archer(2),
            }
        }

    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()


if __name__ == "__main__":
    #print("begin")
    barrack = Barracks()
    knight1 = barrack.build_unit("knight", 1)
    Archer1 = barrack.build_unit("archer", 1)
    Archer1.upgrade()
    Archer2 = barrack.build_unit("archer", 2)
    Archer2.upgrade()
    print ("[knight1] {}".format(knight1))
    print ("[Archer1] {}".format(Archer1))
    print ("[Archer1 upgrade] {}".format(Archer1))
    print ("[Archer2] {}".format(Archer2))
    print ("[Archer2 upgrade] {}".format(Archer2))