def fibonacci_dp(n):
    """
    Числа Фибоначчи через ДП (восходящий подход)
    Сложность: O(n) время, O(n) память
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def knapsack_01_dp(capacity, weights, values):
    """
    Задача о рюкзаке 0/1 через ДП
    Сложность: O(n * capacity) время, O(n * capacity) память
    """
    n = len(weights)
    
    # Создаем таблицу DP
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Заполняем таблицу
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Можно взять предмет
                dp[i][w] = max(
                    dp[i - 1][w],  # Не берем
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]  # Берем
                )
            else:
                # Нельзя взять предмет
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]


def test_algorithms():
    """Тестируем 2 алгоритма"""
    print("Тестирование алгоритмов ДП")
    print("=" * 40)
    
    # Test 1: Фибоначчи
    print("1. Числа Фибоначчи:")
    for n in [0, 1, 5, 10, 20]:
        result = fibonacci_dp(n)
        print(f"   F({n}) = {result}")
    
    # Test 2: Рюкзак 0/1
    print("\n2. Рюкзак 0/1:")
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 7
    
    max_value = knapsack_01_dp(capacity, weights, values)
    print(f"   Веса: {weights}")
    print(f"   Стоимости: {values}")
    print(f"   Вместимость: {capacity}")
    print(f"   Максимальная стоимость: {max_value}")


if __name__ == "__main__":
    test_algorithms()