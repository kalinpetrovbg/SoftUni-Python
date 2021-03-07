class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return f"This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        try:
            filtered = [p for p in self.pokemon if p.name == pokemon_name][0]
            self.pokemon.remove(filtered)
            return f"You have released {pokemon_name}"
        except IndexError:
            return "Pokemon is not caught"

    def trainer_data(self):
        res = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        for p in self.pokemon:
            res += f"- {p.pokemon_details()}\n"
        return res

