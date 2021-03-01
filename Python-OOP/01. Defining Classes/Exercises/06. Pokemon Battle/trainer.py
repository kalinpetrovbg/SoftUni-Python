class Trainer:
    def __init__(self, name: str, ):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon.name in [p.name for p in self.pokemon]:
            return f'This pokemon is already caught'
        self.pokemon.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str):
        if pokemon_name not in [pok.name for pok in self.pokemon]:
            return "Pokemon is not caught"
        to_remove = [pok for pok in self.pokemon if pok.name == pokemon_name][0]
        self.pokemon.remove(to_remove)
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        res = f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n'
        for x in self.pokemon:
           res += f'- {x.pokemon_details()}\n'
        return res