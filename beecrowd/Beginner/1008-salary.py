# 1008-salary.py
# Problem: Salary
# Link: https://judge.beecrowd.com/en/problems/view/1008
# Solved on: 2024-08-18

def salary():
    number = int(input())
    hours = int(input())
    value = float(input())
    salary = (hours * value)
    print(f'NUMBER = {number}')
    print(f'SALARY = U$ {salary:.2f}')

salary()