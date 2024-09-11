# 3344-brute.py
# Problem: Brute
# Link: https://judge.beecrowd.com/en/problems/view/3344
# Solved on: 2024-09-03

def brute():
    n = int(input())
    numWords = {
        0: "ZERO",
        1: "ONE",
        2: "TWO",
        3: "THREE",
        4: "FOUR", 
        5: "FIVE",
        6: "SIX",
        7: "SEVEN",
        8: "EIGHT",
        9: "NINE", 
        10: "TEN",
        11: "ELEVEN",
        12: "TWELVE",
        13: "THIRTEEN", 
        14: "FOURTEEN",
        15: "FIFTEEN",
        16: "SIXTEEN", 
        17: "SEVENTEEN",
        18: "EIGHTEEN",
        19: "NINETEEN", 
        20: "TWENTY",
        30: "THIRTY", 
        40: "FORTY",
        50: "FIFTY", 
        60: "SIXTY",
        70: "SEVENTY",
        80: "EIGHTY",
        90: "NINETY",
        100: "ONE HUNDRED",
    }

    def transformNumberInWords(number):
        if number in numWords:
            return len(numWords[number])
        else:
            tens, ones = divmod(number, 10)
            return len(numWords[tens * 10]) + len(numWords[ones]) + 1

    current = n
    for _ in range(1000):
        current = transformNumberInWords(current)
    print(current)

brute()