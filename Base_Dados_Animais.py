"""
Nesse projeto foi criado uma base de dados sobre animais utilizando a estrutura dict, ou dicionário, 
e utilizando uma função para realizar uma pesquisa dentro dessa base de dados informando 3 informações sobre o animal 
e sendo retornado o nome do animal pesquisado.

In this project, a database on animals was created using the dict structure, or dictionary,
and using a function to perform a search within this database informing 3 pieces of information about the animal
and the name of the searched animal being returned.
"""


def busca(*args):
    for tipo in args:
        #Vertebrado
        if tipo == 'vertebrado':
            for classe in args:
                #Classe Ave
                if classe == 'ave':
                    for alimentacao in args:
                        #Alimentação Onívora
                        if alimentacao == 'onivoro':
                            animal = 'pomba'
                        #Alimentação Carnívora
                        elif alimentacao == 'carnivoro':
                            animal = 'aguia'
                #Classe Mamífero
                elif classe == 'mamifero':
                    for alimentacao in args:
                        if alimentacao == 'onivoro':
                            animal = 'homem'
                        elif alimentacao == 'herbivoro':
                            animal = 'vaca'
        #Invertebrado                   
        elif tipo == 'invertebrado':
            for classe in args:
                #Classe Inseto
                if classe == 'inseto':
                    for alimentacao in args:
                        #Alimentação Hematófaga
                        if alimentacao == 'hematofago':
                            animal = 'pulga'
                        #Alimentação Herbivora
                        elif alimentacao == 'herbivoro':
                            animal = 'lagarta'
                #Classe Anelidio
                elif classe == 'anelidio':
                    for alimentacao in args:
                        #Alimentação Hematófaga
                        if alimentacao == 'hematofago':
                            animal = 'sanguessuga'
                        #Alimentação Onívara
                        elif alimentacao == 'onivoro':
                            animal = 'minhoca'

    return animal

vertebrado = {
    "classe": {
        "ave": {
            "alimentacao": {
                "onivoro": "pomba",
                "carnivoro": "aguia",
            },
        },
        "mamifero": {
            "alimentacao": {
                "onivoro": "homem",
                "herbivoro": "vaca",
            },
        },
    },
}

invertebrado = {
    "classe": {
        "inseto": {
            "alimentacao": {
                "hematofago": "pulga",
                "herbivoro": "lagarta",
            },
        },
        "anelideo": {
            "alimentacao": {
                "hematofago": "pulga",
                "onivoro": "minhoca",
            },
        },
    },
}

print('------------- Busca de Espécies -------------')
print('Por favor, diga 3 informações sobre o animal que deseja buscar:\n\
      Seu tipo, sua alimentação e sua classe')
A = str(input('Informação 1: ')).lower()
B = str(input('Informação 2: ')).lower()
C = str(input('Informação 3: ')).lower()

animal = busca(A, B, C)

for tipo in [A, B, C]:
    if tipo in ['vertebrado', 'invertebrado']:
        tipo_animal = tipo
for classe in [A, B, C]:
    if classe in ['inseto', 'anelidio', 'mamifero', 'ave']:
        classe_animal = classe
for alimentacao in [A, B, C]:
    if alimentacao in ['carnivoro', 'onivoro', 'herbivoro', 'hematofago']:
        alimentacao_animal = alimentacao
# procura = busca('invertebrados', 'inseto', 'herbivoro')

print(f'Você procurou um animal do tipo {tipo_animal.capitalize()}\n\
      da classe {classe_animal.capitalize()}\n\
      e de alimentação {alimentacao_animal.capitalize()}\n\
      Esse animal é um(a) {animal.capitalize()}')