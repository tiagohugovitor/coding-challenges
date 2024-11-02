# 1024-encryption.py
# Problem: Encryption
# Link: https://judge.beecrowd.com/en/problems/view/1024
# Solved on: 2024-11-01

def encryption():
    tests= int(input())
    
    for _ in range(tests):
        decrypted = input()
        encrypted = ''
        
        for char in decrypted:
            if char.isalpha():
                encrypted += chr(ord(char) + 3)
            else:
                encrypted += char
        
        reversedEncrypted = encrypted[::-1]

        finalEncryption = ''
        middle = len(reversedEncrypted) // 2

        for index, char in enumerate(reversedEncrypted):
            if index >= middle:
                finalEncryption += chr(ord(char) - 1)
            else:
                finalEncryption += char

        print(finalEncryption)

encryption()