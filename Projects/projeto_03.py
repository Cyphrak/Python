# Chat

import os

mensagens = []

nome = input('Digite seu nome: ')

while True:

    # Limpando terminal
    os.system('cls')

    # Organizando o Chat
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
    print('__________________________________')

    # Obtendo texto
    texto = input('mensagem: ')
    if texto == 'fim':
        break


    # Adicionando mensagem na lista
    mensagens.append({
        'nome': nome,
        'texto': texto,
    })

        
    