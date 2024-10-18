# 2863-umilBolt.py
# Problem: Umil Bolt
# Link: https://judge.beecrowd.com/en/problems/view/2863
# Solved on: 2024-10-17

def umilBolt():
    while True:
        try:
            tests = int(input())
            bestTime = 0
            for _ in range(tests):
                time = float(input())
                if time < bestTime or bestTime == 0:
                    bestTime = time
                
            print(bestTime)

        except EOFError:
            break

umilBolt()
