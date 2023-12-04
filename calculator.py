def main(input_str: str) -> str:
    try:
        var = list(map(str, input_str.split()))

        if len(var) != 3 or var[1] not in {'+', '-', '*', '/'}:
            return "throws Exception: Формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)"

        if "." in var[0] or "." in var[2]:
            return "throws Exception: Введенные числа не целые"
        
        num1 = int(var[0])
        num2 = int(var[2])

        if not (1 <= num1 <= 10) or not (1 <= num2 <= 10):
            return "throws Exception: Введенные числа меньше 0 или больше 10"

        result = None
        if var[1] == "+":
            result = num1 + num2
        elif var[1] == "-": 
            result = num1 - num2
        elif var[1] == "*":
            result = num1 * num2
        elif var[1] == "/":
            result = num1 // num2
        return result

    except:
        return str(result)


user_input = input("Введите пример в формате 1 + 2: ")
result = main(user_input)
print(result)
