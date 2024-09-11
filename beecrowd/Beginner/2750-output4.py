# 2750-output4.py
# Problem: Output 4
# Link: https://judge.beecrowd.com/en/problems/view/2750
# Solved on: 2024-09-09

def output4():
    border = '-' * 39
    header = '|  decimal  |  octal  |  Hexadecimal  |'

    print(border)
    print(header)
    print(border)
    for i in range(16):
        print(f'|{str(i).rjust(7)}    |{oct(i)[2:].rjust(5)}    |{hex(i)[2:].upper().center(15)}|')
    print(border)

output4()
