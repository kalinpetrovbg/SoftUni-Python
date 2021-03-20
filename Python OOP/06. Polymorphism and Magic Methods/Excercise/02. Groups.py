class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def full_name(self):
        return self.name + " " + self.surname

    def __add__(self, other):
        return self.full_name() + other.full_name()

class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = list(people)





p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

# first_group = Group('__VIP__', [p0, p1, p2])
# # second_group = Group('Special', [p3, p4])
# # third_group = first_group + second_group
#
# print(len(first_group))
# print(second_group)
# # print(third_group[0])
