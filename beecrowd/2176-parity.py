# 2176-parity.py
# Problem: Parity
# Link: https://judge.beecrowd.com/en/problems/view/2176
# Solved on: 2024-09-02

def parity():
    string = input()
    activeBits = 0
    for char in string:
        if char == '1':
            activeBits += 1
    parityBit = 0 if activeBits % 2 == 0 else 1
    print(f'{string}{parityBit}') 

parity()
