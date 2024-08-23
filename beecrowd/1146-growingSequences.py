# 1146-growingSequence.py
# Problem: Growing Sequence
# Link: https://judge.beecrowd.com/en/problems/view/1146
# Solved on: 2024-08-22

def growingSequence():

    while True:
        x = int(input())
        
        if x == 0:
            break

        for number in range(1, x + 1):
            print(f'{number}', end='')
            if number == x:
                print('\n', end='')
            else:
                print(' ', end='')


growingSequence()
