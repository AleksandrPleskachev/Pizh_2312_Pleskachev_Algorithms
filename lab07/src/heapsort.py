"""
Пирамидальная сортировка (Heapsort)
"""

from heap import MinHeap

def heapsort(array):
    """
    Сортировка кучей (Heapsort) с использованием MinHeap.
    Сложность: O(n log n)
    """
    # Создаем кучу из массива
    heap = MinHeap()
    heap.build_heap(array)
    
    # Извлекаем элементы по одному - они будут идти в порядке возрастания
    sorted_array = []
    while not heap.is_empty():
        sorted_array.append(heap.extract_min())
    
    return sorted_array

def heapsort_inplace(array):
    """
    In-place версия Heapsort (без использования дополнительной кучи).
    Модифицирует исходный массив.
    Сложность: O(n log n)
    """
    def sift_down(arr, n, i):
        """Вспомогательная функция для погружения"""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
            
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            sift_down(arr, n, largest)
    
    n = len(array)
    
    # Построение max-кучи (для in-place сортировки используем max-heap)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(array, n, i)
    
    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]  # Перемещаем корень в конец
        sift_down(array, i, 0)  # Восстанавливаем свойство кучи для уменьшенной кучи
    
    return array

def test_heapsort():
    """Тестирование сортировки кучей"""
    print("Тестирование Heapsort:")
    
    # Тест 1
    arr1 = [12, 11, 13, 5, 6, 7]
    print(f"Исходный массив: {arr1}")
    sorted1 = heapsort(arr1.copy())
    print(f"Отсортированный: {sorted1}")
    print(f"Правильно: {sorted1 == sorted(arr1)}")
    
    # Тест 2
    arr2 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(f"\nИсходный массив: {arr2}")
    sorted2 = heapsort_inplace(arr2.copy())
    print(f"In-place отсортированный: {sorted2}")
    print(f"Правильно: {sorted2 == sorted(arr2)}")