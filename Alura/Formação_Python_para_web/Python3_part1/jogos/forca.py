def jogar():
    print("*********************************")
    print("** Bem vindo ao jogo de Forca! **")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]  # Isto se chama List comprehensions

    acertou = False
    enforcou = False
    erros = 0

    print(letras_acertadas)

    while not acertou and not enforcou:
        chute = input("Qual Letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você venceu!")
    else:
        print("Você perdeu!")

    print("Fim de jogo!")


if __name__ == "__main__":
    jogar()
