# Exercício - sistema de perguntas e respostas

import os
from time import sleep

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções' : ['1', '3', '4', '5'],
        'Resposta': '4'
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções' : ['25', '55', '10', '51'],
        'Resposta': '25'
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções' : ['4', '5', '2', '1'],
        'Resposta': '5'
    },
    {
        'Pergunta': 'O que se comemora no dia 25 de Dezembro?',
        'Opções' : ['Carnaval', 'Páscoa', 'Natal', 'Ano Novo'],
        'Resposta': 'Natal'
    },
    {
        'Pergunta': 'Qual a capital da França?',
        'Opções' : ['Londres', 'Madrid', 'Praga', 'Paris'],
        'Resposta': 'Paris'
    },
    {
        'Pergunta': 'Quantos estados o Brasil possui?',
        'Opções' : ['34', '26', '16', '28'],
        'Resposta': '26'
    },
    {
        'Pergunta': 'Quantas Champions League o Real Madrid possui?',
        'Opções' : ['14', '6', '9', '11'],
        'Resposta': '14'
    }
]

total_acertos = 0

for c in range (0, len(perguntas)):
    #Pergunta
    print('Pergunta:', perguntas[c]['Pergunta'])

    #Opções
    print('Opções:')
    for opcao, resposta in enumerate (perguntas[c]['Opções']):
        print(f'{opcao}) {resposta}')
    
    #Resposta Usuário
    resposta_usuario = int(input('Escolha uma opção: '))
    if resposta_usuario not in [0, 1, 2, 3]:
        while resposta_usuario not in [0, 1, 2, 3]:
            print('Opção inexistente, tente novamente!')
            resposta_usuario = int(input('Escolha uma opção: '))

    if perguntas[c]['Opções'][resposta_usuario] == perguntas[c]['Resposta']:
        print('Você acertou ^^')
        total_acertos += 1
    else:
        print('Você errou :/')
        print('A resposta correta é:', perguntas[c]['Resposta'])
    sleep(1.5)
    os.system('cls')
print('-------------- FIM DAS QUESTÕES --------------')
print(f'Sua nota: {total_acertos:.2f}/{len(perguntas):.2f}')
