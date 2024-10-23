# 3140-copyingPasting.py
# Problem: Copying and Pasting Code
# Link: https://judge.beecrowd.com/en/problems/view/3140
# Solved on: 2024-10-23

def copyingPasting():
    isPartOfBody = False
    while True:
        try:
            line = input()
            if line.strip() == '</body>':
                isPartOfBody = False
            if isPartOfBody:
                print(line)
            if line.strip() == '<body>':
                isPartOfBody = True

        except EOFError:
            break

copyingPasting()
