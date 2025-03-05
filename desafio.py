# Integre no desafio anterior funções, type hint e dicionários.
from typing import Dict, List, Union

def validate_name(name: str) -> str:
    if not name:
        raise ValueError("Name cannot be empty.")
    elif name.isspace():
        raise ValueError("Name cannot contain only spaces.")
    elif any(char.isdigit() for char in name):
        raise ValueError("Name cannot contain digits.")
    else: 
        print("Your name is valid.")
        return name
    
def validate_salary(salary: float) -> float:
    if salary < 0:
        raise ValueError("Salary cannot be less than zero.")
    else: 
        print("Salary is valid.")
        return salary
    
def validate_bonus(bonus: float) -> float:
    if bonus < 0:
        raise ValueError("Bonus cannot be less than zero.")
    else:
        print("Bonus is valid.")
        return bonus

def calculate_final_bonus(salary: float, bonus: float, CONSTANT_BONUS: float) -> float:    
    return  CONSTANT_BONUS + salary * bonus

def main() -> List[Dict[str, Union[str, float]]]:
    resultados: List[Dict[str, Union[str, float]]] = []

    while True:
        try:
            name_input = input("Enter your name (or type 'exit' to finish): ")
            if name_input.lower() == "exit":
                break
            name: str = validate_name(name_input)

            salary_input = input("Enter your salary: ")
            salary = validate_salary(float(salary_input))

            bonus_input = input("Enter your bonus: ")
            bonus = validate_bonus(float(bonus_input))

            CONSTANT_BONUS = 1000
            final_bonus = calculate_final_bonus(salary, bonus, CONSTANT_BONUS)

            resultado = {
                "name": name,
                "salary": salary,
                "bonus": bonus,
                "final_bonus": final_bonus
            }

            resultados.append(resultado)

            print(f'''###============###\nMr./Mrs. {name},\nYour salary is: {salary}\nAnd your final bonus is: {final_bonus}\n###============###''')

        except ValueError as e:
            print(f'Error: {e}')

    return resultados

if __name__ == "__main__":
    final_result = main()
    print(f"Final results: {final_result}")