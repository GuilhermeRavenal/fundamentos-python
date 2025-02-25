verse_dict = {
    'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 
    'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 
    'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 
    'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 
    'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 
    'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, "don't": 3, 
    'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 
    'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1
}

# Número de palavras únicas em verse_dict
num_unique_words = len(verse_dict)
print("Number of unique words:", num_unique_words)

# A chave "breathe" está em verse_dict?
is_breathe_in_dict = "breathe" in verse_dict
print("Is 'breathe' in verse_dict?:", is_breathe_in_dict)

# Primeiro elemento no dicionário (não ordenado)
first_key = next(iter(verse_dict))  # Pega a primeira chave sem ordenação
print("First key in verse_dict:", first_key)

# Primeiro elemento na lista de chaves ordenadas
sorted_keys = sorted(verse_dict.keys())  # Ordena as chaves alfabeticamente
first_sorted_key = sorted_keys[0]  # Pega a primeira chave ordenada
print("First element in sorted key list:", first_sorted_key)

# Qual palavra tem o maior valor no dicionário?
max_word = max(verse_dict, key=verse_dict.get)  # Encontra a chave com maior valor
print("Word with the highest value:", max_word)
