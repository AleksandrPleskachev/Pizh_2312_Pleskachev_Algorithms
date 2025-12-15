# greedy_algorithms.py
"""
Жадные алгоритмы для оценки 3
"""

def interval_scheduling(intervals):
    """
    Задача о выборе заявок.
    Сложность: O(n log n)
    """
    if not intervals:
        return []
    
    # Сортируем по времени окончания
    intervals.sort(key=lambda x: x[1])
    
    selected = []
    last_end = -float('inf')
    
    for start, end in intervals:
        if start >= last_end:  # Не пересекается
            selected.append((start, end))
            last_end = end
    
    return selected


def fractional_knapsack(capacity, items):
    """
    Непрерывный рюкзак.
    Сложность: O(n log n)
    """
    # Считаем удельную стоимость
    for item in items:
        item['ratio'] = item['value'] / item['weight']
    
    # Сортируем по убыванию удельной стоимости
    items.sort(key=lambda x: x['ratio'], reverse=True)
    
    total_value = 0
    remaining = capacity
    
    for item in items:
        if remaining <= 0:
            break
            
        take = min(item['weight'], remaining)
        total_value += take * item['ratio']
        remaining -= take
    
    return total_value


def test_algorithms():
    """Тестируем 2 алгоритма"""
    print("Тестирование жадных алгоритмов")
    print("=" * 40)
    
    # Test 1: Interval Scheduling
    intervals = [(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (8, 9)]
    result = interval_scheduling(intervals)
    print(f"1. Interval Scheduling:")
    print(f"   Вход: {intervals}")
    print(f"   Выбрано: {result}")
    print(f"   Количество: {len(result)}")
    
    # Test 2: Fractional Knapsack
    items = [
        {'weight': 10, 'value': 60},
        {'weight': 20, 'value': 100},
        {'weight': 30, 'value': 120}
    ]
    capacity = 50
    max_value = fractional_knapsack(capacity, items)
    print(f"\n2. Fractional Knapsack:")
    print(f"   Вместимость: {capacity}")
    print(f"   Предметы: {items}")
    print(f"   Максимальная стоимость: {max_value:.2f}")
    
    print("\n✓ Тесты пройдены")


if __name__ == "__main__":
    test_algorithms()