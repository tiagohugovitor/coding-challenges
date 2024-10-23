# 3299-smallUnluckyNumbers.py
# Problem: Small Unlucky Numbers
# Link: https://judge.beecrowd.com/en/problems/view/3299
# Solved on: 2024-10-23

def smallUnluckyNumbers():
    number = input()
    unlucky = False

    for char in range(1, len(number)):
        if number[char] == '3' and number[char - 1] == '1':
            unlucky = True
            break
    if unlucky:
        print(f'{number} es de Mala Suerte')
    else:
        print(f'{number} NO es de Mala Suerte')

smallUnluckyNumbers()
