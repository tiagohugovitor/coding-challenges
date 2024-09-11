# 2502-decipheringCard.py
# Problem: Deciphering the Encrypted Card
# Link: https://judge.beecrowd.com/en/problems/view/2502
# Solved on: 2024-09-04

def decipheringCard():
    def decipher(cipher1, cipher2, char):
        isUpper = char.isupper()
        char = char.lower()  
        if char in cipher1:
            index = cipher1.index(char)
            return cipher2[index].upper() if isUpper else cipher2[index]
        if char in cipher2:
            index = cipher2.index(char)
            return cipher1[index].upper() if isUpper else cipher1[index]
        return char.upper() if isUpper else char
    
    while True:
        try:
            _, texts = map(int, input().split())
            cipher1 = input().lower()
            cipher2 = input().lower()
            for _ in range(texts):
                ciphered = input()
                deciphered = ''.join(decipher(cipher1, cipher2, char) for char in ciphered) 
                print(deciphered)
            print()
        except EOFError:
            break
decipheringCard()
