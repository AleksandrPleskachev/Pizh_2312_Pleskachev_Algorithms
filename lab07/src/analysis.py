"""
Анализ производительности кучи
"""

import time
import random
import sys
from heap import MinHeap
from heapsort import heapsort, heapsort_inplace

def test_heap_operations():
    """Тестирование основных операций кучи"""
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ОСНОВНЫХ ОПЕРАЦИЙ КУЧИ")
    print("=" * 60)
    
    heap = MinHeap()
    
    print("1. Вставка элементов: 5, 3, 8, 1, 2")
    for num in [5, 3, 8, 1, 2]:
        heap.insert(num)
        print(f"   После вставки {num}: {heap.heap}")
    
    print(f"\n2. Просмотр минимума: {heap.peek()}")
    
    print("\n3. Извлечение минимумов:")
    while not heap.is_empty():
        min_val = heap.extract_min()
        print(f"   Извлечен: {min_val}, осталось: {heap.heap}")
    
    print("\n4. Построение кучи из массива [9, 4, 7, 1, 3]:")
    heap.build_heap([9, 4, 7, 1, 3])
    heap.print_heap()

def measure_performance():
    """Измерение производительности операций кучи"""
    print("\n" + "=" * 60)
    print("ИЗМЕРЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ")
    print("=" * 60)
    
    sizes = [100, 500, 1000, 2000]
    
    for size in sizes:
        print(f"\nРазмер данных: {size}")
        print("-" * 40)
        
        # Генерируем случайные данные
        data = [random.randint(1, 10000) for _ in range(size)]
        
        # Тест 1: Построение кучи методом последовательной вставки
        heap1 = MinHeap()
        start = time.perf_counter()
        for item in data:
            heap1.insert(item)
        time_insert = time.perf_counter() - start
        
        # Тест 2: Построение кучи методом build_heap
        heap2 = MinHeap()
        start = time.perf_counter()
        heap2.build_heap(data)
        time_build = time.perf_counter() - start
        
        print(f"  Последовательная вставка: {time_insert:.6f} сек")
        print(f"  Метод build_heap:        {time_build:.6f} сек")
        print(f"  Отношение:               {time_insert/time_build:.2f}x")
        
        # Тест 3: Извлечение всех элементов
        start = time.perf_counter()
        while not heap1.is_empty():
            heap1.extract_min()
        time_extract = time.perf_counter() - start
        print(f"  Извлечение всех:         {time_extract:.6f} сек")

def compare_sorts():
    """Сравнение Heapsort с встроенной сортировкой"""
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ АЛГОРИТМОВ СОРТИРОВКИ")
    print("=" * 60)
    
    sizes = [100, 500, 1000]
    
    for size in sizes:
        print(f"\nРазмер массива: {size}")
        print("-" * 40)
        
        data = [random.randint(1, 10000) for _ in range(size)]
        
        # Heapsort (наша реализация)
        start = time.perf_counter()
        sorted1 = heapsort(data.copy())
        time_heap = time.perf_counter() - start
        
        # In-place Heapsort
        data_copy = data.copy()
        start = time.perf_counter()
        heapsort_inplace(data_copy)
        time_heap_inplace = time.perf_counter() - start
        
        # Встроенная сортировка Python (Timsort)
        start = time.perf_counter()
        sorted_builtin = sorted(data)
        time_builtin = time.perf_counter() - start
        
        # Проверка корректности
        correct = (sorted1 == sorted_builtin) and (data_copy == sorted_builtin)
        
        print(f"  Heapsort:          {time_heap:.6f} сек")
        print(f"  Heapsort (in-place): {time_heap_inplace:.6f} сек")
        print(f"  Встроенная сортировка: {time_builtin:.6f} сек")
        print(f"  Корректность:      {'✓' if correct else '✗'}")
        
        # Отношение времени
        if time_builtin > 0:
            ratio = time_heap / time_builtin
            print(f"  Heapsort медленнее в: {ratio:.1f}x")

def generate_graphs():
    """Генерация графиков производительности"""
    print("\n" + "="*60)
    print("ГЕНЕРАЦИЯ ГРАФИКОВ")
    print("="*60)
    
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        
        # Массивы для хранения времени
        insert_times = []
        build_times = []
        extract_times = []
        heapsort_times = []
        
        print("Провожу замеры для графиков...")
        
        for size in sizes:
            print(f"  Размер {size}...", end=" ")
            
            # Генерируем данные
            data = [random.randint(1, 10000) for _ in range(size)]
            
            # 1. Последовательная вставка
            heap = MinHeap()
            start = time.perf_counter()
            for item in data:
                heap.insert(item)
            insert_times.append(time.perf_counter() - start)
            
            # 2. Построение через build_heap
            heap = MinHeap()
            start = time.perf_counter()
            heap.build_heap(data)
            build_times.append(time.perf_counter() - start)
            
            # 3. Извлечение всех элементов
            start = time.perf_counter()
            while not heap.is_empty():
                heap.extract_min()
            extract_times.append(time.perf_counter() - start)
            
            # 4. Heapsort
            start = time.perf_counter()
            heapsort(data.copy())
            heapsort_times.append(time.perf_counter() - start)
            
            print("готово")
        
        # Создаем графики
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # График 1: Вставка vs BuildHeap
        ax1 = axes[0, 0]
        ax1.plot(sizes, insert_times, 'b-', linewidth=2, label='Последовательная вставка')
        ax1.plot(sizes, build_times, 'r-', linewidth=2, label='Метод build_heap')
        ax1.set_xlabel('Размер данных (n)')
        ax1.set_ylabel('Время (секунды)')
        ax1.set_title('Построение кучи: O(n log n) vs O(n)')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        
        # График 2: Извлечение всех элементов
        ax2 = axes[0, 1]
        ax2.plot(sizes, extract_times, 'g-', linewidth=2)
        ax2.set_xlabel('Размер данных (n)')
        ax2.set_ylabel('Время (секунды)')
        ax2.set_title('Извлечение всех элементов: O(n log n)')
        ax2.grid(True, alpha=0.3)
        
        # График 3: Heapsort
        ax3 = axes[1, 0]
        ax3.plot(sizes, heapsort_times, 'm-', linewidth=2)
        ax3.set_xlabel('Размер данных (n)')
        ax3.set_ylabel('Время (секунды)')
        ax3.set_title('Heapsort: O(n log n)')
        ax3.grid(True, alpha=0.3)
        
        # График 4: Все операции вместе (логарифмическая шкала)
        ax4 = axes[1, 1]
        x_log = np.log(sizes)
        ax4.plot(x_log, np.log(insert_times), 'b-', label='Вставка', linewidth=2)
        ax4.plot(x_log, np.log(build_times), 'r-', label='BuildHeap', linewidth=2)
        ax4.plot(x_log, np.log(extract_times), 'g-', label='Извлечение', linewidth=2)
        ax4.plot(x_log, np.log(heapsort_times), 'm-', label='Heapsort', linewidth=2)
        ax4.set_xlabel('log(n)')
        ax4.set_ylabel('log(Время)')
        ax4.set_title('Логарифмическая шкала (для проверки сложности)')
        ax4.grid(True, alpha=0.3)
        ax4.legend()
        
        plt.suptitle('Анализ производительности операций с кучей', fontsize=14, fontweight='bold')
        plt.tight_layout()
        
        # Сохраняем график
        filename = 'heap_performance.png'
        plt.savefig(filename, dpi=100, bbox_inches='tight')
        print(f"\n✓ Графики сохранены как '{filename}'")
        
        # Таблица с данными
        print("\nТАБЛИЦА ДАННЫХ ДЛЯ ГРАФИКОВ:")
        print("Размер | Вставка(сек) | BuildHeap(сек) | Извлечение(сек) | Heapsort(сек)")
        print("-" * 80)
        for i, size in enumerate(sizes):
            print(f"{size:6} | {insert_times[i]:12.6f} | {build_times[i]:13.6f} | "
                  f"{extract_times[i]:14.6f} | {heapsort_times[i]:11.6f}")
        
        # Анализ сложности
        print("\nАНАЛИЗ СЛОЖНОСТИ:")
        print("-" * 40)
        
        # Проверяем O(n) vs O(n log n) для build_heap vs вставки
        ratio_last = insert_times[-1] / build_times[-1]
        print(f"build_heap быстрее вставки в: {ratio_last:.1f} раз (для n=1000)")
        
        # Проверяем рост Heapsort
        if len(heapsort_times) >= 3:
            n1, n2 = sizes[2], sizes[-1]
            t1, t2 = heapsort_times[2], heapsort_times[-1]
            # Теоретическое отношение: (n2*log(n2)) / (n1*log(n1))
            theory_ratio = (n2 * np.log2(n2)) / (n1 * np.log2(n1))
            actual_ratio = t2 / t1
            print(f"Heapsort: отношение времени ({n2}/{n1}): теоретическое {theory_ratio:.1f}x, фактическое {actual_ratio:.1f}x")
        
        # Показываем график
        try:
            plt.show()
        except:
            print("\n⚠ График сохранен в файл, но не может быть отображен")
            print("Файл: heap_performance.png")
    
    except ImportError:
        print("⚠ Matplotlib не установлен. Графики не будут построены.")
        print("Установите: pip install matplotlib numpy")

# Добавь вызов в main() после compare_sorts():
def main():
    """Основная функция"""
    
    # Часть 1: Демонстрация работы кучи
    test_heap_operations()
    
    # Часть 2: Производительность
    measure_performance()
    
    # Часть 3: Сортировка
    compare_sorts()
    
    # Часть 4: Графики
    generate_graphs()  # <-- ДОБАВЬ ЭТУ СТРОЧКУ
    
    # Часть 5: Теория
    print("\n" + "=" * 60)
    print("ТЕОРЕТИЧЕСКИЙ АНАЛИЗ")
    print("=" * 60)

if __name__ == "__main__":
    main()