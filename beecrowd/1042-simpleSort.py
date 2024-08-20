# 1042-simpleSort.py
# Problem: Simple Sort
# Link: https://judge.beecrowd.com/en/problems/view/1042
# Solved on: 2024-08-19

def simpleSort():

    unsorted = input().split()

    sorted = [0] * 3

    for i, element in enumerate(unsorted):
        sorted[i] = int(element)

    for i in range(1, len(sorted)):
        current = sorted[i]
        j = i - 1
        while j >= 0 and sorted[j] > current:
            sorted[j + 1] = sorted[j]
            j -= 1 
        sorted[j + 1] = current
        
    for element in sorted:
        print(element)

    print('')

    for element in unsorted:
        print(element)    

simpleSort()