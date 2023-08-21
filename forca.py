import random

# lista de palavras para o jogo
palavras = ['python', 'programacao', 'desenvolvimento', 'computador', 'algoritmo', 'jogo', 'github']

# função para escolher uma palavra aleatória
def escolher_palavra(palavras):
    return random.choice(palavras)

# função para exibir o estado atual da palavra com letras ocultas
def exibir_palavra(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

# função para receber a próxima letra do jogador
def receber_letra(letras_escolhidas):
    while True:
        letra = input('Digite uma letra: ').lower()
        if letra in letras_escolhidas:
            print('Você já escolheu essa letra. Tente outra.')
        elif len(letra) != 1 or not letra.isalpha():
            print('Por favor, digite apenas uma letra.')
        else:
            return letra

# função principal do jogo
def jogar_forca():
    print('Bem-vindo ao jogo da forca!')
    palavra = escolher_palavra(palavras)
    letras_corretas = set()
    letras_incorretas = set()
    max_erros = 6
    
    while True:
        # exibir estado atual da palavra
        exibir_palavra(palavra, letras_corretas)
        
        # exibir letras incorretas
        if letras_incorretas:
            print('Letras erradas:', ' '.join(sorted(letras_incorretas)))
        
        # checar se o jogador ganhou
        if all(letra in letras_corretas for letra in palavra):
            print('Parabéns, você ganhou!')
            break
        
        # checar se o jogador perdeu
        if len(letras_incorretas) >= max_erros:
            print('Você perdeu! A palavra era:', palavra)
            break
        
        # receber a próxima letra do jogador
        letra = receber_letra(letras_corretas.union(letras_incorretas))
        
        # checar se a letra está na palavra
        if letra in palavra:
            print('Boa escolha! Essa letra está na palavra.')
            letras_corretas.add(letra)
        else:
            print('Letra errada. Tente novamente.')
            letras_incorretas.add(letra)

# chamar a função principal do jogo
jogar_forca()
