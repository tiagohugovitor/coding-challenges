# 2493-operatorGame.py
# Problem: Operator Game
# Link: https://judge.beecrowd.com/en/problems/view/2493
# Solved on: 2024-09-04

def operatorGame():
    while True:
        try:
            tests = int(input())
            operations = []
            for _ in range(tests):
                solution = []
                first, expression = input().split()
                second, answer = expression.split('=')
                first, second, answer = int(first), int(second), int(answer)
                if first + second == answer:
                    solution.append('+')
                if first - second == answer:
                    solution.append('-')
                if first * second == answer:
                    solution.append('*')
                operations.append(solution)
            losers = []
            for _ in range(tests):
                name, number, operator = input().split()
                number = int(number) - 1
                if (operator == 'I' and len(operations[number]) != 0) or (operator != 'I' and operator not in operations[number]):
                    losers.append(name)

            if len(losers) == tests:
                print('None Shall Pass!')
            
            elif len(losers) == 0:
                print('You Shall All Pass!')

            else:
                losers.sort()
                for i, loser in enumerate(losers):
                    print(loser, end='')
                    if i != len(losers) - 1:
                        print(' ', end='')
                print()

        except EOFError:
            break

operatorGame()
