# Inteiros (int) e números de ponto flutuante (float)
idade = 25  # Tipo inteiro
altura = 1.75  # Tipo float

# Booleanos (bool)
maior_de_idade = idade >= 18  # True, pois 25 é maior que 18

# Strings (str)
nome = " Alice "
mensagem = f"Olá, meu nome é {nome.strip()} e eu tenho {idade} anos."
# Usa f"{}" para formatação de strings (mais moderno que format()).

# Métodos úteis para strings
nome_maiusculo = nome.upper()  # Converte para maiúsculas
nome_minusculo = nome.lower()  # Converte para minúsculas
nome_tamanho = len(nome.strip())  # Conta os caracteres, removendo espaços extras

# Exibindo os valores
print("Idade:", idade, "- Tipo:", type(idade))
print("Altura:", altura, "- Tipo:", type(altura))
print("Maior de idade?", maior_de_idade, "- Tipo:", type(maior_de_idade))
print(mensagem)  # Exibe a mensagem formatada
print("Nome em maiúsculas:", nome_maiusculo)
print("Nome em minúsculas:", nome_minusculo)
print("Número de caracteres no nome:", nome_tamanho)
