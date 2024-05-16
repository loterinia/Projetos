import random

numeroSecreto = random.randint(1, 100)

print("Bem vindo ao jogo", "\n" "Digite um número de 1 a 100 para adivinhar: ")

tentativas = 0

while tentativas <7:
    palpite = int(input("Digite seu palpite"))
    
    if palpite == numeroSecreto:
        print("Você acertou!")
        break
    elif palpite < numeroSecreto:
        print("Muito baixo")
    else:
        print("Muito alto")
        
    tentativas += 1
    
if tentativas == 7:
    print("Acabaram suas tentativas. O número secreto era:", numeroSecreto)