# 1248-dietPlan.py
# Problem: Diet Plan
# Link: https://judge.beecrowd.com/en/problems/view/1248
# Solved on: 2024-11-05

def dietPlan():
    tests = int(input())

    for _ in range(tests):
        diet = list(input())
        breakfast = list(input())
        lunch = list(input())
        cheater = False

        for food in breakfast:
            if food not in diet:
                cheater = True
                break
            diet.remove(food)

        for food in lunch:
            if food not in diet or cheater:
                cheater = True
                break
            diet.remove(food)

        if cheater:
            print('CHEATER')
            continue
        
        diet.sort()

        print(''.join(diet))

dietPlan()