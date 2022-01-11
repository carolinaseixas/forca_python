import re

def escolhe_letra():
    escolha = input("Por favor, escolha uma letra de A a Z sem acentos: ")
    #Checando se a entrada do usuário é uma única letra
    while (re.search('[^a-zA-Z]', escolha)) or (len(escolha) != 1):
        escolha = input("Escolha inválida. Por favor, escolha uma letra de A a Z sem acentos: ")
    return escolha


#Deve-se definir a palavra aqui
palavra = 'abracadabra'

#Imprimindo a abertura do jogo e um _ para cada letra da palavra
print("***JOGO DA FORCA***\n")
print("Esta é sua palavra: \n")
print("_ " * len(palavra))

#Inicializando as variáveis de tentativas, de letras descobertas e de letras restantes para descobrir
tentativas_restantes = 6
letras_restantes = len(palavra)
palavra_atual = list("_" * len(palavra))

#Enquanto ainda houver tentativas e letras para descobrir
while (tentativas_restantes > 0) and (letras_restantes > 0):
    letra_escolhida = escolhe_letra()
    letra_escolhida = letra_escolhida.lower()

    #Se a letra escolhida não pertence à palavra, subtrair uma tentativa
    if letra_escolhida not in palavra:
        tentativas_restantes -= 1
        print('\nA letra escolhida não faz parte da palavra. Você perdeu uma tentativa.\n')

    #Se a letra escolhida estiver na palavra, diminuir a quantidade de letras que faltam encontrar e preencher a palavra exibida para o usuário com ela
    index = 0
    for letra in palavra:
        if letra == letra_escolhida:
            letras_restantes -= 1
            palavra_atual[index] = letra_escolhida
        index += 1

    #Exibir a palavra para o usuário com as letras já descobertas
    for letra in palavra_atual:
        print(letra, "", end="")


    print("\nVocê possui mais {} tentativa(s).\n".format(tentativas_restantes))


if tentativas_restantes == 0:
    print('Acabaram as tentativas :(\nVocê foi enforcado!')

if letras_restantes == 0:
    print('Parabéns! Você descobriu que a palavra secreta é {}!'.format(palavra))

print("\nFim do jogo")
