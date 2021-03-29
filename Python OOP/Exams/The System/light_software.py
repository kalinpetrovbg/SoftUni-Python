from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, type='Light', capacity_consumption=capacity_consumption*2,
                         memory_consumption=memory_consumption/2)
