# 1018-banknotesAndCoins.py
# Problem: Banknotes and Coins
# Link: https://judge.beecrowd.com/en/problems/view/1021
# Solved on: 2024-08-18

# Wrong answer?? 

def banknotesAndCoins():
    change = int(float(input()) * 100)
    notes = [10000, 5000, 2000, 1000, 500, 200]
    coins = [100, 50, 25, 10, 5, 1]
    print('NOTAS:')
    for note in notes:
        amount = int(change // note)
        change = change % note
        print(f'{amount:} nota(s) de R$ {note // 100}.00')
    
    print('MOEDAS:')
    for coin in coins:
        amount = int(change // coin)
        change = change % coin
        print(f'{amount} moeda(s) de R$ {coin / 100:.2f}')

banknotesAndCoins()