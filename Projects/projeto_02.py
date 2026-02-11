# Digitação de Notas por estudante

notas = []

for x in range(2):
    nome = input('Digite o NOME do aluno: ')
    nota = int(input('Digite a NOTA do aluno: '))
    resultado = [nome, nota]
    notas.append(resultado)
print('\n')

print('***Planilha de Notas***')
for n in notas:
    nome = n[0]
    nota = n[1]   
    print(f'Estudante: {nome} - Nota: {nota}')