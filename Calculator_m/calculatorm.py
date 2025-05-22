class Calculator:
    OPERATIONS = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else None,
        '%': lambda a, b: a % b if b != 0 else None,
        '**': lambda a, b: a ** b
    }

    @staticmethod
    def calculate(num1: float, num2: float, operation: str) -> float:
        if operation not in Calculator.OPERATIONS:
            raise ValueError("Неподдерживаемая операция")
        return Calculator.OPERATIONS[operation](num1, num2)

    @staticmethod
    def get_supported_operations() -> list:
        return list(Calculator.OPERATIONS.keys())

    @staticmethod
    def get_operation_description(op: str) -> str:
        descriptions = {
            '+': "Сложение",
            '-': "Вычитание",
            '*': "Умножение",
            '/': "Деление",
            '%': "Остаток от деления",
            '**': "Возведение в степень"
        }
        return descriptions.get(op, "Неизвестная операция")