import random
from main import sort_numbers_list

list_size: int = 10
min_value: int = 1
max_value: int = 1000

aleatory_list: list = [random.randint(min_value, max_value) for _ in range(list_size)]
print(aleatory_list)

print(sort_numbers_list(aleatory_list))