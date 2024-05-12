"""
QUESTÃO 1: 
Faça um Programa que leia 5 números inteiros, armazene-os em uma lista e imprima essa
lista na tela.
"""

lista = []
for i in range (5):
    x = int(input('Digite um número: '))
    lista.append(x)
print(lista)