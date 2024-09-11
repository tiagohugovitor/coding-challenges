# 1933-convertingToHexadecimal.py
# Problem: Converting to Hexadecimal
# Link: https://judge.beecrowd.com/en/problems/view/1957
# Solved on: 2024-08-27

def convertingToHexadecimal():
    convertion = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }
    decimal = int(input())
    hexa = ''
    while decimal > 0:
        current = decimal % 16
        decimal = decimal // 16
        if current >=10:
            hexa = f'{convertion[current]}{hexa}'
        else:
            hexa = f'{current}{hexa}'
    print(hexa)
    
convertingToHexadecimal()
