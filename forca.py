import random
import re

def sortear_palavra():
    palavras_possiveis = ['abacadabra', 'finalidade', 'idoneidade', 'sublime', 'cultura', 'alcunha']
    posicao_da_palavra = random.randint(0, len(palavras_possiveis))
    return palavras_possiveis[posicao_da_palavra]

def escolher_letra():
    escolha = input("Por favor, escolha uma letra de A a Z sem acentos: ")
    while (re.search('[^a-zA-Z]', escolha)) or (len(escolha) != 1):
        escolha = input("Escolha inválida. Por favor, escolha uma letra de A a Z sem acentos: ")
    return escolha

print("***JOGO DA FORCA***\n")
print("Esta é sua palavra: \n")
palavra_sorteada = sortear_palavra()
print("_ " * len(palavra_sorteada))

tentativas_restantes = 6
letras_restantes = len(palavra_sorteada)
palavra_descoberta = list("_" * len(palavra_sorteada))

#Enquanto ainda houver tentativas e letras para descobrir
while (tentativas_restantes > 0) and (letras_restantes > 0):
    letra_escolhida = escolher_letra()
    letra_escolhida = letra_escolhida.lower()

    #Se a letra escolhida não pertence à palavra, subtrair uma tentativa
    if letra_escolhida not in palavra_sorteada:
        tentativas_restantes -= 1
        print('\nA letra escolhida não faz parte da palavra. Você perdeu uma tentativa.\n')

    #Se a letra escolhida estiver na palavra, diminuir a quantidade de letras que faltam encontrar e preencher a palavra exibida para o usuário com ela
    index = 0
    for letra in palavra_sorteada:
        if letra == letra_escolhida:
            letras_restantes -= 1
            palavra_descoberta[index] = letra_escolhida
        index += 1

    #Exibir a palavra para o usuário com as letras já descobertas
    for letra in palavra_descoberta:
        print(letra, "", end="")


    print("\nVocê possui mais {} tentativa(s).\n".format(tentativas_restantes))


if tentativas_restantes == 0:
    print('Acabaram as tentativas :(\nVocê foi enforcado!')

if letras_restantes == 0:
    print('Parabéns! Você descobriu que a palavra secreta é {}!'.format(palavra_sorteada))

print("\nFim do jogo")
