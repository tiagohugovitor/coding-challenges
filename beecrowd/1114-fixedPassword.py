# 1114-fixedPassword.py
# Problem: Fixed Password
# Link: https://judge.beecrowd.com/en/problems/view/1114
# Solved on: 2024-08-21

def fixedPassword():
    incorrect = True
    while incorrect:
        password = int(input())
        if password == 2002:
            incorrect = False
        else:
            print('Senha Invalida')
    print('Acesso Permitido')

fixedPassword()
