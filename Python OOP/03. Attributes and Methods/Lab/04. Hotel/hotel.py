class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        pass

    def add_room(self, room):
        pass

    def take_room(self, room_number, people):
        pass

    def free_room(self, room_number):
        pass

    def print_status(self):
        result = f"Hotel {self.name} has {self.guests} total guests"
        # result += f"Free rooms:{}"
        # result += f"Taken rooms:{}"
        return result
