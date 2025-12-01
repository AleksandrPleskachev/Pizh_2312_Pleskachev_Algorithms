def bubble_sort(arr):
    """
    Сортировка пузырьком
    Временная сложность:
      - Лучший: O(n) - уже отсортирован
      - Средний: O(n²)
      - Худший: O(n²) - обратно отсортирован
    Пространственная сложность: O(1)
    """
    n = len(arr)
    # Проходим по массиву n-1 раз
    for i in range(n):
        swapped = False
        # Сравниваем соседние элементы
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Меняем местами если нужно
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если не было обменов - массив отсортирован
        if not swapped:
            break
    return arr


def selection_sort(arr):
    """
    Сортировка выбором
    Временная сложность:
      - Лучший: O(n²)
      - Средний: O(n²)
      - Худший: O(n²)
    Пространственная сложность: O(1)
    """
    n = len(arr)
    for i in range(n):
        # Ищем минимальный элемент в неотсортированной части
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Меняем местами с текущим элементом
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    """
    Сортировка вставками
    Временная сложность:
      - Лучший: O(n) - уже отсортирован
      - Средний: O(n²)
      - Худший: O(n²) - обратно отсортирован
    Пространственная сложность: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Сдвигаем элементы больше key вправо
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Вставляем key на правильное место
        arr[j + 1] = key
    return arr


def test_sorts():
    """Тестирование алгоритмов сортировки"""
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1, 2, 3, 4, 5],  # Уже отсортирован
        [5, 4, 3, 2, 1],  # Обратный порядок
    ]
    
    print("ТЕСТИРОВАНИЕ АЛГОРИТМОВ СОРТИРОВКИ")
    print("=" * 40)
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"\nТест {i}: {arr}")
        
        # Создаем копии для каждого алгоритма
        arr1 = arr.copy()
        arr2 = arr.copy()
        arr3 = arr.copy()
        
        print(f"Пузырьком:    {bubble_sort(arr1)}")
        print(f"Выбором:      {selection_sort(arr2)}")
        print(f"Вставками:    {insertion_sort(arr3)}")


if __name__ == "__main__":
    test_sorts()