# 2235-walkingOnTime.py
# Problem: Walking on Time
# Link: https://judge.beecrowd.com/en/problems/view/2235
# Solved on: 2024-09-02

def walkingOnTime():
    possibilities = ['++-', '+-+', '+--', '-++', '-+-', '--+']
    c1, c2, c3 = map(int, input().split())

    if c1 == c2 or c1 == c3 or c2 == c3:
        print('S')
        return

    travel = 'N'
    for possibility in possibilities:
        s1 = +1 if possibility[0] == '+' else -1
        s2 = +1 if possibility[1] == '+' else -1
        s3 = +1 if possibility[2] == '+' else -1
        sum = c1 * s1 + c2 * s2 + c3 * s3
        if sum == 0:
            travel = 'S'
            break

    print(f'{travel}')


def walkingOnTimeOptimized():
    c1, c2, c3 = map(int, input().split())

    if c1 == c2 or c1 == c3 or c2 == c3:
        print('S')
        return

    distance = (c1 + c2 + c3) / 2
    
    if distance == c1 or distance == c2 or distance == c3:
        print('S')
        return

    print('N')

walkingOnTimeOptimized()
