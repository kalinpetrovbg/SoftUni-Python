class PizzaDelivery:
    ordered = False

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient in self.ingredients.keys():
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity
        self.price += quantity * ingredient_price

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients.keys():
            return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
        if self.ingredients[ingredient] - quantity < 0:
            return f'Please check again the desired quantity of {ingredient}!'
        self.ingredients[ingredient] -= quantity
        self.price -= ingredient_price * quantity

    def make_order(self):
        PizzaDelivery.ordered = True
        return f"You've ordered pizza {self.name} prepared with " \
               f"{', '.join('{}: {}'.format(k, v) for k, v in self.ingredients.items())} and the price " \
               f"will be {self.price}lv."



margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
