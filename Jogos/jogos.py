import adivinhacao_for
import forca_com_funcao
print("################")
print("Escolha um jogo!")
print("################\n")

print("(1) Adivinhação\n(2) Forca\n")

jogo = int(input())

if (jogo == 1):
    print("Adivinhacao\n")
    adivinhacao_for.jogo()
elif (jogo ==2):
    print("Jogando forca\n")
    forca_com_funcao.jogo()
else:
    print("Opção inválida")