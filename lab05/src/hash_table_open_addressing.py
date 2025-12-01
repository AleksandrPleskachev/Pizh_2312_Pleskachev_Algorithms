def simple_hash(key, table_size):
    """
    Простая хеш-функция для строк
    (Дублируем здесь чтобы не было проблем с импортом)
    """
    hash_value = 0
    for char in str(key):
        hash_value += ord(char)
    return hash_value % table_size


class HashTableOpenAddressing:
    """
    Хеш-таблица с открытой адресацией (линейное пробирование)
    Сложность операций в среднем случае: O(1/(1-α))
    Сложность в худшем случае: O(n)
    """
    
    def __init__(self, capacity=10):
        self.capacity = capacity  # Размер таблицы
        self.size = 0  # Количество элементов
        self.table = [None] * capacity  # Основная таблица
        self.DELETED = "DELETED"  # Маркер удаленного элемента
    
    def _hash(self, key):
        """Вычисление хеша для ключа"""
        return simple_hash(str(key), self.capacity)
    
    def _linear_probe(self, hash_val, i):
        """Линейное пробирование"""
        return (hash_val + i) % self.capacity
    
    def insert(self, key, value):
        """
        Вставка элемента в таблицу
        Средняя сложность: O(1/(1-α))
        """
        # Проверяем нужно ли увеличивать таблицу
        if self.size >= self.capacity * 0.7:  # При 70% заполнения
            self._resize()
        
        index = self._hash(key)
        
        # Линейное пробирование для поиска свободной ячейки
        for i in range(self.capacity):
            probe_index = self._linear_probe(index, i)
            
            # Если ячейка пуста или содержит DELETED
            if self.table[probe_index] is None or self.table[probe_index] == self.DELETED:
                self.table[probe_index] = (key, value)
                self.size += 1
                return True
            
            # Если ключ уже существует - обновляем значение
            if self.table[probe_index][0] == key:
                self.table[probe_index] = (key, value)
                return True
        
        # Если не нашли свободную ячейку (должно быть редко)
        self._resize()
        return self.insert(key, value)  # Пробуем снова после ресайза
    
    def search(self, key):
        """
        Поиск элемента по ключу
        Средняя сложность: O(1/(1-α))
        """
        index = self._hash(key)
        
        # Линейное пробирование
        for i in range(self.capacity):
            probe_index = self._linear_probe(index, i)
            
            # Если ячейка пуста - ключ не найден
            if self.table[probe_index] is None:
                return None
            
            # Если нашли DELETED - продолжаем поиск
            if self.table[probe_index] == self.DELETED:
                continue
            
            # Если нашли ключ
            if self.table[probe_index][0] == key:
                return self.table[probe_index][1]
        
        return None  # Ключ не найден
    
    def delete(self, key):
        """
        Удаление элемента по ключу
        Средняя сложность: O(1/(1-α))
        """
        index = self._hash(key)
        
        # Линейное пробирование
        for i in range(self.capacity):
            probe_index = self._linear_probe(index, i)
            
            # Если ячейка пуста - ключ не найден
            if self.table[probe_index] is None:
                return False
            
            # Если нашли DELETED - продолжаем поиск
            if self.table[probe_index] == self.DELETED:
                continue
            
            # Если нашли ключ - помечаем как удаленный
            if self.table[probe_index][0] == key:
                self.table[probe_index] = self.DELETED
                self.size -= 1
                return True
        
        return False  # Ключ не найден
    
    def _resize(self):
        """Увеличение размера таблицы при переполнении"""
        print(f"  Ресайз таблицы: {self.capacity} -> {self.capacity * 2}")
        
        old_table = self.table
        old_capacity = self.capacity
        
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0
        
        # Перехеширование всех элементов
        for item in old_table:
            if item is not None and item != self.DELETED:
                key, value = item
                self.insert(key, value)
    
    def get_load_factor(self):
        """Коэффициент заполнения таблицы"""
        return self.size / self.capacity
    
    def display(self):
        """Вывод содержимого таблицы"""
        print("\nСОДЕРЖАНИЕ ХЕШ-ТАБЛИЦЫ (открытая адресация):")
        print("=" * 50)
        print(f"Размер: {self.size}/{self.capacity}")
        print(f"Коэф. заполнения: {self.get_load_factor():.2f}")
        
        for i in range(min(self.capacity, 20)):  # Показываем первые 20 ячеек
            if self.table[i] is None:
                print(f"[{i}]: пусто")
            elif self.table[i] == self.DELETED:
                print(f"[{i}]: УДАЛЕНО")
            else:
                key, value = self.table[i]
                print(f"[{i}]: {key} -> {value}")
        
        if self.capacity > 20:
            print(f"... и еще {self.capacity - 20} ячеек")


def compare_methods():
    """Сравнение метода цепочек и открытой адресации"""
    print("СРАВНЕНИЕ МЕТОДОВ РАЗРЕШЕНИЯ КОЛЛИЗИЙ")
    print("=" * 60)
    
    import time
    
    # Тестовые данные
    test_data = [
        ("apple", "red"),
        ("banana", "yellow"),
        ("orange", "orange"),
        ("grape", "purple"),
        ("kiwi", "green"),
        ("melon", "green"),
        ("strawberry", "red"),
        ("blueberry", "blue"),
        ("peach", "orange"),
        ("pear", "green"),
        ("mango", "yellow"),
        ("pineapple", "brown"),
        ("watermelon", "green"),
        ("cherry", "red"),
        ("plum", "purple")
    ]
    
    # Метод цепочек
    print("\n1. МЕТОД ЦЕПОЧЕК:")
    from hash_table_chaining import HashTableChaining
    
    ht_chain = HashTableChaining(capacity=10)
    
    start = time.time()
    for key, value in test_data:
        ht_chain.insert(key, value)
    chain_insert_time = time.time() - start
    
    start = time.time()
    for key, _ in test_data:
        ht_chain.search(key)
    chain_search_time = time.time() - start
    
    print(f"   Вставка: {chain_insert_time:.6f} сек")
    print(f"   Поиск:   {chain_search_time:.6f} сек")
    print(f"   Коэф. заполнения: {ht_chain.get_load_factor():.2f}")
    
    # Открытая адресация
    print("\n2. ОТКРЫТАЯ АДРЕСАЦИЯ:")
    ht_open = HashTableOpenAddressing(capacity=10)
    
    start = time.time()
    for key, value in test_data:
        ht_open.insert(key, value)
    open_insert_time = time.time() - start
    
    start = time.time()
    for key, _ in test_data:
        ht_open.search(key)
    open_search_time = time.time() - start
    
    print(f"   Вставка: {open_insert_time:.6f} сек")
    print(f"   Поиск:   {open_search_time:.6f} сек")
    print(f"   Коэф. заполнения: {ht_open.get_load_factor():.2f}")
    
    # Сравнение (с проверкой деления на ноль)
    print("\nСРАВНЕНИЕ РЕЗУЛЬТАТОВ:")
    
    if open_insert_time > 0:
        ratio_insert = chain_insert_time / open_insert_time
        print(f"   Вставка: цепочки/открытая = {ratio_insert:.2f}")
    else:
        print(f"   Вставка: открытая адресация слишком быстрая (< 0.000001 сек)")
    
    if open_search_time > 0:
        ratio_search = chain_search_time / open_search_time
        print(f"   Поиск:   цепочки/открытая = {ratio_search:.2f}")
    else:
        print(f"   Поиск:   открытая адресация слишком быстрая (< 0.000001 сек)")


def test_open_addressing():
    """Тестирование открытой адресации"""
    print("🧪 ТЕСТИРОВАНИЕ ОТКРЫТОЙ АДРЕСАЦИИ")
    print("=" * 50)
    
    # Создаем таблицу
    ht = HashTableOpenAddressing(capacity=5)
    
    # Вставляем элементы
    print("\nДобавляем элементы:")
    test_data = [
        ("apple", 10),
        ("banana", 20),
        ("orange", 30),
        ("grape", 40),
        ("kiwi", 50)
    ]
    
    for key, value in test_data:
        ht.insert(key, value)
        print(f"  {key}: {value}")
    
    # Показываем таблицу
    ht.display()
    
    # Поиск элементов
    print("\nПОИСК ЭЛЕМЕНТОВ:")
    search_keys = ["apple", "banana", "cherry"]
    for key in search_keys:
        value = ht.search(key)
        if value is not None:
            print(f"  {key} найден: {value}")
        else:
            print(f"  {key} не найден")
    
    # Удаление элемента
    print("\nУДАЛЕНИЕ ЭЛЕМЕНТА:")
    delete_key = "orange"
    if ht.delete(delete_key):
        print(f"  {delete_key} удален")
    else:
        print(f"  {delete_key} не найден для удаления")
    
    ht.display()
    
    # Проверка поиска после удаления
    print("\nПОИСК ПОСЛЕ УДАЛЕНИЯ:")
    value = ht.search("orange")
    if value is not None:
        print(f"  orange найден: {value}")
    else:
        print(f"  orange не найден (правильно!)")
    
    # Попробуем добавить еще элементов чтобы вызвать ресайз
    print("\n➕ ДОБАВЛЕНИЕ ДОПОЛНИТЕЛЬНЫХ ЭЛЕМЕНТОВ:")
    extra_data = [
        ("melon", 60),
        ("peach", 70),
        ("pear", 80),
        ("berry", 90)
    ]
    
    for key, value in extra_data:
        ht.insert(key, value)
        print(f"  {key}: {value}")
    
    ht.display()


def test_automatic_resize():
    """Тест автоматического увеличения таблицы"""
    print("\nТЕСТ АВТОМАТИЧЕСКОГО УВЕЛИЧЕНИЯ ТАБЛИЦЫ")
    print("=" * 50)
    
    ht = HashTableOpenAddressing(capacity=5)
    
    print(f"Начальный размер: {ht.capacity}")
    print("Добавляем элементы до заполнения 70%...")
    
    # Добавляем элементы пока не сработает ресайз
    for i in range(10):
        key = f"key_{i}"
        value = f"value_{i}"
        ht.insert(key, value)
        print(f"  Добавлен {key}, размер: {ht.size}/{ht.capacity}")
    
    print(f"\nИтоговый размер: {ht.capacity}")


if __name__ == "__main__":
    test_open_addressing()
    print("\n")
    test_automatic_resize()
    print("\n")
    compare_methods()