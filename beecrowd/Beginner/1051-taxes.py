# 1051-taxes.py
# Problem: Taxes
# Link: https://judge.beecrowd.com/en/problems/view/1051
# Solved on: 2024-08-19

def taxes():
    salary = float(input())
    
    taxesTable = [
        (3000, 18),
        (2000, 8),
    ]

    tax = max(0, salary - 4500) * 0.28
    salary -= max(0, salary - 4500)

    for boundary, percent in taxesTable:
        tax += (max(0, salary - boundary) * (percent/100))
        salary -= max(0, salary - boundary)

    result = f'R$ {tax:.2f}' if tax > 0 else 'Isento'
    print(f'{result}')

taxes()