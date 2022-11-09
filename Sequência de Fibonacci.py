#============================================ DESAFIO 63 ============================================

#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros
#elementos de uma Sequência de Fibonacci

n = int(input('Digite quantos termos da Sequência de Fibonacci você quer ver: '))
proximo = 0
anterior = 0
c = 1
while c <= n:
    if proximo == 0:
        proximo += 1
    print(f'{proximo} -> ', end='')
    proximo += anterior
    anterior = proximo - anterior
    c += 1
print('FIM')


