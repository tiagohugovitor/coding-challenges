# 2982-strikes.py
# Problem: The Strike Stops or Continues?
# Link: https://judge.beecrowd.com/en/problems/view/2982
# Solved on: 2024-10-16

def strikes():
    values = int(input())
    sum = 0
    for _ in range(values):
        identifier, value = input().split()
        if identifier == 'V':
            sum += int(value)
        else:
            sum -= int(value)
    
    if sum < 0:
        print('NAO VAI TER CORTE, VAI TER LUTA!')
    else:
        print('A greve vai parar.')

strikes()
