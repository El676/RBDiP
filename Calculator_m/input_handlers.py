from calculatorm import Calculator

def get_number_input(prompt: str) -> float:
    while True:
        try:
            num = float(input(prompt))
            if num.is_integer():
                return int(num)
            return num
        except ValueError:
            print("Ошибка: введите корректное число!")

def get_operation_input() -> str:
    supported_ops = Calculator.get_supported_operations()
    while True:
        print("\nДоступные операции:")
        for op in supported_ops:
            print(f"{op} - {Calculator.get_operation_description(op)}")
        
        op = input("\nВведите операцию: ").strip()
        if op in supported_ops:
            return op
        print(f"Ошибка: операция должна быть одной из: {', '.join(supported_ops)}")

def ask_to_continue() -> bool:
    while True:
        answer = input("\nПродолжить вычисления? (да/нет): ").lower()
        if answer in ('да', 'д', 'yes', 'y'):
            return True
        elif answer in ('нет', 'н', 'no', 'n'):
            return False
        print("Пожалуйста, введите 'да' или 'нет'")

def display_welcome_message():
    print("\nДобро пожаловать в калькулятор!")
    print("Вы можете выполнять базовые математические операции.\n")