# 1048-salaryIncrease.py
# Problem: Salary Increase
# Link: https://judge.beecrowd.com/en/problems/view/1048
# Solved on: 2024-08-19

def salaryIncrease():
    salary = float(input())
    if salary <= 400:
        percent = 15
    elif salary <= 800:
        percent = 12
    elif salary <= 1200:
        percent = 10
    elif salary <= 2000:
        percent = 7
    else:
        percent = 4
    
    increase = salary * percent / 100
    newSalary = salary + increase

    print(f'Novo salario: {newSalary:.2f}')
    print(f'Reajuste ganho: {increase:.2f}')
    print(f'Em percentual: {percent} %')

salaryIncrease()