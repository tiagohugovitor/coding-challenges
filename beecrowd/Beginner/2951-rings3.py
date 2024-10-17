# 2951-rings3.py
# Problem: The Return of The King
# Link: https://judge.beecrowd.com/en/problems/view/2951
# Solved on: 2024-10-16

def rings3():
    runesSize, friendshipNeeded = map(int, input().split())
    runes = dict()
    for _ in range(runesSize):
        rune, value = input().split()
        runes[rune] = int(value)
    
    totalFriendship = 0
    
    runesRecitedSize = int(input())
    runesRecited = list(input().split())

    for rune in runesRecited:
        totalFriendship += runes[rune]
    
    message = 'You shall pass!' if totalFriendship >= friendshipNeeded else 'My precioooous'

    print(totalFriendship)
    print(message)

rings3()
