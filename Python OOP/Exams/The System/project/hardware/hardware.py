class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.cur_capacity = capacity
        self.cur_memory = memory

    def install(self, software):
        if software.capacity_consumption <= self.cur_capacity and software.memory_consumption <= self.cur_memory:
            self.software_components.append(software)
            self.cur_capacity -= software.capacity_consumption
            self.cur_memory -= software.memory_consumption
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)
