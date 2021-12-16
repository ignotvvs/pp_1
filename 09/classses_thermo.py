import random

class thermo():
    def __init__(self):
        self.state = False
        self.temperature = 0

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False

    def measure(self):
        self.temperature = round(random.uniform(34.0,42.0),1)

    def display(self):
        if self.state:
            if self.temperature >= 41:
                print(f"Temperature: {self.temperature} CRITICAL TEMPERATURE!!")
            elif self.temperature >= 37.0:
                print(f"Temperature: {self.temperature} (fever)")
            else:
                print(f"Temperature: {self.temperature}")

t1 = thermo()
t1.turn_on()
t1.measure()
t1.display()
t1.turn_off()