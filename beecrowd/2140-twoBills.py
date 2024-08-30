# 2140-twoBills.py
# Problem: Two Bills
# Link: https://judge.beecrowd.com/en/problems/view/2140
# Solved on: 2024-08-29

def twoBills():
    bills = [2, 5, 10, 20, 50, 100]
    while True:
        price, paid = map(int, input().split())

        if price == 0 and paid == 0:
            break

        change = paid - price
        possible = False
        for bill in bills:
            if change - bill in bills and change - bill != bill:
                possible = True
                break

        print(f"{'possible' if possible else 'impossible'}")

twoBills()
