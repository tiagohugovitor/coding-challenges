# 2813-avoidingRain.py
# Problem: Avoiding Rain
# Link: https://judge.beecrowd.com/en/problems/view/2813
# Solved on: 2024-10-30

def avoidingRain():
    days = int(input())
    houseUmbrellas = 0
    workUmbrellas = 0
    totalHouseUmbrellas = 0
    totalWorkUMbrellas = 0

    for _ in range(days):
        houseToWork, workToHouse = input().split()

        if houseToWork == 'chuva':
            if houseUmbrellas == 0:
                houseUmbrellas += 1
                totalHouseUmbrellas += 1
            houseUmbrellas -= 1
            workUmbrellas += 1

        if workToHouse == 'chuva':
            if workUmbrellas == 0:
                workUmbrellas += 1
                totalWorkUMbrellas += 1
            houseUmbrellas += 1
            workUmbrellas -= 1
    
    print(f'{totalHouseUmbrellas} {totalWorkUMbrellas}')
    

avoidingRain()
