import pygame
import time
import random

# Inicializando o pygame
pygame.init()

# Definindo as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Tamanho da tela
largura = 600
altura = 400

# Configurando a tela do jogo
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha do Cyphrak')

# Configurações do relógio
relogio = pygame.time.Clock()

# Tamanho do bloco da cobrinha e a velocidade
tamanho_bloco = 10
velocidade = 20

# Função para exibir a pontuação
def pontuacao(score):
    fonte = pygame.font.SysFont("bahnschrift", 15)
    texto = fonte.render("Pontuação: " + str(score), True, preto)
    tela.blit(texto, [0, 0])

# Função principal do jogo
def jogo():
    game_over = False
    game_close = False

    # Posições iniciais da cobrinha
    x1 = largura / 2
    y1 = altura / 2
    x1_mudar = 0
    y1_mudar = 0

    # Lista para armazenar os segmentos da cobrinha
    corpo_cobrinha = []
    comprimento_cobrinha = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0

    while not game_over:

        while game_close:
            tela.fill(azul)
            fonte = pygame.font.SysFont("bahnschrift", 20)
            mensagem = fonte.render("Fim de Jogo! Pressione Q para Sair ou C para Jogar", True, vermelho)
            tela.blit(mensagem, [largura / 10, altura / 5])
            pontuacao(comprimento_cobrinha - 1)
            pygame.display.update()

            # Verifica as teclas pressionadas após o fim do jogo
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        jogo()

        # Eventos de controle
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x1_mudar = -tamanho_bloco
                    y1_mudar = 0
                elif evento.key == pygame.K_RIGHT:
                    x1_mudar = tamanho_bloco
                    y1_mudar = 0
                elif evento.key == pygame.K_UP:
                    y1_mudar = -tamanho_bloco
                    x1_mudar = 0
                elif evento.key == pygame.K_DOWN:
                    y1_mudar = tamanho_bloco
                    x1_mudar = 0

        # Se a cobrinha bater nas bordas, o jogo acaba
        if x1 >= largura or x1 < 0 or y1 >= altura or y1 < 0:
            game_close = True

        # Atualiza a posição da cobrinha
        x1 += x1_mudar
        y1 += y1_mudar
        tela.fill(azul)

        # Desenha a comida
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])

        # Atualiza o corpo da cobrinha
        corpo_cobrinha.append([x1, y1])
        if len(corpo_cobrinha) > comprimento_cobrinha:
            del corpo_cobrinha[0]

        for segmento in corpo_cobrinha[:-1]:
            if segmento == [x1, y1]:
                game_close = True

        for bloco in corpo_cobrinha:
            pygame.draw.rect(tela, verde, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])

        pontuacao(comprimento_cobrinha - 1)

        pygame.display.update()

        # Verifica se a cobrinha comeu a comida
        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 10.0) * 10.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 10.0) * 10.0
            comprimento_cobrinha += 2
            
        

        relogio.tick(velocidade)

    pygame.quit()
    quit()

# Inicia o jogo
jogo()
