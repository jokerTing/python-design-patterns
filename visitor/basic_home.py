import random
import unittest

class Light(object):
    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        return random.choice(range(-1, 2))

    def is_online(self):
        return self.get_status != -1
    
    def boot_up(self):
        self.status = 0
    
    def update_status(self, person_1_home, person_2_home):
        if person_1_home:
            if person_2_home:
                self.status = 1
            else:
                self.status = 0
        elif person_2_home:
            self.status = 1
        else:
            self.status = 0

# 恒温器
class Thermostat(object):
    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        temp_range = [x for x in range(-10, 31)]
        temp_range.append(None)
        return random.choice(temp_range)
    
    def is_online(self):
        return self.get_status is not None
    
    def boot_up(self):
        pass
    
    def update_status(self, person_1_home, person_2_home):
        pass

# 温度调节器
class TemperatureRegulator(object):
    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        return random.choice(['headting', 'cooling', 'on', 'off', 'error'])

    def is_online(self):
        return self.get_status != 'error'
    
    def boot_up(self):
        self.status = 'on'
    
    def update_status(self, person_1_home, person_2_home):
        if person_1_home:
            if person_2_home:
                self.status = 'on'
            else:
                self.status = 'heating'
        elif person_2_home:
            self.status = 'cooling'
        else:
            self.status = 'off'

class DoorLock(object):
    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        return random.choice(range(-1, 2))
    
    def is_online(self):
        return self.get_status != -1
    
    def boot_up(self):
        pass

    def update_status(self, person_1_home, person_2_home):
        if person_1_home:
            self.status = 0
        elif person_2_home:
            self.status = 1
        else:
            self.status = 1

class CoffeeMachine(object):
    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        return random.choice(range(-1, 5))
    
    def is_online(self):
        return self.get_status != -1

    def boot_up(self):
        self.status = 1
    
    def update_status(self, person_1_home, person_2_home):
        if person_1_home:
            if person_2_home:
                self.status = 2
            else:
                self.status = 3
        elif person_2_home:
            self.status = 4
        else:
            self.status = 0

class Clock(object):
    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    def get_status(self):
        return "{}:{}".format(random.randrange(24), random.randrange(60))
    
    def is_online(self):
        return True

    def boot_up(self):
        self.status = "00:00"
    
    def update_status(self, person_1_home, person_2_home):
        if person_1_home:
            if person_2_home:
                pass
            else:
                self.status = "00:01"
        elif person_2_home:
            self.status = "20:22"
        else:
            pass

class HomeAutomationBootTests(unittest.TestCase):
    def setUp(self):
        self.thermostat = Thermostat("General Thermostat")
        self.thermal_regulator = TemperatureRegulator("Thermal Regulator")
        self.front_door_lock = DoorLock("Front Door Lock")
        self.coffee_machine = CoffeeMachine("Coffee Machine")
        self.bedroom_light = Light("Bedroom Light")
        self.system_clock = Clock("System Clock")
    
    def test_boot_thermostat_does_nothing_to_stat(self):
        state_before = self.thermostat.status
        self.thermostat.boot_up()
        self.assertEqual(state_before, self.thermostat.status)
    
    def test_boot_thermal_regulator_turns_it_on(self):
        self.thermal_regulator.boot_up()
        self.assertEqual(self.thermal_regulator.status, "on")
    
    def test_boot_front_door_lock_does_nothing_to_state(self):
        state_before = self.front_door_lock.status
        self.front_door_lock.boot_up()
        self.assertEqual(state_before, self.front_door_lock.status)
    
    def test_boot_coffee_machine_turns_it_on(self):
        self.coffee_machine.boot_up()
        self.assertEqual(self.coffee_machine.status, 1)
    
    def test_boot_light_turns_it_off(self):
        self.bedroom_light.boot_up()
        self.assertEqual(self.bedroom_light.status, 0)
    
    def test_boot_system_clock_zeros_it(self):
        self.system_clock.boot_up()
        self.assertEqual(self.system_clock.status, "00:00")

'''
def main():
    device_network = [
        Thermostat("General Thermostat"),
        TemperatureRegulator("Thermal Regulator"),
        DoorLock("Front Door Lock"),
        CoffeeMachine("Coffee Machine"),
        Light("Bedroom Light"),
        Light("Kitchen Light"),
        Clock("System Clock")
    ]
    for device in device_network:
        print("{} is online:\t {}".format(device.name, device.is_online()))
'''

if __name__ == "__main__":
    #main()
    unittest.main()