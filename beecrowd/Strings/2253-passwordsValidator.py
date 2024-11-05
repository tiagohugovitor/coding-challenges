# 2253-passwordsValidator.py
# Problem: Passwords Validator
# Link: https://judge.beecrowd.com/en/problems/view/2253
# Solved on: 2024-11-04

import re

def passwordsValidator():
    
    def isValidString(s):
        return bool(re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z0-9]{6,32}$', s))

    while True:
        try:
            password = input()

            if isValidString(password):
                print('Senha valida.')
            else:
                print('Senha invalida.')
            
        except EOFError:
            break

passwordsValidator()