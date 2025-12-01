class Node:
    """Узел для метода цепочек"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTableChaining:
    """
    Хеш-таблица с методом цепочек
    Сложность операций в среднем случае: O(1 + α), где α = n/m
    Сложность в худшем случае: O(n)
    """
    
    def __init__(self, capacity=10):
        self.capacity = capacity  # Размер таблицы
        self.size = 0  # Количество элементов
        self.table = [None] * capacity  # Основная таблица
    
    def _hash(self, key):
        """Вычисление хеша для ключа"""
        from hash_functions import simple_hash
        return simple_hash(key, self.capacity)
    
    def insert(self, key, value):
        """
        Вставка элемента в таблицу
        Средняя сложность: O(1 + α)
        """
        index = self._hash(key)
        
        # Если ячейка пуста
        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
            return True
        
        # Если ячейка занята - идем по цепочке
        current = self.table[index]
        while current:
            # Если ключ уже существует - обновляем значение
            if current.key == key:
                current.value = value
                return True
            if current.next is None:
                break
            current = current.next
        
        # Добавляем в конец цепочки
        current.next = Node(key, value)
        self.size += 1
        return True
    
    def search(self, key):
        """
        Поиск элемента по ключу
        Средняя сложность: O(1 + α)
        """
        index = self._hash(key)
        current = self.table[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        return None  # Ключ не найден
    
    def delete(self, key):
        """
        Удаление элемента по ключу
        Средняя сложность: O(1 + α)
        """
        index = self._hash(key)
        current = self.table[index]
        prev = None
        
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return True
            prev = current
            current = current.next
        
        return False  # Ключ не найден
    
    def get_load_factor(self):
        """Коэффициент заполнения таблицы"""
        return self.size / self.capacity
    
    def display(self):
        """Вывод содержимого таблицы"""
        print("\n📋 СОДЕРЖАНИЕ ХЕШ-ТАБЛИЦЫ:")
        print("=" * 40)
        print(f"Размер: {self.size}/{self.capacity}")
        print(f"Коэф. заполнения: {self.get_load_factor():.2f}")
        
        for i in range(self.capacity):
            print(f"\nЯчейка {i}: ", end="")
            current = self.table[i]
            if current is None:
                print("пусто")
            else:
                while current:
                    print(f"[{current.key}: {current.value}]", end=" -> ")
                    current = current.next
                print("None")


def test_hash_table():
    """Тестирование хеш-таблицы"""
    print("🧪 ТЕСТИРОВАНИЕ ХЕШ-ТАБЛИЦЫ")
    print("=" * 40)
    
    # Создаем таблицу
    ht = HashTableChaining(capacity=5)
    
    # Вставляем элементы
    test_data = [
        ("apple", 10),
        ("banana", 20),
        ("orange", 30),
        ("grape", 40),
        ("kiwi", 50),
        ("melon", 60)
    ]
    
    print("Добавляем элементы:")
    for key, value in test_data:
        ht.insert(key, value)
        print(f"  {key}: {value}")
    
    # Показываем таблицу
    ht.display()
    
    # Поиск элементов
    print("\n🔍 ПОИСК ЭЛЕМЕНТОВ:")
    search_keys = ["apple", "banana", "cherry"]
    for key in search_keys:
        value = ht.search(key)
        if value is not None:
            print(f"  {key} найден: {value}")
        else:
            print(f"  {key} не найден")
    
    # Удаление элемента
    print("\n🗑️ УДАЛЕНИЕ ЭЛЕМЕНТА:")
    delete_key = "orange"
    if ht.delete(delete_key):
        print(f"  {delete_key} удален")
    else:
        print(f"  {delete_key} не найден для удаления")
    
    ht.display()


def measure_performance():
    """Измерение производительности"""
    print("\n⏱️ ИЗМЕРЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ")
    print("=" * 40)
    
    import time
    
    ht = HashTableChaining(capacity=100)
    
    # Вставка
    print("Тест вставки 100 элементов:")
    start = time.time()
    for i in range(100):
        ht.insert(f"key_{i}", f"value_{i}")
    insert_time = time.time() - start
    print(f"  Время: {insert_time:.6f} сек")
    print(f"  Коэф. заполнения: {ht.get_load_factor():.2f}")
    
    # Поиск
    print("\nТест поиска 50 элементов:")
    start = time.time()
    for i in range(0, 100, 2):
        ht.search(f"key_{i}")
    search_time = time.time() - start
    print(f"  Время: {search_time:.6f} сек")
    
    # Удаление
    print("\nТест удаления 50 элементов:")
    start = time.time()
    for i in range(0, 100, 2):
        ht.delete(f"key_{i}")
    delete_time = time.time() - start
    print(f"  Время: {delete_time:.6f} сек")
    print(f"  Итоговый размер: {ht.size}")


if __name__ == "__main__":
    test_hash_table()
    measure_performance()