import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Definindo as cores
COR_FUNDO = (255, 255, 255)
COR_TEXTO = (0, 0, 0)

# Definindo as dimensões da janela
largura = 800
altura = 600

# Criando a janela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Quiz de Geografia')

# Definindo a fonte
fonte = pygame.font.Font(None, 36)

# Definindo as perguntas e respostas
perguntas = [
    "Qual é o país com a maior população?",
    "Qual é o país com a maior área territorial?",
    "Qual é o país mais visitado por turistas?",
    "Qual é o país com a maior economia?",
    "Qual é o país com o maior número de Patrimônios Mundiais da UNESCO?"
]

respostas = [
    ["China", "Índia", "Estados Unidos", "Brasil"],
    ["Rússia", "Canadá", "China", "Estados Unidos"],
    ["França", "Estados Unidos", "Espanha", "China"],
    ["Estados Unidos", "China", "Japão", "Alemanha"],
    ["Itália", "Espanha", "China", "França"]
]

respostas_corretas = [0, 1, 1, 0, 2]

pontuacao = 0
pergunta_atual = 0

# Função para exibir a pergunta atual
def exibir_pergunta(pergunta, opcoes):
    tela.fill(COR_FUNDO)

    texto_pergunta = fonte.render(pergunta, True, COR_TEXTO)
    tela.blit(texto_pergunta, (20, 20))

    y = 100
    for i, opcao in enumerate(opcoes):
        texto_opcao = fonte.render(opcao, True, COR_TEXTO)
        tela.blit(texto_opcao, (20, y))
        y += 50

    pygame.display.flip()

# Função para exibir a pontuação final
def exibir_pontuacao_final(pontos):
    tela.fill(COR_FUNDO)

    texto_final = fonte.render("Fim do jogo! Você acertou {} perguntas.".format(pontos), True, COR_TEXTO)
    tela.blit(texto_final, (20, altura // 2 - 50))

    pygame.display.flip()

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_1:
                if respostas_corretas[pergunta_atual] == 0:
                    pontuacao += 1
                pergunta_atual += 1
            elif evento.key == pygame.K_2:
                if respostas_corretas[pergunta_atual] == 1:
                    pontuacao += 1
                pergunta_atual += 1
            elif evento.key == pygame.K_3:
                if respostas_corretas[pergunta_atual] == 2:
                    pontuacao += 1
                pergunta_atual += 1
            elif evento.key == pygame.K_4:
                if respostas_corretas[pergunta_atual] == 3:
                    pontuacao += 1
                pergunta_atual += 1

    if pergunta_atual < len(perguntas):
        exibir_pergunta(perguntas[pergunta_atual], respostas[pergunta_atual])
    else:
        exibir_pontuacao_final(pontuacao)
