# 2146-password.py
# Problem: Password
# Link: https://judge.beecrowd.com/en/problems/view/2146
# Solved on: 2024-08-29

def password():
    while True:
        try:
            tip = int(input())

            print(f'{tip - 1}')
        except EOFError:
            break
password()
