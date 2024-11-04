# 2174-pokemonCollection.py
# Problem: Pokemon Collection
# Link: https://judge.beecrowd.com/en/problems/view/2174
# Solved on: 2024-11-03

def pokemonCollection():
    pokemons = int(input())

    collection = set()
    for _ in range(pokemons):
        pokemon = input()
        collection.add(pokemon)
        
    print(f'Falta(m) {151 - len(collection)} pomekon(s).')

pokemonCollection()