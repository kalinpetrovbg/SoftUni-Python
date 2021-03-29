from project.software.software import Software
from project.software.light_software import LightSoftware
from project.software.express_software import ExpressSoftware
from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware


class System:
    _hardware = []
    _software = []
    expr_software = len([s for s in _software if s.__class__.__name__ == ExpressSoftware])
    light_software = len([s for s in _software if s.__class__.__name__ == LightSoftware])

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        power = PowerHardware(name, capacity, memory)
        System._hardware.append(power)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        heavy = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        try:
            current_hardware = [h for h in System._hardware if h.name == hardware_name][0]
            express = ExpressSoftware(name, capacity_consumption, memory_consumption)
            try:
                Hardware.install(current_hardware, express)
                if True:
                    System._software.append(express)
            except:
                pass
        except:
            raise Exception("Hardware does not exist")

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        try:
            current_hardware = [h for h in System._hardware if h.name == hardware_name][0]
            light = LightSoftware(name, capacity_consumption, memory_consumption)
            try:
                Hardware.install(current_hardware, light)
                if True:
                    System._software.append(light)
            except:
                pass
        except:
            raise Exception("Hardware does not exist")

    @staticmethod
    def release_software_component(hardware_name, software_name):
        try:
            cur_hardware = [h for h in System._hardware if h.name == hardware_name][0]
            cur_software = [s for s in System._software if s.name == software_name][0]
            if cur_hardware and cur_software:
                Hardware.uninstall(cur_hardware, cur_software)
            else:
                return "Some of the components do not exist"
        except:
            pass

    @staticmethod
    def analyze():
        total_used_memory = sum([h.memory for h in System._hardware])
        total_used_capacity = sum([h.capacity for h in System._hardware])
        result = "System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        result += f"Total Operational Memory: {total_used_memory} / {total_used_memory}\n"
        result += f"Total Capacity Taken: {total_used_capacity} / {total_used_capacity}"
        return result

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            result += f"Hardware Component - {h.name}\n"
            result += f"Express Software Components: {System.expr_software}\n"
            result += f"Light Software Components: {System.light_software}\n"
            result += f"Memory Usage: to do\n"
            result += f"Capacity Usage: to do\n"
            result += f"{h.type}\n"
            if len(h.software_components) > 0:
                result += f"{', '.join(h.software_components.name)}"
            else:
                result += "None"
            return result