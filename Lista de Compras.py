"""
Faça uma lista de compras com listas. O usuário deve ter a possibilidade
de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros índices inexistentes na lista
"""
import os
lista = []
while True:
    print("Escolha uma das opções abaixo:\n"\
          "1 - Inserir um produto na lista\n"\
          "2 - Apagar um produto da lista\n"\
          "3 - Listar os produtos da lista")
    
    opcao = input(":")
    if opcao not in ['1', '2', '3']:
        while opcao not in ['1', '2', '3']:
            print("Opção inválida!")
            opcao = input("Escolha uma opção:")

    if opcao == '1':
        os.system('cls')
        produto = input("Qual produto deseja adicionar? ")
        lista.append(produto)

    elif opcao == '2':
        os.system('cls')
        indice = int(input("Qual o indice do produto que deseja apagar? "))
        try:
            del lista[indice]
        except:
            print("Indice inexistente!")

    elif opcao == '3':
        os.system('cls')
        print("Itens da lista:")
        for indice, item in enumerate(lista):
            print(indice, item)
