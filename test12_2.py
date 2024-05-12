"""QUESTÃO 2:
Faça um programa que leia 10 números inteiros. Cada numero par deve ser armazenado em
uma lista de pares e cada impar tem que ser armazenado em uma lista de impares. Ao
término do programa imprima as duas listas.
"""

lista_pares = []
lista_impares = []
for i in range (0,10): 
    numero = int(input('Digite um número: '))
    if numero % 2 == 0: 
        lista_pares.append(numero)
    else: lista_impares.append(numero)
print(f'A lista dos números pares é: {lista_pares}')
print(f'A lista dos números ímpares é: {lista_impares}')