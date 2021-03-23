class HDMI:
    def connect(self, other):
        return f"{self} is connected with {other}"

class Ethernet:
    def connect(self, other):
        return f"{self} is connected with {other}"

class ACDCPower:
    def connect(self, other):
        return f"{self} is connected with {other}"

class Television:
    def __init__(self):
        self.connect_hdmi = HDMI()
        self.connect_power = ACDCPower()

class DVDPlayer:
    def __init__(self):
        self.connect_hdmi = HDMI()
        self.connect_power = ACDCPower()

class GameConsole:
    def __init__(self):
        self.connect_ethernet = Ethernet()
        self.connect_hdmi = HDMI()
        self.connect_power = ACDCPower()

class Router:
    def __init__(self):
        self.connect_ethernet = Ethernet()
        self.connect_power = ACDCPower()

tv = Television()
DVD = DVDPlayer()

print(tv.connect_power.connect(DVD.connect_power))
