from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, type="Heavy", capacity=capacity*2, memory=memory*0.75)