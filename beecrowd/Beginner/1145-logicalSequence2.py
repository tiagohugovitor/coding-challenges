# 1145-logicalSequence2.py
# Problem: Logical Sequence 2
# Link: https://judge.beecrowd.com/en/problems/view/1145
# Solved on: 2024-08-22

def logicalSequence2():
    x, y = map(int, input().split())

    count = 0
    for number in range(1, y + 1):
        count += 1
        print(f'{number}', end='')
        if count == x:
            count = 0
            print('\n', end='')
        else:
            print(' ', end='')


logicalSequence2()
