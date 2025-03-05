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
""" from typing import Dict, Any

livro_1: Dict[str, Any] = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}

for k, v in livro_1.items():
    print(f"{k}: {v}")

livro_2: Dict[str, Any] = {"titulo": "Game of Thrones", "autor": "George R. R. Martin", "ano": 2011}

books_list: list = []

books_list.append(livro_1)
books_list.append(livro_2)

print(books_list)

books_dict: dict = {
    "book_1": livro_1, 
    "book_2": livro_2
}

print(books_dict)

print(books_dict["book_1"]["titulo"])
print(list(books_dict["book_1"].values())) """

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# Using get()
""" def character_count(string):
    count: dict = {}

    for character in string:
        count[character] = count.get(character, 0) + 1

    return count 

print(character_count("engenharia de dados")) """

# Whithout get()
""" def character_count(string):
    count: dict = {}

    for character in string:
        if character not in count:
            count[character] = 1
        else:
            count[character] += 1

    return count 

print(character_count("engenharia de dados")) """

# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
# calcule o preço total da lista de compras.
# without list comprehension
""" fruits_list: list = ["maçã", "banana", "cereja"]
fruits_dict: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total_price: float = 0

for i in fruits_list:
    total_price += fruits_dict[i]

print(total_price) """

# with list comprehension
""" fruits_list: list = ["maçã", "banana", "cereja"]
prices: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}


total_price: float = sum(prices[fruit] for fruit in prices)


print(total_price) """

# 6. [Remover duplicatas] Dada uma lista de emails, remover todos os duplicados.
""" emails: list = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]

unique_emails: list = list(set(emails))

print(unique_emails) """

# 7. [Filtragem de Dados] Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
""" idades: list = [22, 15, 30, 17, 18]

filtered_ages: list = [age for age in idades if age >= 18]

print(filtered_ages) """

# 8. [Ordenação Personalizada] Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
""" peoples: dict = [
    {"nome": "Bob", "idade": 30},
    {"nome": "Alice", "idade": 25},
    {"nome": "Carol", "idade": 20}
]

peoples.sort(key= lambda peoples: peoples["nome"])

print(peoples) """

# 9. [Agregação de Dados] Dado um conjunto de números, calcular a média.
""" numeros: list = [10, 20, 30, 40, 50]

average: float = sum(numeros) / len(numeros)

print(average) """

# 10. [Divisão de Dados em Grupos] Dada uma lista de valores, dividir em duas listas: uma para valores 
# pares e outra para ímpares.
""" numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even: list = [even for even in numbers if even % 2 == 0]

odd: list = [odd for odd in numbers if odd % 2 != 0]

print(f"Even: {even}\nOdd: {odd}") """

# 11. [Atualização de Dados] Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
# desempacotamento de dicionários
""" products: list = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

# Atualizar o preço do produto com id 2 para 90
update_products: list = [{**product, "preço": 90} if product["id"] == 2 else product for product in products]

print(update_products) """

# Unpacking with function
############## Ex1.: ##############
""" def apresentar(**kwargs):
    print(f"Meu nome é {kwargs["nome"]}, tenho {kwargs["idade"]} anos e moro em {kwargs["cidade"]}.")

# Dicionário com os dados
dados: dict = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}

# Desempacotando o dicionário como argumentos
apresentar(**dados) """

############## Ex2.: ##############
""" def apresentar(nome, idade, cidade):
    print(f"Meu nome é {nome}, tenho {idade} anos e moro em {cidade}.")

# Dicionário com os dados
dados: dict = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}

# Desempacotando o dicionário como argumentos
apresentar(**dados) """
############## End ##############

# with for
""" products: list = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

for product in products:
    if product["id"] == 2:
        product["preço"] = 90

print(products) """

# 12. [Fusão de Dicionários] Dados dois dicionários, fundi-los em um único dicionário.
""" dicionario1: dict = {"a": 1, "b": 2}
dicionario2: dict = {"c": 3, "d": 4}

cominated_dict: dict = {**dicionario1, **dicionario2}

print(cominated_dict) """

# 13. [Filtragem de Dados em Dicionário] Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
# with dictionary comprehension
""" estoque: dict = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

filtered_stock: dict = {product: quantity for product, quantity in estoque.items() if quantity > 0}

print(filtered_stock) """

# without dictionary comprehencion
""" estoque: dict = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

filtered_stock: dict = {}

for product, quantity in estoque.items():
    if quantity > 0:
        filtered_stock[product] = quantity

print(filtered_stock) """

# 14. [Extração de Chaves e Valores] Dado um dicionário, criar listas separadas para suas chaves e valores.
""" dictonary: dict = {"a": 1, "b": 2, "c": 3}

keys: list = [key for key in dictonary.keys()]

values: list = [value for value in dictonary.values()]

print(keys, values, sep='\n') """

# 15. [Contagem de Frequência de Itens] Dada uma string, contar a frequência de cada caractere usando um dicionário.
""" text = "engenharia de dados"
words_count = {}

for word in text:
    words_count[word] = words_count.get(word, 0) + 1

print(words_count) """

# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
""" import random

def add_numbers(numbers_list: list) -> list:
    return sum(numbers_list) 

def generate_random_number(min_value: float, max_value: float, list_size: int) -> list:
    numbers_list = random.sample((range(min_value, max_value + 1)), list_size)
    print(numbers_list)
    return numbers_list

print(add_numbers(generate_random_number(0, 1000, 10))) """

# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
""" def validate_prime_number(number: int) -> bool:
    number_prime = True

    if number <= 1:
        number_prime = False
    for i in range(2, int(number**0.5)):
        if number % i == 0:
            number_prime = False

    return f"Number Prime is {number_prime}"

number = int(input("Enter a integer: "))

print(validate_prime_number(number)) """

# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
""" def return_reverse_string(string: str) -> str:
    return string[::-1]

string = input("Enter a string: ")

print(return_reverse_string(string)) """

# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. 
# A função deve retornar todas as combinações de pares na lista que somem ao número dado.
""" def find_pairs(numbers: list, target: int) -> list:
    pairs = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))

    return pairs    

numbers = [2, 4, 3, 5, 7, 8, 1, 9]
target = 10

print(find_pairs(numbers, target)) """

# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.
""" def sort_keys(fruits_dictionary: dict) -> dict:
    fruits_list = sorted(fruits_dictionary.keys())

    return fruits_list

dicionario_exemplo = {
    "banana": 3,
    "maçã": 5,
    "laranja": 2,
    "abacaxi": 4
}

print(sort_keys(dicionario_exemplo)) """