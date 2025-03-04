# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
""" numbers: list = list(range(1, 11))

for i in numbers:
    squared = i ** 2
    print(squared) """

# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
""" programming_language: list = ["Python", "Java", "C++", "JavaScript"]

programming_language.remove("C++")
programming_language.append("Ruby")

print(programming_language) """

# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
""" livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}

for k, v in livro.items():
    print(f"{k}: {v}") """

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.