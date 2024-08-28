# 1973-starTrek.py
# Problem: Start Trek
# Link: https://judge.beecrowd.com/en/problems/view/1973
# Solved on: 2024-08-27

def starTrek():
    farms = int(input())
    sheeps = list(map(int, input().split()))
    stolen = 0
    starsStolen = 0
    current = 0
    while current < farms and current >= 0:
        if sheeps[current] > 0:
            stolen += 1
            sheeps[current] -= 1
    
            if (sheeps[current] + 1) % 2 == 0:
                current -= 1
            else:
                starsStolen += 1
                current += 1
        else:
            current -= 1
            
    if current < 0:
        starsStolen += 1

    total = 0

    for farm in range(farms):
        total += sheeps[farm]

    print(f'{starsStolen} {total}')

starTrek()
