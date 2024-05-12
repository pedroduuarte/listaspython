"""
QUESTÃO 4: 
Modifique o programa da questão 3 para que o usuário indique a quantidade de alunos que
será utilizada no programa. Assim antes de começar a leitura de idades e alturas, o programa
deve solicitar ao usuário o quantitativo de alunos."""

age = []
high = []
contador_final = 0 
quantidade = int(input('Digite aqui a quantidade de alunos que serão entrevistados: '))
if quantidade <= 0: print('Você digitou uma quantidade inválida, programa encerrado!')
else:
    for i in range (quantidade):
            age.append(int(input(f'Digite aqui a idade do aluno {i+1}: ')))
            high.append(float(input(f'Digite aqui a altura do aluno {i+1}: ')))
high_media = sum(high) / quantidade 
for i in range (quantidade): 
    if age[i] > 13 and high[i] < high_media: 
        contador_final += 1
print(f'A quantidade de alunos com idade superior à 13 e altura inferios à altura média é de: {contador_final} ALUNOS')
