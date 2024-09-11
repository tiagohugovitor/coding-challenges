# 1958-scientificNotation.py
# Problem: Scientific Notation
# Link: https://judge.beecrowd.com/en/problems/view/1958
# Solved on: 2024-08-27

def scientificNotation():
    x = float(input().strip())
    
    result = f"{x:+.4E}"

    print(result)
scientificNotation()
