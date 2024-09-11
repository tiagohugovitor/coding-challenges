# 2749-output3.py
# Problem: Output 3
# Link: https://judge.beecrowd.com/en/problems/view/2749
# Solved on: 2024-09-06

def output3():
    border = '-' * 39

    start = '|x = 35{:>31}|'.format('', '')
    empty = '|{:>37}|'.format('')
    middle = '|{:>15}x = 35{:>16}|'.format('', '')
    end = '|{:>31}x = 35|'.format('', '')

    print(border)
    print(start)
    print(empty)
    print(middle)
    print(empty)
    print(end)
    print(border)

output3()
