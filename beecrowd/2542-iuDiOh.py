# 2542-iuDiOh.py
# Problem: Iu-Di-Oh!
# Link: https://judge.beecrowd.com/en/problems/view/2542
# Solved on: 2024-09-05

def iuDiOh():
    while True:
        try:
            n = int(input())
            marcosDeck, leonardoDeck = map(int, input().split())
            
            marcosCards = [0] * marcosDeck
            for i in range(marcosDeck):
                marcosCards[i] = list(map(int, input().split()))

            leonardoCards = [0] * leonardoDeck
            for i in range(leonardoDeck):
                leonardoCards[i] = list(map(int, input().split()))
            
            marcosChoice, leonardoChoice = map(int, input().split())
            attribute = int(input())

            marcosForce =  marcosCards[marcosChoice - 1][attribute - 1]
            leonardoForce = leonardoCards[leonardoChoice - 1][attribute - 1]

            if marcosForce == leonardoForce:
                print('Empate') 
            
            elif marcosForce > leonardoForce:
                print('Marcos')

            else:
                print('Leonardo')

        except EOFError:
            break

iuDiOh()
