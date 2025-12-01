import random

def generate_random(size):
    """Случайный массив"""
    return [random.randint(1, 10000) for _ in range(size)]

def generate_sorted(size):
    """Уже отсортированный массив"""
    return list(range(1, size + 1))

def generate_reversed(size):
    """Обратно отсортированный массив"""
    return list(range(size, 0, -1))

def generate_almost_sorted(size, percent=5):
    """Почти отсортированный массив (95% упорядочено)"""
    arr = list(range(1, size + 1))
    # Меняем местами percent% элементов
    swap_count = size * percent // 100
    for _ in range(swap_count):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def generate_test_data():
    """Создание всех тестовых данных"""
    sizes = [100, 500, 1000]
    data_types = ['random', 'sorted', 'reversed', 'almost_sorted']
    
    test_data = {}
    
    for size in sizes:
        test_data[size] = {
            'random': generate_random(size),
            'sorted': generate_sorted(size),
            'reversed': generate_reversed(size),
            'almost_sorted': generate_almost_sorted(size)
        }
    
    return test_data

def print_sample_data():
    """Вывод примеров данных для проверки"""
    print("ОБРАЗЦЫ ТЕСТОВЫХ ДАННЫХ")
    print("=" * 40)
    
    size = 10  # Маленький размер для наглядности
    
    print(f"\nСлучайный массив ({size} элементов):")
    print(generate_random(size))
    
    print(f"\nОтсортированный массив ({size} элементов):")
    print(generate_sorted(size))
    
    print(f"\nОбратно отсортированный ({size} элементов):")
    print(generate_reversed(size))
    
    print(f"\nПочти отсортированный ({size} элементов):")
    print(generate_almost_sorted(size))

if __name__ == "__main__":
    print_sample_data()