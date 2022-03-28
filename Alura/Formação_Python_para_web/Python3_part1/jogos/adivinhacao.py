import random

print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000

print("Qual será o nível de dificuldade?")
print("(1) Fácil \n(2) Médio \n(3) Difícil")

nivel = int(input("Nível Definido: "))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}" .format(rodada, total_de_tentativas))

    # preciso declarar o tipo do input, porque input sempre retorna string
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: {}" .format(chute_str))
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou e fez {} pontos!" .format(pontos))
        break
    else:
        if maior:
            print("Você errou! Seu chute foi maior do que o numero secreto\n")
        elif menor:
            print("Você errou! Seu chute foi menor do que o numero secreto\n")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("O número secreto era {}." .format(numero_secreto))
print("Fim de jogo!")
