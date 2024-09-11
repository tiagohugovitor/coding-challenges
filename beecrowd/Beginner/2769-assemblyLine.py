# 2769-assemblyLine.py
# Problem: Assembly Line
# Link: https://judge.beecrowd.com/en/problems/view/2769
# Solved on: 2024-09-10

def assemblyLine():
    while True:
        try:
            steps = int(input())
            e1, e2 = map(int, input().split())
            line1 = list(map(int, input().split()))
            line2 = list(map(int, input().split()))
            if steps != 1:
                transfer1 = list(map(int, input().split()))
                transfer2 = list(map(int, input().split()))

            x1, x2 = map(int, input().split())

            sum1 = [0] * steps
            sum2 = [0] * steps

            sum1[0] = e1 + line1[0]
            sum2[0] = e2 + line2[0]

            for i in range(1, steps):
                sum1[i] = min(sum1[i-1] + line1[i], sum2[i-1] + line1[i] + transfer2[i-1])
                sum2[i] = min(sum2[i-1] + line2[i], sum1[i-1] + line2[i] + transfer1[i-1])

            minCost = min(sum1[steps-1] + x1, sum2[steps-1] + x2)

            print(minCost)
            
        except EOFError:
            break

assemblyLine()
