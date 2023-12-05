def main(user_input: str) -> str:
    var = user_input.split(" ")

    try:    
        if len(var) != 3 or var[1] not in {'+', '-', '*', '/'}:
            raise ValueError("Формат операции неверный")

        if not (var[0].isdigit() and var[2].isdigit()):
            raise ValueError("Введенные числа некорректны")

        num1 = int(var[0])
        num2 = int(var[2])
        operator = var[1]

        if not (1 <= num1 <= 10) or not (1 <= num2 <= 10):
            raise ValueError("Введенные числа меньше 1 или больше 10")

        result = calc(num1, operator, num2)
        return str(result)

    except ValueError as e:
        return f"Error: {e}"

def calc(num1: int, operator: str, num2: int) -> int:
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return int(num1 // num2)
    
if __name__ == '__main__':
    user_input = input("Введите пример в формате 1 + 2: ")
    result_end = main(user_input)
    print(result_end)
