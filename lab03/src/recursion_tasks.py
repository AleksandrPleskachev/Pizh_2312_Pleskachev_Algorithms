def binary_search_recursive(arr, target, left=0, right=None):
    """
    Бинарный поиск с использованием рекурсии
    Сложность: O(log n)
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:  # Базовый случай - элемент не найден
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:  # Базовый случай - элемент найден
        return mid
    elif arr[mid] < target:  # Рекурсивный шаг - искать справа
        return binary_search_recursive(arr, target, mid + 1, right)
    else:  # Рекурсивный шаг - искать слева
        return binary_search_recursive(arr, target, left, mid - 1)


def hanoi_towers(n, source="A", auxiliary="B", destination="C"):
    """
    Решение задачи "Ханойские башни"
    Количество шагов: 2^n - 1
    """
    if n == 1:  # Базовый случай
        print(f"Переместить диск 1 со стержня {source} на {destination}")
        return
    
    # Рекурсивный шаг
    hanoi_towers(n - 1, source, destination, auxiliary)
    print(f"Переместить диск {n} со стержня {source} на {destination}")
    hanoi_towers(n - 1, auxiliary, source, destination)


def test_algorithms():
    """Тестирование реализованных алгоритмов"""
    print("ТЕСТИРОВАНИЕ АЛГОРИТМОВ")
    print("=" * 30)
    
    # Тест бинарного поиска
    print("\n1. БИНАРНЫЙ ПОИСК")
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    result = binary_search_recursive(arr, target)
    print(f"Массив: {arr}")
    print(f"Ищем {target}: индекс {result}")
    
    # Тест Ханойских башен
    print("\n2. ХАНОЙСКИЕ БАШНИ (3 диска)")
    print("=" * 20)
    hanoi_towers(3)


if __name__ == "__main__":
    test_algorithms()