# 2670-coffeeMachine.py
# Problem: Coffee Machine
# Link: https://judge.beecrowd.com/en/problems/view/2670
# Solved on: 2024-09-06

def coffeeMachine():
    time = [0] * 3
    for floor in range(3):
        employees = int(input())
        for i in range(3):
            time[i] += (employees * abs(floor - i) * 2)

    print(min(time))
coffeeMachine()
