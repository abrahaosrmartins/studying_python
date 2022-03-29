import forca
import adivinhacao


def escolhe_jogo():
    print("*********************************")
    print("****** Escolha o seu jogo! ******")
    print("*********************************")

    print("(1) Forca \n(2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if jogo == 1:
        print("Jogando Forca.")
        forca.jogar()
    elif jogo == 2:
        print("Jogando Advinhação")
        adivinhacao.jogar()


if __name__ == "__main__":
    escolhe_jogo()
