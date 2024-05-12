"""
QUESTÃO 7:
Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 - Janeiro, 2 - Fevereiro, . . . ).
"""

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temp = []
for i in meses: 
    temperatura = float(input(f'Digite a temperatura média  do mês {i}: '))
    temp.append(temperatura)
temp_media = sum(temp) / len(temp)
for i in range (len(temp)):
    if temp[i] > temp_media: 
        print(f'{meses[i]} - {temp[i]}')

