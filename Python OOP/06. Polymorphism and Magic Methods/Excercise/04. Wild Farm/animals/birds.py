from project.animals.animal import Bird


class Owl(Bird):
    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food):
        pass

class Hen(Bird):

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food):
        pass


owl = Owl("Pip", 10, 10)
print(owl)


owl = Owl("Pip", 10, 10)
print(owl)
