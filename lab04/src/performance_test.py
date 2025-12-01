import time
import random
from sorts import bubble_sort, selection_sort, insertion_sort


def generate_random_array(size):
    """Генерация случайного массива"""
    return [random.randint(1, 1000) for _ in range(size)]


def measure_sort_time(sort_func, arr):
    """Измерение времени сортировки"""
    arr_copy = arr.copy()  # Создаем копию чтобы не менять оригинал
    start_time = time.time()
    sort_func(arr_copy)
    end_time = time.time()
    return end_time - start_time


def run_performance_test():
    """Запуск тестов производительности"""
    sizes = [100, 500, 1000]
    
    print("⏱ТЕСТ ПРОИЗВОДИТЕЛЬНОСТИ СОРТИРОВОК")
    print("=" * 50)
    
    for size in sizes:
        print(f"\nРазмер массива: {size} элементов")
        print("-" * 30)
        
        # Генерируем случайный массив
        random_array = generate_random_array(size)
        
        # Замеряем время для каждого алгоритма
        time_bubble = measure_sort_time(bubble_sort, random_array)
        time_selection = measure_sort_time(selection_sort, random_array)
        time_insertion = measure_sort_time(insertion_sort, random_array)
        
        print(f"Сортировка пузырьком: {time_bubble:.6f} сек")
        print(f"Сортировка выбором:   {time_selection:.6f} сек")
        print(f"Сортировка вставками: {time_insertion:.6f} сек")
        
        # Находим самый быстрый
        times = [time_bubble, time_selection, time_insertion]
        fastest = min(times)
        fastest_idx = times.index(fastest)
        algorithms = ["Пузырьком", "Выбором", "Вставками"]
        
        print(f"Самый быстрый: {algorithms[fastest_idx]}")


def test_worst_case():
    """Тестирование худшего случая (обратно отсортированный массив)"""
    print("\nТЕСТИРОВАНИЕ ХУДШЕГО СЛУЧАЯ")
    print("=" * 40)
    
    size = 500
    # Создаем массив в обратном порядке
    reversed_array = list(range(size, 0, -1))
    
    time_bubble = measure_sort_time(bubble_sort, reversed_array)
    time_selection = measure_sort_time(selection_sort, reversed_array)
    time_insertion = measure_sort_time(insertion_sort, reversed_array)
    
    print(f"Массив {size} элементов в обратном порядке:")
    print(f"Пузырьком:    {time_bubble:.6f} сек")
    print(f"Выбором:      {time_selection:.6f} сек")
    print(f"Вставками:    {time_insertion:.6f} сек")


def test_best_case():
    """Тестирование лучшего случая (уже отсортированный массив)"""
    print("\nТЕСТИРОВАНИЕ ЛУЧШЕГО СЛУЧАЯ")
    print("=" * 40)
    
    size = 500
    # Создаем уже отсортированный массив
    sorted_array = list(range(1, size + 1))
    
    time_bubble = measure_sort_time(bubble_sort, sorted_array)
    time_selection = measure_sort_time(selection_sort, sorted_array)
    time_insertion = measure_sort_time(insertion_sort, sorted_array)
    
    print(f"Массив {size} элементов уже отсортирован:")
    print(f"Пузырьком:    {time_bubble:.6f} сек")
    print(f"Выбором:      {time_selection:.6f} сек")
    print(f"Вставками:    {time_insertion:.6f} сек")


if __name__ == "__main__":
    run_performance_test()
    test_worst_case()
    test_best_case()