# 2862-insect.py
# Problem: Insect!
# Link: https://judge.beecrowd.com/en/problems/view/2862
# Solved on: 2024-10-15

def insect():
    tests = int(input())

    for _ in range(tests):
        power = int(input())
        if power > 8000:
            print("Mais de 8000!")
        else:
            print("Inseto!")

insect()
