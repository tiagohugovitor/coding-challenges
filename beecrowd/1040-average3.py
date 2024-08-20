# 1040-average3.py
# Problem: Average 3
# Link: https://judge.beecrowd.com/en/problems/view/1040
# Solved on: 2024-08-18

def average3():

    n1, n2, n3, n4 = map(float, input().split())
    average = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
    print(f'Media: {average:.1f}')
    if average >= 7.0:
        print('Aluno aprovado.')
    elif average < 5.0:
        print('Aluno reprovado.')
    else:
        print('Aluno em exame.')
        finalScore = float(input())
        average = (average + finalScore) / 2
        print(f'Nota do exame: {finalScore:.1f}')
        if average >= 5.0:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
        print(f'Media final: {average:.1f}')

average3()