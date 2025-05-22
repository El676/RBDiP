from calculatorr import Calculator

def get_number_input(prompt: str) -> float:
    
    while True:
        try:
            value = input(prompt)
            return float(value) if '.' in value else int(value)
        except ValueError:
            print("Ошибка: введите корректное число!")

def get_operation_input() -> str:
    
    supported_ops = Calculator.get_supported_operations()
    op_descriptions = [
        f"{op} - {Calculator.get_operation_description(op)}"
        for op in supported_ops
    ]
    
    while True:
        print("\nДоступные операции:", *op_descriptions, sep="\n")
        op = input("\nВведите операцию: ").strip()
        if op in supported_ops:
            return op
        print(f"Ошибка: доступные операции - {', '.join(supported_ops)}")

def ask_to_continue() -> bool:
    
    while True:
        answer = input("\nПродолжить? (да/нет): ").lower()
        if answer in ('да', 'д', 'yes', 'y'):
            return True
        if answer in ('нет', 'н', 'no', 'n'):
            return False
        print("Пожалуйста, введите 'да' или 'нет'")

def display_welcome_message() -> None:
    
    print("\n=== Калькулятор ===")
    print("Доступные операции:")
    for op in Calculator.get_supported_operations():
        print(f"  {op} - {Calculator.get_operation_description(op)}")
    print("\nДля выхода нажмите Ctrl+C\n")