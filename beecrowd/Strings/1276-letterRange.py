# 1276-letterRange.py
# Problem: Letter Range
# Link: https://judge.beecrowd.com/en/problems/view/1276
# Solved on: 2024-11-12

import sys
def letterRange():
    input_data = sys.stdin.read().strip().splitlines()
    data_index = 0

    while data_index < input_data:
        letters = input_data[data_index]
        data_index += 1

        if len(letters) == 0:
            print()
            continue
        start = letters[0]
        end = letters[0]
        
        for char in letters:



letterRange()