# 2879-montyHall.py
# Problem: Desvendando Monty Hall
# Link: https://judge.beecrowd.com/en/problems/view/2879
# Solved on: 2024-10-17

def montyHall():
        tests = int(input())
        loses = 0
        for _ in range(tests):
            carDoor = int(input())
            if carDoor == 1:
                  loses += 1
            
        print(tests - loses)

montyHall()
