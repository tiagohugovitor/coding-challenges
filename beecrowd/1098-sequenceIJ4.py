# 1098-sequenceIJ4.js
# Problem: Sequence IJ 4
# Link: https://judge.beecrowd.com/en/problems/view/1098
# Solved on: 2024-08-20

def sequenceIJ4():
    i = 0.0
    while i <= 2.0:
        for j in range(1, 4):
            i_formatted = int(i) if i.is_integer() else i
            j_formatted = int(j + i) if (j + i).is_integer() else j + i
            print(f'I={i_formatted} J={j_formatted}')
        i = round(i + 0.2, 1)

sequenceIJ4()
