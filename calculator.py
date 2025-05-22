def calc():
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    op = input("Введите операцию (+, -, *, /): ")
    
    if op == '+':
        res = x + y
    elif op == '-':
        res = x - y
    elif op == '*':
        res = x * y
    elif op == '/':
        if y == 0:
            print("Ошибка: деление на ноль!")
            return
        res = x / y
    else:
        print("Неизвестная операция!")
        return
    
    print(f"Результат: {res}")

def main():
    while True:
        calc()
        again = input("Продолжить? (да/нет): ").lower()
        if again != 'да':
            break

if __name__ == "__main__":
    main()
    