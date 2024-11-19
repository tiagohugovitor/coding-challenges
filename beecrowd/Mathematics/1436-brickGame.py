# 1436-brickGame.py
# Problem: Brick Game
# Link: https://judge.beecrowd.com/en/problems/view/1436
# Solved on: 2024-11-19

# Insertion Sort is a good algorithm for only a few elements

def insertionSort(array):
    size = len(array)
    for i in range(1, size):
        j = i
        currentValue = array[j]
        while j > 0 and currentValue < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
            
        array[j] = currentValue
    

def brickGame():
    tests = int(input())
    
    for case in range(tests):
        players = list(map(int, input().split()))
        ages = players[1:]
        numberOfPlayers = players[0]
        
        insertionSort(ages)
        
        print(f'Case {case + 1}: {ages[numberOfPlayers // 2]}')

brickGame()
