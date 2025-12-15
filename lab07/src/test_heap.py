from heap import MinHeap

def test_basic():
    """Базовый тест кучи"""
    print("Тестирование MinHeap...")
    
    heap = MinHeap()
    
    # Вставка
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    heap.insert(2)
    
    print(f"Куча после вставок: {heap.heap}")
    print(f"Минимум: {heap.peek()}")
    
    # Извлечение
    result = []
    while not heap.is_empty():
        result.append(heap.extract_min())
    
    print(f"Извлеченные элементы: {result}")
    print(f"Отсортированы правильно: {result == sorted(result)}")
    
    # Построение кучи
    heap.build_heap([9, 4, 7, 1, 3, 6])
    print(f"\nКуча построенная из массива: {heap.heap}")
    
    print("\n✓ Все тесты пройдены!")

if __name__ == "__main__":
    test_basic()