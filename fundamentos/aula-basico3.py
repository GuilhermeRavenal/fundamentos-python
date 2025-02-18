texto = "Python is fun! Python is powerful! Python is easy to learn!"

# Convertendo para maiúsculas e minúsculas
print("Texto em maiúsculas:", texto.upper())
print("Texto em minúsculas:", texto.lower())

# Contando quantas vezes "Python" aparece
contagem = texto.count("Python")
print(f"A palavra 'Python' aparece {contagem} vezes no texto.")

# Substituindo palavras
novo_texto = texto.replace("Python", "Programming")
print("Texto modificado:", novo_texto)

# Contando o número de caracteres no texto
tamanho_texto = len(texto)
print(f"O texto tem {tamanho_texto} caracteres.")

# Dividindo o texto em palavras (gera uma lista)
palavras = texto.split()
print("Lista de palavras no texto:", palavras)

# Unindo a lista de palavras de volta em uma string separada por hífen
texto_reconstruido = " - ".join(palavras)
print("Texto reconstruído com hífens:", texto_reconstruido)
