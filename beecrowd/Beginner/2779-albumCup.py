# 2779-albumCup.py
# Problem: Album of the Cup
# Link: https://judge.beecrowd.com/en/problems/view/2779
# Solved on: 2024-09-11

def albumCup():
    total = int(input())
    purchase = int(input())
    collection = set()
    for i in range(purchase):
        card = int(input())
        collection.add(card)

    print(total-len(collection))

albumCup()
