# 3302-correctAnswer.py
# Problem: Correct Answer
# Link: https://judge.beecrowd.com/en/problems/view/3302
# Solved on: 2024-09-03

def correctAnswer():
    while True:
        try:
            questions = int(input())
            for question in range(questions):
                answer = input()
                print(f'resposta {question + 1}: {answer}')
        
        except EOFError:
            break
    

correctAnswer()