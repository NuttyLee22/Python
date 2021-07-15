def jogo():
    import random
    print("################################")
    print("Bem vindo ao jogo da adivinhação")
    print("################################\n")

    print("Nesse jogo você tem que adivinhar um número entre 1 e 100. \n"
          "Você começa com um total de 1000 pontos, que vai diminuindo \n"
          "a cada vez que errar o número, subtraindo a diferença entre \n"
          "o número que você digitou do número secreto\n")

    numero_secreto = random.randrange(1, 101)
    print("Níveis de dificuldade:\n(1) Fácil\n(2) Médio\n(3) Dificíl\n")

    nivel=int(input("Escolha seu nível: "))
    pontos = 1000

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5
    else:
        total_de_tentativas = 0
        print("Opção inválida")

    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou ", chute, "\n")

        if (chute<0 or chute>100):
            print("Você deve digitar um número entre 1 e 100!\n")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("\nParabéns! Você acertou!\nTotal de pontos: {}".format(pontos))
            break
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
                if(rodada == total_de_tentativas):
                    print("\nO número secreto era: {}\nTotal de pontos: {}".format(numero_secreto, pontos))
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
                if (rodada == total_de_tentativas):
                    print("\nO número secreto era: {}\nTotal de pontos: {}".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogo()