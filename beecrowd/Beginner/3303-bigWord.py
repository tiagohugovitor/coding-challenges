# 3303-bigWord.py
# Problem: Big Word
# Link: https://judge.beecrowd.com/en/problems/view/3303
# Solved on: 2024-09-03

def bigWord():
    while True:
        try:
            word = input()
            if len(word) >= 10:
                print('palavrao')
            else:
                print('palavrinha')
        
        except EOFError:
            break
    

bigWord()