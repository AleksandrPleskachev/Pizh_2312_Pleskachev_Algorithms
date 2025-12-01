def simple_hash(key, table_size):
    """
    Простая хеш-функция для строк
    Сложность: O(n) где n - длина строки
    Особенность: простая, но плохое распределение для похожих строк
    """
    hash_value = 0
    for char in key:
        hash_value += ord(char)  # Сумма кодов символов
    return hash_value % table_size  # Приводим к размеру таблицы


def test_hash_functions():
    """Тестирование хеш-функции"""
    print("ТЕСТ ХЕШ-ФУНКЦИИ")
    print("=" * 40)
    
    table_size = 10
    test_keys = ["apple", "banana", "orange", "grape", "kiwi", "melon"]
    
    print(f"Размер таблицы: {table_size}")
    print("Ключи и их хеши:")
    
    for key in test_keys:
        hash_val = simple_hash(key, table_size)
        print(f"  '{key}' -> {hash_val}")
    
    # Проверка коллизий
    print("\nПРОВЕРКА КОЛЛИЗИЙ:")
    hash_counts = {}
    for key in test_keys:
        hash_val = simple_hash(key, table_size)
        if hash_val in hash_counts:
            hash_counts[hash_val].append(key)
        else:
            hash_counts[hash_val] = [key]
    
    collisions = 0
    for hash_val, keys in hash_counts.items():
        if len(keys) > 1:
            print(f"  Коллизия в ячейке {hash_val}: {keys}")
            collisions += len(keys) - 1
    
    print(f"\nВсего ключей: {len(test_keys)}")
    print(f"Коллизий: {collisions}")
    print(f"Коэффициент коллизий: {collisions/len(test_keys):.2f}")


if __name__ == "__main__":
    test_hash_functions()