# 3047-ageOfMonica.py
# Problem: The Age of Mrs. Monica
# Link: https://judge.beecrowd.com/en/problems/view/3047
# Solved on: 2024-10-21

def ageOfMonica():
    monica = int(input())
    firstSon = int(input())
    secondSon = int(input())
    thirdSon = monica - firstSon - secondSon

    print(max(firstSon, secondSon, thirdSon))

ageOfMonica()
