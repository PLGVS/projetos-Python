#============================================ DESAFIO 58 ============================================

#Melhore o desafio 028 onde o computador vai pensar um número entre 0 e 10. Só que agora, o jogador
#vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer!

import random
c = 1
escolha_pc = random.randint(0, 10)
escolha = -1
tentativas = 0
print('---- Jogo da Advinhação V2.0 ----\n'
      'O PC pensou em um número entre 0 e 10, consegue advinhar qual foi?\n')
while c != 0:
    escolha = int(input('Escolha um número: '))
    if escolha != escolha_pc:
        print('Você errou, tente novamente!')
        tentativas += 1
    else:
        c = 0
        tentativas += 1
print('Parabéns, você acertou!! O número era {}!!!\n'
      'Foram necessárias {} tentativas!'.format(escolha_pc, tentativas))
