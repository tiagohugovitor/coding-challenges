# 1962-longLongTimeAgo.py
# Problem: A long, long time ago
# Link: https://judge.beecrowd.com/en/problems/view/1962
# Solved on: 2024-08-27

def longLongTimeAgo():
    tests = int(input())

    for _ in range(tests):
        time = int(input())
        year = 2015 - time
        answer = f'{year} D.C.' if year > 0 else f'{abs(year) + 1} A.C.'
        print(answer)

longLongTimeAgo()
