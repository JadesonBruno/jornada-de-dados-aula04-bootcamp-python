# TYPE HINT

# Without Type Hint   
""" idade = 30
altura = 1.75
nome = "Alice"
is_estudante = True """

# With Type Hint
""" idade: int = 30
altura: float = 1.75
nome: str = "Alice"
estudante: bool = True """

# Refactoring the last desafio.py
""" valid_name: bool = False
valid_salary: bool = False
valid_bonus: bool = False

while not valid_name:
    try:
        name: str = input("Type your name: ")

        if not name:
            raise ValueError("Name cannot be empty.")
        elif name.isspace():
            raise ValueError("Name cannot contain only spaces.")
        elif any(char.isdigit() for char in name):
            raise ValueError("Name cannot contain digits.")
        else: 
            print("Your name is valid.")
            valid_name = True

    except ValueError as e:
        print(f"Error: {e}")

while not valid_salary:
    try:
        salary: float = float(input("Type your salary: "))

        if salary < 0:
            raise ValueError("Salary cannot be less than zero.")
        else: 
            print("Salary is valid.")
            valid_salary = True

    except ValueError as e:
        print(f"Error: {e}")

while not valid_bonus:
    try:
        bonus: float = float(input("Type your bonus: "))
        
        if bonus < 0:
            raise ValueError("Bonus cannot be less than zero.")
        else:
            print("Bonus is valid.")
            valid_bonus = True

    except ValueError as e:
        print(f"Error: {e}")

CONSTANTE_BONUS: float = 1000

final_bonus: float = CONSTANTE_BONUS + salary * bonus

print(f'''###============###\nMr./Mrs. {name},\nYour salary is: {salary}\nAnd your final bonus is: {final_bonus}\n###============###''') """

# LIST

""" produto_1: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "video-game"

produtos: list = list()

produtos.append(produto_1)
produtos.append(produto_2)
produtos.append(produto_3)

print(produtos) """

# Remove especific item
""" produtos.remove("sapato")

print(produtos) """

# Remove last item of list
""" produtos.pop()

print(produtos) """

# Using extend()
""" lista1: list = [1, 2, 3]
lista2: list = [4, 5, 6]

lista1.extend(lista2)

print(lista1)

lista1.extend(range(7, 15))

print(lista1) """

# DICT

# Diference of dict to list
""" list_product: list = ["Sapato", 39, 10.38, True]

product_01: dict = {
    "nome": "sapato",
    "quantity": 39,
    "preco": 10.38,
    "disponibility": True
}

product_02: dict = {
    "nome": "television",
    "quantity": 10,
    "preco": 70.38,
    "disponibility": False
}

cart: list = []

cart.append(product_01)
cart.append(product_02)

print(cart, type(cart)) """


# Working with json and dictionary
""" import json

json_cart: json = json.dumps(cart) # transforming python dictionary to json

print(json_cart, type(json_cart)) """

# CSV

# Readign csv file with native lib
""" import csv

path: str = "example.csv"

with open(file= path, mode= "r", encoding= "utf-8") as file:
    csv_reader: csv.DictReader = csv.DictReader(file)

    data = [line for line in csv_reader]

print(data) """

# FUNCTIONS

# without function

# Implementação do algoritmo de ordenação por seleção
# i = 1, [34, 64, 25, 12, 22, 11, 90];
# i = 2, [34, 25, 64, 12, 22, 11, 90];
# i = 3, [34, 25, 12, 64, 22, 11, 90].

""" lista = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

# Ordenando a lista
print("Lista ordenada com função personalizada:", lista) """

# with function
""" number_list = [64, 34, 25, 12, 22, 11, 90]

def sort_numbers_list(number_list: list) -> list:
    ordered_list = number_list.copy()

    for i in range(len(ordered_list)):
        for j in range(i+1, len(ordered_list)):
            if ordered_list[i] > ordered_list[j]:
                ordered_list[i], ordered_list[j] = ordered_list[j], ordered_list[i]

    return ordered_list

# Ordenando a lista
print(sort_numbers_list(number_list)) """

# with varied lists and foreseeing use in another script.py
""" import random

def sort_numbers_list(number_list: list) -> list:
    ordered_list = number_list.copy()

    for i in range(len(ordered_list)):
        for j in range(i+1, len(ordered_list)):
            if ordered_list[i] > ordered_list[j]:
                ordered_list[i], ordered_list[j] = ordered_list[j], ordered_list[i]

    return ordered_list

if __name__ == "__main__":
    len_list = 10
    min_value = 1
    max_value = 100

    aleatory_list_1: list = [random.randint(min_value, max_value) for _ in range(len_list)]
    aleatory_list_2: list = [random.randint(min_value, max_value) for _ in range(len_list)]
    aleatory_list_3: list = [random.randint(min_value, max_value) for _ in range(len_list)]
    
    # Ordenando a lista
    print(sort_numbers_list(aleatory_list_1))
    print(sort_numbers_list(aleatory_list_2))
    print(sort_numbers_list(aleatory_list_3)) """

# with bulti-in function sorted()
""" number_list: list = [64, 34, 25, 12, 22, 11, 90]
ordered_list: list = sorted(number_list)

print(number_list, ordered_list, sep= "\n") """

# with varied lists and foreseeing use in another script.py
""" import random

def sort_numbers_list(number_list: list) -> list:
    try:
        ordered_list = number_list.copy()

        for i in range(len(ordered_list)):
            for j in range(i+1, len(ordered_list)):
                if ordered_list[i] > ordered_list[j]:
                    ordered_list[i], ordered_list[j] = ordered_list[j], ordered_list[i]

        return ordered_list
    
    except:
        print("Error: Deu erro!")

nome = "Jadeson"

# Ordenando a lista
print(sort_numbers_list(nome)) """