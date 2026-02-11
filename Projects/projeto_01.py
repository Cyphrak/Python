# Crie um script que peça para o usuário digitar o nome de 5 bebidas favoritas, armazenando esses nomes dentro de uma lista.
# Exiba na tela os elementos da lista em ordem alfabética, um por linha, usando o laço de repetição for.

bebidas = []

for i in range(5):
    bebida = input('digite uma bebida favorita: ')
    bebidas.append(bebida)

bebidas.sort()

print('\nBebidas favoritas:')
for bebida in bebidas:
    print(bebida)
    
