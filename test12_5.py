"""
QUESTÃO 5: 
Modifique o programa da questão 3 para que o programa funcione para qualquer
quantidade de alunos. Assim, durante a leitura das idades e alturas o usuário poderá inserir
um valor negativo para indicar que deseja interromper a leitura dos dados.
"""

age = []
high = []
contador_final = 0 
contador_alunos = 0
while True: 
    age_students = (int(input(f'Digite aqui a idade do aluno {contador_alunos+1}: ')))
    if age_students < 0:
        print('você digitou um valor negativo, programa encerrado!')
        break 
    else: 
       age.append(age_students)
       high.append(float(input(f'Digite aqui a altura do aluno {contador_alunos+1}: ')))
       contador_alunos += 1 
high_media = sum(high) / len(high)
for i in range (len(age)): 
    if age[i] > 13 and high[i] < high_media: 
        contador_final += 1
print(f'A quantidade de alunos com idade superior à 13 e altura inferios à altura média é de: {contador_final} ALUNOS')
