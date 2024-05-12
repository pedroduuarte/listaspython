"""
QUESTÃO 3: 
Faça um programa que armazene as idades e as alturas de 4 alunos. Seu programa deve
exibir quantos alunos com mais de 13 anos possuem uma altura inferior à altura média
dentre todos os alunos.
"""

age = []
high = []
contador_final = 0 
for i in range (4):
   age.append(int(input(f'Digite aqui a idade do aluno {i+1}: ')))
   high.append(float(input(f'Digite aqui a altura do aluno {i+1}: ')))  
high_media = sum(high)/ 4
for i in range (4): 
    if age[i] > 13 and high[i] < high_media: 
        contador_final += 1
print(f'A quantidade de alunos com idade superior à 13 e altura inferios à altura média é de: {contador_final} ALUNOS')