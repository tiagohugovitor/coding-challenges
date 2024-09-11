# 2756-output10.py
# Problem: Output 10
# Link: https://judge.beecrowd.com/en/problems/view/2756
# Solved on: 2024-09-09

def output10():
    a = '{:>7}A'
    b = '{:>6}B B'
    c = '{:>5}C{:>3}C'
    d = '{:>4}D{:>5}D'
    e = '{:>3}E{:>7}E'

    print(a.format(' '))
    print(b.format(' '))
    print(c.format('', ''))
    print(d.format('', ''))
    print(e.format('', ''))
    print(d.format('', ''))
    print(c.format('', ''))
    print(b.format(' '))
    print(a.format(' '))

output10()
