from random import randint
from time import sleep

while True:
    
    # Itens do jogo
    itens = ("Pedra", "Papel", "Tesoura")

    # Definindo jogadas do jogador e computador
    computador = randint(0,2)
    print('''Suas Opções:
          [0] PEDRA
          [1] PAPEL
          [2] TESOURA''')
    jogador = int(input('Qual é sua opção? '))

    # Iniciando partida
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PO!!!')

    # Definindo resultados
    print('-=' * 15)
    print(f'Computador escolheu a opção {computador}')
    print(f'Jogador escolheu a opção {jogador}')
    print('-=' * 15)

    # Definindo vencedor
    if computador == 0:
        if jogador == 0:
            print('EMPATE!')
        if jogador == 1: 
            print('JOGADOR GANHOU!')  
        if jogador == 2:
            print('COMPUTADOR GANHOU!')   

    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR GANHOU!') 
        if jogador == 1:  
            print('EMPATE!')
        if jogador == 2:
            print('JOGADOR GANHOU!') 

    elif computador == 2:
        if jogador == 0:
            print('JOGADOR GANHOU!')
        if jogador == 1: 
            print('COMPUTADOR GANHOU!')
        if jogador == 2: 
            print('EMPATE!')
    
    print('-=' * 15, '\n')
    
    # Definindo continuação
    continuar = input('Quer jogar de novo? [S/N]')
    if continuar in 'Nn':
        break
             
    



    
    

    
