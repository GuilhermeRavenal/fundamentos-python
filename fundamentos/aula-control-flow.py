
# Condicionais

idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida!")
elif idade <= 12:
    print("Você é uma criança.")
elif idade <= 17:
    print("Você é um adolescente.")
elif idade <= 64:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

# Loops for

num = int(input("Digite um número: "))

for i in range(1, 11):  # Laço de 1 a 10
    print(f"{num} x {i} = {num * i}")

# Loops while

import random
numero_secreto = random.randint(1, 10)  # Gera um número aleatório de 1 a 10
tentativa = 0

while tentativa != numero_secreto:
    tentativa = int(input("Adivinhe o número (entre 1 e 10): "))
    
    if tentativa < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif tentativa > numero_secreto:
        print("Muito alto! Tente novamente.")

print("Parabéns! Você acertou!")

# Break e continue

numero_secreto = random.randint(1, 20)  # Número aleatório entre 1 e 20
tentativas = 5

print("Jogo de Adivinhação! Você tem 5 chances para acertar o número secreto entre 1 e 20.")

for tentativa in range(1, tentativas + 1):
    chute = int(input(f"Tentativa {tentativa}/{tentativas}: Digite seu palpite: "))

    # Se o número estiver fora do intervalo, pula a tentativa
    if chute < 1 or chute > 20:
        print("Número inválido! Digite um número entre 1 e 20.")
        continue  # Pula para a próxima iteração do loop

    if chute == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        break  # Sai do loop se acertar
    else:
        print("Errado! Tente novamente.")

else:  # Esse bloco só é executado se o usuário errar todas as tentativas
    print(f"Você perdeu! O número secreto era {numero_secreto}.")
