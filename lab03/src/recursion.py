def factorial(n):
    """
    Вычисление факториала числа n
    Сложность: O(n)
    Глубина рекурсии: n
    """
    if n <= 1:  # Базовый случай
        return 1
    return n * factorial(n - 1)  # Рекурсивный шаг


def fibonacci(n):
    """
    Вычисление n-го числа Фибоначчи (наивная рекурсия)
    Сложность: O(2^n)
    Глубина рекурсии: n
    """
    if n <= 1:  # Базовый случай
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Рекурсивный шаг


def fast_pow(a, n):
    """
    Быстрое возведение числа a в степень n
    Сложность: O(log n)
    Глубина рекурсии: log n
    """
    if n == 0:  # Базовый случай
        return 1
    if n % 2 == 0:  # Четная степень
        return fast_pow(a * a, n // 2)
    else:  # Нечетная степень
        return a * fast_pow(a, n - 1)


def demo_functions():
    """Демонстрация работы рекурсивных функций"""
    print("РЕКУРСИВНЫЕ ФУНКЦИИ")
    print("=" * 30)
    
    print(f"Факториал 5: {factorial(5)}")  # 120
    print(f"Число Фибоначчи F(6): {fibonacci(6)}")  # 8
    print(f"2^10 = {fast_pow(2, 10)}")  # 1024
    
    print("\nПроверка факториала:")
    for i in range(1, 6):
        print(f"{i}! = {factorial(i)}")


if __name__ == "__main__":
    demo_functions()