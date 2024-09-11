# 2061-closingTabs.py
# Problem: Closing Tabs
# Link: https://judge.beecrowd.com/en/problems/view/2060
# Solved on: 2024-08-29

def closingTabs():
    tabs, actions = map(int, input().split())

    for _ in range(actions):
        action = input()
        if action == 'fechou':
            tabs += 1
        else:
            tabs -= 1
    
    print(tabs)

closingTabs()
