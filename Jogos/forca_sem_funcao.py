import random
def jogo():
    print("*******************************************")
    print("***Bem vindo ao jogo da Forca de Frutas!***")
    print("*******************************************")

    # arquivo = open("palavras.txt", "r")
    # arquivo.close() #-- sempre precisa fechar o arquivo, menos quando usa o comando WITH
    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    # letras_acertadas= []
    # for letra in palavra_secreta:
    #     letras_acertadas.append("_")

    letras_acertadas = ["_" for letra in palavra_secreta]
    # List Comprehension: desse jeito da para fazer aquele for ali de cima dentro da própria lista
    # Outro exemplo:
    # inteiros = [1, 3, 4, 5, 7, 8, 9] -- selecionar apenas os numeros pares
    # pares = [x for x in inteiros if x % 2 == 0]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not acertou and not enforcou):

        chute = input("Digite uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = (erros == len(palavras))
        acertou = ("_" not in letras_acertadas)
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim de jogo")

if(__name__ == "__main__"):
    jogo()