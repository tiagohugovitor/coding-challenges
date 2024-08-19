# 1009-salaryWithBonus.py
# Problem: Salary with Bonus
# Link: https://judge.beecrowd.com/en/problems/view/1009
# Solved on: 2024-08-18

def salaryWithBonus():
    name = input()
    salary = float(input())
    sells = float(input())
    salaryWithBonus = (sells * 0.15) + salary
    print(f'TOTAL = R$ {salaryWithBonus:.2f}')

salaryWithBonus()