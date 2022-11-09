#============================================ DESAFIO 67 ============================================

#Faça um desafio que mostre a tabuada de vários números, um de cada vez, para cada valor
#digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

n = 0
m = 1

while True:
    n = int(input('Escolha um número para saber a tabuada dele [Digite um número negativo para encerrar]: '))
    if n < 0:
        break
    while m <= 10:
        print(f'{n} x {m} = {n * m}')
        m += 1
    m = 1
print('Fim do programa!')
