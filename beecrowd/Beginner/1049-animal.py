# 1049-animal.py
# Problem: Animal
# Link: https://judge.beecrowd.com/en/problems/view/1049
# Solved on: 2024-08-19

def animal():
    firstCharacteristic = input()
    secondCharacteristic = input()
    thirdCharacteristic = input()
    
    animals = {
        'vertebrado': {
            'ave': {
                'carnivoro': 'aguia',
                'onivoro': 'pomba',
            },
            'mamifero': {
                'herbivoro': 'vaca',
                'onivoro': 'homem',
            }
        },
        'invertebrado': {
            'inseto': {
                'hematofago': 'pulga',
                'herbivoro': 'lagarta',
            },
            'anelideo': {
                'hematofago': 'sanguessuga',
                'onivoro': 'minhoca',
            }
        }
    }

    result = animals[firstCharacteristic][secondCharacteristic][thirdCharacteristic]

    print(f'{result}')

animal()