# 1837-preface.py
# Problem: Preface!
# Link: https://judge.beecrowd.com/en/problems/view/1837
# Solved on: 2024-08-26

def preface():
        dividend, divisor = map(int, input().split())
        quotient = dividend // divisor

        remainder = dividend - divisor * quotient

        if remainder < 0:
            if divisor > 0:
                quotient -= 1
            else:
                quotient += 1
            remainder = dividend - divisor * quotient

        print(f'{quotient} {remainder}')

preface()
