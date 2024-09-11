# 1094-experiments.py
# Problem: Experiments
# Link: https://judge.beecrowd.com/en/problems/view/1094
# Solved on: 2024-08-20

def experiments():
    frogs = 0
    rabits = 0
    rats = 0
    
    testCases = int(input())
    for _ in range(0, testCases):
        value, animal = input().split()
        if animal == 'C':
            rabits += int(value)
        if animal == 'R':
            rats += int(value)
        if animal == 'S':
            frogs += int(value)
        
    total = frogs + rabits + rats
    frogsPercentage = frogs * 100 / total 
    rabitsPercentage = rabits * 100 / total
    ratsPercentage = rats * 100 / total

    print(f'Total: {total} cobaias')
    print(f'Total de coelhos: {rabits}')
    print(f'Total de ratos: {rats}')
    print(f'Total de sapos: {frogs}')
    print(f'Percentual de coelhos: {rabitsPercentage:.2f} %')
    print(f'Percentual de ratos: {ratsPercentage:.2f} %')
    print(f'Percentual de sapos: {frogsPercentage:.2f} %')

experiments()