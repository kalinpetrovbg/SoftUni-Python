from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
        except IndexError:
            return "Hardware does not exist"

        try:
            hardware.install(software)
            System._software.append(software)
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        software = LightSoftware(name, capacity_consumption, memory_consumption)

        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
        except IndexError:
            return "Hardware does not exist"

        try:
            hardware.install(software)
            System._software.append(software)
        except Exception:
            return "Software cannot be installed"

    @staticmethod
    def release_software_component(hardware_name, software_name):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_memory = sum([h.memory for h in System._hardware])
        total_capacity = sum([h.capacity for h in System._hardware])
        used_memory = sum([s.memory_consumption for s in System._software])
        used_capacity = sum([s.capacity_consumption for s in System._software])
        res = "System Analysis\n"
        res += f"Hardware Components: {len(System._hardware)}\n"
        res += f"Software Components: {len(System._software)}\n"
        res += f"Total Operational Memory: {int(used_memory)} / {int(total_memory)}\n"
        res += f"Total Capacity Taken: {int(used_capacity)} / {int(total_capacity)}"
        return res

    @staticmethod
    def system_split():
        res = ""

        for h in System._hardware:
            num_express = len([s for s in h.software_components if s.type == "Express"])
            num_light = len([s for s in h.software_components if s.type == "Light"])
            used_memory = sum([s.memory_consumption for s in h.software_components])
            used_capacity = sum([s.capacity_consumption for s in h.software_components])
            all_software = ', '.join([s.name for s in h.software_components])
            res += f"Hardware Component - {h.name}\n"
            res += f"Express Software Components: {num_express}\n"
            res += f"Light Software Components: {num_light}\n"
            res += f"Memory Usage: {int(used_memory)} / {int(h.memory)}\n"
            res += f"Capacity Usage: {int(used_capacity)} / {int(h.capacity)}\n"
            res += f"Type: {h.type}\n"
            if h.software_components:
                res += f"Software Components: {all_software}"
            else:
                res += f"Software Components: None"
        return res


