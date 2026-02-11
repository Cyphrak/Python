import random

print('Gerar 5 número aleatórios entre 1 e 50: ')
for i in range(6):
    n = random.randint(1,50)
    print(f'Número gerado: {n}')
print('\n')    

valor = random.random()
print(f'Número aleatório gerado: {round(valor * 100, 2)}')
print('\n')

valor = random.uniform(1,100)
print(f'Número aleatório gerado: {round(valor, 4)}')
print('\n')

L = [1,2,3,4,5,6,7,8,9,10]
n = random.choice(L)
print(f'Número escolhido dentro da lista L: {n}')
s = random.sample(L, 3)
print(f'3 Números escolhidos dentro da lista L: {s}')
print('Lista original: ')
print(L)
print('Lista embaralhada: ')
e = random.shuffle(L)
print(L)