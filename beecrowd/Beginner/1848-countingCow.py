# 1848-countingCow.py
# Problem: Counting Cow
# Link: https://judge.beecrowd.com/en/problems/view/1848
# Solved on: 2024-08-26

def countingCow():
    numbers = {
        '---': 0,
        '--*': 1,
        '-*-': 2,
        '-**': 3,
        '*--': 4,
        '*-*': 5,
        '**-': 6,
        '***': 7,
    }
    screams = 0
    sum = 0
    while screams < 3:
        action = input()
        if action == 'caw caw':
            print(sum)
            sum = 0
            screams += 1
        else:
            sum += numbers[action]

countingCow()
