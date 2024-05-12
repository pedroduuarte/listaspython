"""
QUESTÃO 6:
6. Faça um programa que leia uma data de nascimento no formato dd/mm/aaaa e
imprima a data com o mês escrito por extenso.
Exemplo:
Data = 20/02/1995
Resultado gerado pelo programa:
Você nasceu em 20 de fevereiro de 1995
"""

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 
         'Setembro', 'Outubro', 'Novembro', 'Dezembro']
data = input('Digite a sua data de nascimento(dd/mm/aaaa): ')
if len(data[:2]) != 2: 
    print('Você digitou um formato de data inválido')
elif len(data[3:5]) != 2:
    print('Você digitou um formato de data inválido')
elif len(data[6:10]) != 4: 
    print('Você digitou um formato de data inválido')
else: print(f'Você nasceu em {data[:2]} de {meses[int(data[3:5])-1]} de {data[6:10]}')