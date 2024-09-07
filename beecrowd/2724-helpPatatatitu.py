# 2724-helpPatatatitu.py
# Problem: Help Patatatitu
# Link: https://judge.beecrowd.com/en/problems/view/2724
# Solved on: 2024-09-06

def isSubstring(substring, string):
    index = 0 

    while index < len(string):
        index = string.find(substring, index)
        
        if index == -1:
            break 

        nextIndex = index + len(substring)

        if nextIndex == len(string) or string[nextIndex].isupper():
            return True 

        index += len(substring)

    return False

def helpPatatatitu():
    tests = int(input())
    for t in range(tests):
        dangerousAmount = int(input())
        dangerous = [0] * dangerousAmount
        for i in range(dangerousAmount):
            dangerous[i] = input()
        experiments = int(input())
        for _ in range(experiments):
            formula = input()
            safe = True
            for component in dangerous:
                if isSubstring(component, formula):
                    safe = False
                    break
            if safe:
                print('Prossiga')
            else:
                print('Abortar')

        if t != tests - 1:
            print()

helpPatatatitu()
