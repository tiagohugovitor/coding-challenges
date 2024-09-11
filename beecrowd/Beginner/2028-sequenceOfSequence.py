# 2028-sequenceOfSequence.py
# Problem: Sequence of Sequence
# Link: https://judge.beecrowd.com/en/problems/view/2028
# Solved on: 2024-08-28

def sequenceOfSequence():
    cases = 0
    plural = 'numeros'
    singular = 'numero'
    while True:
        cases += 1
        try:
            size = int(input())
            amount = int((size * size + size)/ 2 + 1)
            print(f'Caso {cases}: {amount} {plural if amount > 1 else singular}')
            for i in range(size + 1):
                if i == 0:
                    print('0', end='')
                else:
                    for _ in range(i):
                        print(f' {i}', end='')
            print('\n')
        except EOFError:
            break

sequenceOfSequence()
