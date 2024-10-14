# 2782-stepladder.py
# Problem: Stepladder
# Link: https://judge.beecrowd.com/en/problems/view/2782
# Solved on: 2024-10-14

def stepladder():
    steps = 0

    n = int(input())
    sequence = list(map(int, input().split()))
    if n == 1 or n == 2:
        print('1')
        return
    
    i = 1
    difference = sequence[1] - sequence[0]

    while i < n:
        if sequence[i] - sequence[i-1] != difference:
            difference = sequence[i] - sequence[i - 1]
            steps += 1
        i += 1

    steps += 1

    print(f'{steps}')

stepladder()
