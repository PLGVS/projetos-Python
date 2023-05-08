#------------------------------ Gerador de CPF------------------------------

import random
nove_digitos = ''

# Gerando os 9 primeiros digitos do CPF

for i in range (9):
    num_gerados = random.randint(0, 9)
    nove_digitos += str(num_gerados)
 
# Gerando o primeiro digito do CPF

soma = 0
multiplicador = 10

for numero in nove_digitos:
    soma += int(numero) * multiplicador
    multiplicador -= 1
soma_mult = soma * 10
resto_div_soma_mult = soma_mult % 11

if resto_div_soma_mult > 9:
    digito_1 = 0
else:
    digito_1 = resto_div_soma_mult

# Gerando o segundo digito do CPF

soma = 0
multiplicador = 11
for numero in (nove_digitos + str(digito_1)):
    soma += int(numero) * multiplicador
    multiplicador -= 1
soma_mult = soma * 10
resto_div_soma_mult = soma_mult % 11

if resto_div_soma_mult > 9:
    digito_2 = 0
else:
    digito_2 = resto_div_soma_mult

cpf_gerado = nove_digitos[0:3] + \
             '.' + nove_digitos[3:6] + \
             '.' + nove_digitos[6:9] + \
             '-' + str(digito_1) + str(digito_2)

print(f"O CPF gerado é {cpf_gerado}")