from calculatorr import Calculator
from input_handlersr import (
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
            print("Ошибка: деление на ноль!")
        else:
            print(f"Результат: {num1} {operation} {num2} = {result}")
    except ValueError as e:
        print(f"Ошибка: {str(e)}")
    except Exception as e:
        print(f"Неожиданная ошибка: {str(e)}")

def main() -> None:
    
    display_welcome_message()
    
    while True:
        try:
            perform_calculation()
            if not ask_to_continue():
                print("\nДо свидания!")
                break
        except KeyboardInterrupt:
            print("\n\nРабота калькулятора завершена.")
            break

if __name__ == "__main__":
    main()