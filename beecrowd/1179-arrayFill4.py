# 1179-arrayFill4.py
# Problem: Array Fill 4
# Link: https://judge.beecrowd.com/en/problems/view/1179
# Solved on: 2024-08-22

def arrayFill4():
    even = [0] * 5
    odd = [0] * 5
    evenPointer = 0
    oddPointer = 0

    def printArray(array, name, size):
        for i in range(size):
            print(f'{name}[{i}] = {array[i]}')

    for i in range(15):
        number = int(input())
        if number % 2 == 0:
            even[evenPointer] = number
            evenPointer += 1
            if evenPointer > 4:
                printArray(even, 'par', 5)
                evenPointer = 0
        else:
            odd[oddPointer] = number
            oddPointer += 1
            if oddPointer > 4:
                printArray(odd, 'impar', 5)
                oddPointer = 0

    printArray(odd, 'impar', oddPointer)
    printArray(even, 'par', evenPointer)

arrayFill4()