# 3161-forgottenFruits.py
# Problem: The Forgotten Fruits
# Link: https://judge.beecrowd.com/en/problems/view/3161
# Solved on: 2024-10-23

def forgottenFruits():
    searchesAmount, fruitsAmount = map(int, input().split())
    searches = []
    fruits = []
    for _ in range(searchesAmount):
        searchFruit = input()
        searches.append(searchFruit.lower())
    
    for _ in range(fruitsAmount):
        savedFruit = input()
        fruits.append(savedFruit.lower())

    for search in searches:
        found = False
        for fruit in fruits:
            if search in fruit or search in ''.join(reversed(fruit)):
                print(f'Sheldon come a fruta {search}')
                found = True
                break
        if not found:
            print(f'Sheldon detesta a fruta {search}')

forgottenFruits()
