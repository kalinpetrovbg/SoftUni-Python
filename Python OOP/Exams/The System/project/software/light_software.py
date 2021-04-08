from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, type="Light", capacity_consumption=capacity_consumption*1.5, memory_consumption=memory_consumption*0.5)