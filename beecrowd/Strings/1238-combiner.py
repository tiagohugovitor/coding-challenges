# 1238-combiner.py
# Problem: Combiner
# Link: https://judge.beecrowd.com/en/problems/view/1238
# Solved on: 2024-11-03

def combiner():
    tests = int(input())

    for _ in range(tests):
        firstString, secondString = input().split()
        firstPointer = 0
        secondPointer = 0
        combinedString = ''
        
        while firstPointer < len(firstString) and secondPointer < len(secondString):
            if secondPointer < firstPointer:
                combinedString += secondString[secondPointer]
                secondPointer += 1
            else:
                combinedString += firstString[firstPointer]
                firstPointer += 1

        while firstPointer < len(firstString):
            combinedString += firstString[firstPointer]
            firstPointer += 1
        
        while secondPointer < len(secondString):
            combinedString += secondString[secondPointer]
            secondPointer += 1

        print(combinedString)

combiner()