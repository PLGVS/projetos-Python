#============================================ DESAFIO 45 ============================================

#Crie um programa que faça o computador jogar Jokenpô com você.

import random
#Variáveis
escolha = str(input('Escolha Pedra, Papel ou Tesoura: ')).title()
escolha_pc = ['Pedra', 'Papel', 'Tesoura']
escolhido_pc = random.choice(escolha_pc)

#Condições caso o usuário escolha Pedra
if escolha == 'Pedra' and escolhido_pc == 'Tesoura':
    print('PC: {}\nVocê: {}\nVocê venceu!!!'.format(escolhido_pc, escolha))
elif escolha == 'Pedra' and escolhido_pc == 'Papel':
    print('PC: {}\nVocê: {}\nVocê perdeu!!!'.format(escolhido_pc, escolha))
elif escolha == 'Pedra' and escolhido_pc == 'Pedra':
    print('PC: {}\nVocê: {}\nEmpate!!!'.format(escolhido_pc, escolha))

#Condições caso o usuário escolha Papel
if escolha == 'Papel' and escolhido_pc == 'Pedra':
    print('PC: {}\nVocê: {}\nVocê venceu!!!'.format(escolhido_pc, escolha))
elif escolha == 'Papel' and escolhido_pc == 'Tesoura':
    print('PC: {}\nVocê: {}\nVocê perdeu!!!'.format(escolhido_pc, escolha))
elif escolha == 'Papel' and escolhido_pc == 'Papel':
    print('PC: {}\nVocê: {}\nEmpate!!!'.format(escolhido_pc, escolha))

#Condições caso o usuário escolha Tesoura
if escolha == 'Tesoura' and escolhido_pc == 'Papel':
    print('PC: {}\nVocê: {}\nVocê venceu!!!'.format(escolhido_pc, escolha))
elif escolha == 'Tesoura' and escolhido_pc == 'Pedra':
    print('PC: {}\nVocê: {}\nVocê perdeu!!!'.format(escolhido_pc, escolha))
elif escolha == 'Tesoura' and escolhido_pc == 'Tesoura':
    print('PC: {}\nVocê: {}\nEmpate!!!'.format(escolhido_pc, escolha))

#Condição caso não escolha nenhuma
if escolha not in escolha_pc:
    print('Escolha inválida, tente novamente!!!')