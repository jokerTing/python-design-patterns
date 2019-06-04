class Barracks(object):
    '''
    def generate_knight(self):
        #print("generate_knight")
        return Knight(400, 5, 3, 1, "short sword")

    def generate_archer(self):
        #print("generate_knight")
        return Archer(200, 7, 1, 3, "short bow")
    '''
    def generate_unit(self, unit_type, level):
        if unit_type == "knight":
            return Knight(level)
        elif unit_type == "archer":
            return Archer(level)


class Knight(object):
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
            "speed {2}\n" \
            "attack_range {3}\n" \
            "attack_power {4}\n" \
            "weapon {5}".format(
                self.unit_type,
                self.life, 
                self.attack_power, 
                self.attack_power, 
                self.attack_range, 
                self.weapon)

class Archer(object):
    def __init__(self, level):
        self.unit_type = "archer"
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
            "speed {2}\n" \
            "attack_range {3}\n" \
            "attack_power {4}\n" \
            "weapon {5}".format(
                self.unit_type,
                self.life, 
                self.attack_power, 
                self.attack_power, 
                self.attack_range, 
                self.weapon)

if __name__ == "__main__":
    #print("begin")
    barrack = Barracks()
    knight1 = barrack.generate_unit("knight", 1)
    Archer1 = barrack.generate_unit("archer", 2)
    print ("[knight1] {}".format(knight1))
    print ("[Archer1] {}".format(Archer1))