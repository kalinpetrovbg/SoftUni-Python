class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)
            self.guests += room.guests

    def take_room(self, room_number, people):
        try:
            find_room = [r for r in self.rooms if r.number == room_number][0]
            if find_room.capacity >= people and find_room.is_taken == False:
                self.guests = people
                find_room.is_taken = True
        except IndexError:
            pass

    def free_room(self, room_number):
        try:
            to_remove = [r for r in self.rooms if room_number == r.number][0]
            self.rooms.remove(to_remove)
        except IndexError:
            pass

    def print_status(self):
        print(f"Hotel {self.name} has {self.guests} total guests")

        free_rooms = [r.number for r in self.rooms if r.is_taken == False]
        taken_rooms = [r.number for r in self.rooms if r.is_taken != False]

        print(f"Free rooms: {', '.join(str(x) for x in free_rooms)}")
        print(f"Taken rooms: {', '.join(str(x) for x in taken_rooms)}")
