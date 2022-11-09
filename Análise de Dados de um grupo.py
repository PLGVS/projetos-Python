#============================================ DESAFIO 69 ============================================

#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada
#o programa deverá perguntar se o usuário quer continar ou não.No final, mostre:

#A) quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20 anos

idade = 0
sexo = ''
qtde_maiores_18 = 0
qtde_homens = 0
qtde_mulheres_mais_20anos = 0
opcao = ''

while True:
    print('--------------------\nCadastre uma pessoa\n--------------------')
    idade = int(input('Digite a idade: '))
    while sexo not in ['M', 'F']:
        sexo = str(input('Digite o sexo [M/F]: ')).upper()[0]

    if idade > 18:
        qtde_maiores_18 += 1
    if sexo == 'M':
        qtde_homens += 1
    if idade > 20 and sexo == 'F':
        qtde_mulheres_mais_20anos += 1

    while opcao not in ['S', 'N']:
        opcao = str(input('--------------------\nDeseja continuar cadastrando [S/N]? ')).upper()[0]
    if opcao == 'N':
        break
print('Fim do cadastro!\n')
print(f'Foram cadastradas:\n'
      f'{qtde_maiores_18} pessoas maiores de 18 anos\n'
      f'{qtde_homens} homens\n'
      f'{qtde_mulheres_mais_20anos} mulheres com mais de 20 anos.')
