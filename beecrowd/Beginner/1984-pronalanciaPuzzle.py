# 1984-pronalanciaPuzzle.py
# Problem: The Pronalancia Puzzle
# Link: https://judge.beecrowd.com/en/problems/view/1984
# Solved on: 2024-08-28

def pronalanciaPuzzle():
    number = list(str(int(input())))
    for char in range(len(number)//2):
        number[char], number[len(number) - 1 - char] = number[len(number) - 1 - char], number[char]

    number = ''.join(number)
    print(number)

pronalanciaPuzzle()
