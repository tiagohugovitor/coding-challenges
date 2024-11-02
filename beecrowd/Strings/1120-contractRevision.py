# 1120-contractRevision.py
# Problem: Contract Revision
# Link: https://judge.beecrowd.com/en/problems/view/1120
# Solved on: 2024-11-01

def contractRevision():
    while True:
        defectedDigit, contractValue = input().split()
        
        if defectedDigit == '0' and contractValue == '0':
            break
        
        typedContractValue = ''
        for char in contractValue:
            if char != defectedDigit:
                typedContractValue += char

        if typedContractValue == '':
            typedContractValue = 0

        print(int(typedContractValue)) 

contractRevision()