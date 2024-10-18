# 2807-iccanobif.py
# Problem: Iccanobif
# Link: https://judge.beecrowd.com/en/problems/view/2807
# Solved on: 2024-10-17

def iccanobif():
    sequence = [1]

    size = int(input())

    if size >= 2:
        sequence.append(1)
    
    if size > 2:
        for i in range(2, size):
            sequence.append(sequence[i-1] + sequence[i-2])

    result = ' '.join(map(str, reversed(sequence)))

    print(result)

iccanobif()
