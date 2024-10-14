# 2783-cupStickers.py
# Problem: Cup Stickers
# Link: https://judge.beecrowd.com/en/problems/view/2783
# Solved on: 2024-10-14

def cupStickers():
    n, c, m = map(int, input().split())
    cardsMissingList = list(map(int, input().split()))
    cardsPurchased = list(map(int, input().split()))

    cardsMissing = set()
    for card in cardsMissingList:
        cardsMissing.add(card)
    
    for card in cardsPurchased:
        cardsMissing.discard(card)

    print(f'{len(cardsMissing)}')

cupStickers()
