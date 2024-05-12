"""
QUESTÃO 8: 
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O
resultado do atleta será determinado pela média dos cinco valores restantes. Você
deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo
atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O
programa deve ser encerrado quando não for informado o nome do atleta.
"""

atletas_lista = []
while True:
    saltos_lista = [] 
    nome = input('Digite o nome do atleta: ')
    if nome == '': 
        break 
    for i in range(5): 
        saltos_lista.append(float(input(f'Digite a distância do {i+1} º salto: ')))
    atletas_lista.append([nome,saltos_lista])
saida_lista = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
for i in range (len(atletas_lista)): 
    print(f'Atleta: {atletas_lista[i][0]}')
    print()
    for c in range(len(atletas_lista[i][1])):
        print(f'{saida_lista[c]} Salto: {atletas_lista[i][1][c]} m')
    print()
    print('Resultado Final:')
    print(f'Atleta: {atletas_lista[i][0]}')
    print(f'Média dos saltos: {sum(atletas_lista[i][1])/5}')
    print()
    
