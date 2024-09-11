# 1827-squareArray4.py
# Problem: Brazil World Cup
# Link: https://judge.beecrowd.com/en/problems/view/1827
# Solved on: 2024-08-26

def squareArray4():
    while True:
        try:
            size = int(input())
            for i in range(size):
                for j in range(size):
                    value = 0
                    if i == j:
                        value = 2
                    if i + j == size - 1:
                        value = 3
                    if i >= size // 3 and j >= size // 3 and  j < size - size // 3 and i < size - size//3:
                        value = 1
                    if i == size // 2 and j == size // 2:
                        value = 4
                    print(value, end='')
                print()
            print()
        except EOFError:
            break
squareArray4()