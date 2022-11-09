#============================================ DESAFIO 68 ============================================

#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando
#o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou ao final
#do jogo.

import random
escolha_jogador = 0
escolha_pc = 0
s = 0
opcao = ''
vitorias = 0

print('------ PAR OU IMPAR ------')
while True:
    while opcao not in ['PAR', 'IMPAR']:
        opcao = str(input('PAR ou IMPAR? ')).upper()
    escolha_jogador = int(input('Escolha um número entre 0 e 10: '))
    escolha_pc = random.randint(0, 10)
    s = escolha_jogador + escolha_pc
    if ((opcao == 'PAR') and (s % 2 != 0)) or ((opcao == 'IMPAR') and (s % 2 == 0)):
        break
    print(f'Voce: {escolha_jogador}\nPC: {escolha_pc}\n{s} é {opcao}, você ganhou!')
    vitorias += 1
    opcao = ''
print(f'Você perdeu depois de {vitorias} vitória(s) seguidas!')