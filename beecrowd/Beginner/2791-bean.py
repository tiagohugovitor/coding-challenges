# 2791-bean.py
# Problem: Bean
# Link: https://judge.beecrowd.com/en/problems/view/2791
# Solved on: 2024-10-15

def bean():
    cups = list(map(int, input().split()))
    for i, cup in enumerate(cups):
        if cup == 1:
            print(i+ 1)
            return


bean()
