# 1581-internationalChat.py
# Problem: International Chat
# Link: https://judge.beecrowd.com/en/problems/view/1581
# Solved on: 2024-11-03

def internationalChat():
    tests = int(input())

    for _ in range(tests):
        groupSize = int(input())
        groupNationalities = []
        for _ in range(groupSize):
            nationality = input()
            groupNationalities.append(nationality)

        firstNationality = groupNationalities[0]
        sameNationality = True
        
        for index in range(1, groupSize):
            if groupNationalities[index] != firstNationality:
                sameNationality = False
                break
        
        if sameNationality:
            print(firstNationality)
        
        else:
            print('ingles')

internationalChat()