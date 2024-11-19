# 1212-primaryArithmetic.py
# Problem: Primary Arithmetic
# Link: https://judge.beecrowd.com/en/problems/view/1212
# Solved on: 2024-11-18

import sys

def primaryArithmetic():
    input_data = sys.stdin.read().splitlines()
    i = 0

    while(i < len(input_data) - 1):
        num1, num2 = map(int, input_data[i].split())
        i += 1

        carriesOperations = 0
        carry = 0
        
        while num2 > 0 or num1 > 0:
            sum = num1 % 10 + num2%10 + carry
            if sum >= 10:
                sum = sum % 10
                carriesOperations += 1
                carry = 1
            else:
                carry = 0
            num1 //= 10
            num2 //= 10
            
        
        if carriesOperations == 0:
            print('No carry operation.')
        else:
            print(f'{carriesOperations} carry {"operations" if carriesOperations > 1 else "operation"}.')
    
primaryArithmetic()
