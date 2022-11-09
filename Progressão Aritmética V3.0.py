#============================================ DESAFIO 62 ============================================

#Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 termos.

p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = p
c = 1
t = 0
extras = 10
while extras != 0:
    t += extras
    while c <= t:
        print(f'{termo} -> ', end='')
        termo += r
        c += 1
    print('Pausa!')
    extras = int(input('Quantos termos extras você deseja ver? '))
print('Fim do programa!')
