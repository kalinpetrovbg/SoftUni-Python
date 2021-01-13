class Inventory:

    def __init__(self, __capacity):
        self.__capacity = __capacity
        self.items = []
        self.remaining = __capacity

    def add_item(self, item):
        if self.remaining > 0:
            self.items.append(item)
            self.remaining -= 1
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.remaining}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
