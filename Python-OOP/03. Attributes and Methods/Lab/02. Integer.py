from math import floor


class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value: float):
        try:
            new_value = floor(value)
            return cls(new_value)
        except TypeError:
            return 'value is not a float'

    @classmethod
    def from_roman(cls, value):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(value)):
            if i > 0 and rom_val[value[i]] > rom_val[value[i - 1]]:
                int_val += rom_val[value[i]] - 2 * rom_val[value[i - 1]]
            else:
                int_val += rom_val[value[i]]
        return cls(int_val)

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):
            return 'wrong type'
        new_value = int(value)
        return cls(new_value)

    def add(self, other):
        if not isinstance(other, Integer):
            return 'number should be an Integer instance'
        return self.value + other.value


first_num = Integer(10)
second_num = Integer.from_roman("IV")

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))