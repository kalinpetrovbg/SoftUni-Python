from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware


class System:
    _hardware = []
    _software = []
    total_hardware_memory = 0
    total_hardware_capacity = 0

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        new = PowerHardware(name, capacity, memory)
        System._hardware.append(new)
        System.total_hardware_memory += new.memory
        System.total_hardware_capacity += new.capacity

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        new = HeavyHardware(name, capacity, memory)
        System._hardware.append(new)
        System.total_hardware_memory += new.memory
        System.total_hardware_capacity += new.capacity

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        pass

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        pass

    @staticmethod
    def release_software_component(hardware_name, software_name):
        pass

    @staticmethod
    def analyze():
        res = []
        res.append("System Analysis")
        res.append(f"Hardware Components: {len(System._hardware)}")
        res.append(f"Software Components: {len(System._software)}")
        res.append(f"Total Operational Memory: / {System.total_hardware_memory:.0f}")
        res.append(f"Total Capacity Taken: / {System.total_hardware_capacity:.0f}")
        return "\n".join(res)

    @staticmethod
    def system_split():
        res = []
        for h in System._hardware:
            installed_express = [s for s in h.software_components if s.type == "Express"]
            installed_light = [s for s in h.software_components if s.type == "Light"]
            res.append(f"Hardware Component - {h.name}")
            res.append(f"Express Software Components: {len(installed_express)}")
            res.append(f"Light Software Components: {len(installed_light)}")
            res.append(f"Memory Usage: ")
            res.append(f"Capacity Usage: ")
            res.append(f"Type: {h.type}")
            names_software = "None"
            if len(System._software) > 0:
                names_software = ", ".join(System._software)
            res.append(f"Software Components: {names_software}")
        return "\n".join(res)
