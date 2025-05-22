from calculatorm import Calculator
from input_handlers import (
    get_number_input, 
    get_operation_input, 
    ask_to_continue,
    display_welcome_message
)

def perform_calculation() -> None:
    try:
        num1 = get_number_input("Введите первое число: ")
        num2 = get_number_input("Введите второе число: ")
        operation = get_operation_input()
        
        result = Calculator.calculate(num1, num2, operation)
        
        if result is None:
            print("\nОшибка: невозможная операция (деление на ноль)!")
        else:
            print(f"\nРезультат: {num1} {operation} {num2} = {result}")
    except Exception as e:
        print(f"\nПроизошла ошибка: {str(e)}")

def main() -> None:
    display_welcome_message()
    while True:
        try:
            perform_calculation()
            if not ask_to_continue():
                print("\nСпасибо за использование калькулятора!")
                break
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            break

if __name__ == "__main__":
    main()