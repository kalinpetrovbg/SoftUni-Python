class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.used_capacity = 0
        self.used_memory = 0

    def install(self, software):
        pass

    def uninstall(self, software):
        pass
