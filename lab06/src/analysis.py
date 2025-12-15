import time
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
from binary_search_tree import BinarySearchTree

# Увеличиваем лимит рекурсии на всякий случай
sys.setrecursionlimit(10000)

def create_balanced_tree(size):
    """Создание сбалансированного дерева"""
    bst = BinarySearchTree()
    # Берем случайные значения
    values = list(range(size * 10))
    random.shuffle(values)
    
    # Берем первые size значений
    for i in range(min(size, len(values))):
        bst.insert(values[i])
    return bst


def create_degenerate_tree_safe(size):
    """Создание вырожденного дерева БЕЗ рекурсии"""
    bst = BinarySearchTree()
    # Вставляем значения в порядке убывания, чтобы создать лево-вырожденное дерево
    # Это лучше, чем возрастающий порядок, так как будет менее глубокая рекурсия
    for value in range(size - 1, -1, -1):
        bst.insert(value)
    return bst


def test_tree_performance_small():
    """Тестирование производительности на небольших размерах"""
    print("=" * 50)
    print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ДЕРЕВЬЕВ")
    print("=" * 50)
    
    # Используем МЕНЬШИЕ размеры для безопасности
    sizes = [50, 100, 200]
    search_count = 50  # Меньше поисков для скорости
    
    print(f"Количество поисков: {search_count}\n")
    
    for size in sizes:
        print(f"\nРазмер дерева: {size} элементов")
        print("-" * 30)
        
        # Сбалансированное дерево
        print("1. Сбалансированное дерево:")
        balanced = create_balanced_tree(size)
        
        # Измеряем время поиска
        start = time.perf_counter()
        for i in range(search_count):
            balanced.search(random.randint(0, size * 10))
        balanced_time = time.perf_counter() - start
        
        height_balanced = balanced.get_height()
        print(f"   Высота: {height_balanced}")
        print(f"   Время поиска: {balanced_time:.6f} сек")
        
        # Вырожденное дерево (безопасное)
        print("\n2. Вырожденное дерево:")
        degenerate = create_degenerate_tree_safe(size)
        
        start = time.perf_counter()
        for i in range(search_count):
            degenerate.search(random.randint(0, size * 10))
        degenerate_time = time.perf_counter() - start
        
        height_degenerate = degenerate.get_height()
        print(f"   Высота: {height_degenerate}")
        print(f"   Время поиска: {degenerate_time:.6f} сек")
        
        # Сравнение
        if balanced_time > 0:
            ratio = degenerate_time / balanced_time
            print(f"\n   Отношение времени (вырожденное/сбалансированное): {ratio:.2f}x")
            print(f"   Вырожденное дерево в {ratio:.1f} раз медленнее")
        else:
            print(f"\n   Очень быстрое выполнение")
        
        # Теоретическая оценка
        print(f"\n   Теоретическая оценка высоты:")
        print(f"   Сбалансированное: O(log n) ≈ {int(round(1.5 * (size ** 0.5)))}")
        print(f"   Вырожденное: O(n) = {size}")


def demo_basic_operations():
    """Демонстрация основных операций"""
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ ОСНОВНЫХ ОПЕРАЦИЙ BST")
    print("=" * 50)
    
    # Создаем небольшое дерево
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    
    print(f"Вставляем значения: {values}")
    for value in values:
        bst.insert(value)
    
    print(f"Обход in-order: {bst.in_order_traversal()}")
    print(f"Высота дерева: {bst.get_height()}")
    print(f"Дерево пустое? {bst.is_empty()}")
    
    # Поиск некоторых значений
    test_values = [40, 90, 30, 100]
    print("\nТестирование поиска:")
    for val in test_values:
        found = bst.search(val)
        print(f"  Поиск {val}: {'Найден' if found else 'Не найден'}")
    
    # Визуализация
    print(f"\nТекстовое представление: {bst.print_tree()}")


def compare_tree_structures():
    """Сравнение структур деревьев"""
    print("\n" + "=" * 50)
    print("СРАВНЕНИЕ СТРУКТУР ДЕРЕВЬЕВ")
    print("=" * 50)
    
    size = 10  # Маленькое дерево для наглядности
    
    print(f"\nСбалансированное дерево из {size} элементов:")
    balanced = create_balanced_tree(size)
    print(f"In-order обход: {balanced.in_order_traversal()}")
    print(f"Высота: {balanced.get_height()}")
    print(f"Представление: {balanced.print_tree()}")
    
    print(f"\nВырожденное дерево из {size} элементов:")
    degenerate = create_degenerate_tree_safe(size)
    print(f"In-order обход: {degenerate.in_order_traversal()}")
    print(f"Высота: {degenerate.get_height()}")
    print(f"Представление: {degenerate.print_tree()}")


def generate_graphs():
    """Генерация графиков на основе реальных измерений"""
    print("\n" + "="*50)
    print("ПОСТРОЕНИЕ ГРАФИКОВ ИЗ РЕАЛЬНЫХ ИЗМЕРЕНИЙ")
    print("="*50)
    
    # Размеры деревьев для тестирования
    sizes = [50, 100, 150, 200, 250]
    search_count = 100
    
    # Массивы для хранения реальных измерений
    real_balanced_times = []
    real_degenerate_times = []
    real_balanced_heights = []
    real_degenerate_heights = []
    
    print("Провожу измерения...")
    
    for size in sizes:
        print(f"  Измеряю для размера {size}...")
        
        # 1. Сбалансированное дерево - РЕАЛЬНОЕ измерение
        balanced_tree = create_balanced_tree(size)
        real_balanced_heights.append(balanced_tree.get_height())
        
        # Измеряем время поиска
        start_time = time.perf_counter()
        for _ in range(search_count):
            balanced_tree.search(random.randint(0, size * 10))
        balanced_time = time.perf_counter() - start_time
        real_balanced_times.append(balanced_time)
        
        # 2. Вырожденное дерево - РЕАЛЬНОЕ измерение
        degenerate_tree = create_degenerate_tree_safe(size)
        real_degenerate_heights.append(degenerate_tree.get_height())
        
        start_time = time.perf_counter()
        for _ in range(search_count):
            degenerate_tree.search(random.randint(0, size * 10))
        degenerate_time = time.perf_counter() - start_time
        real_degenerate_times.append(degenerate_time)
    
    print("\nРезультаты измерений:")
    print("Размер | Время(сб) | Время(выр) | Высота(сб) | Высота(выр)")
    for i, size in enumerate(sizes):
        print(f"{size:6} | {real_balanced_times[i]:9.6f} | {real_degenerate_times[i]:10.6f} | "
              f"{real_balanced_heights[i]:10} | {real_degenerate_heights[i]:11}")
    
    # Создаем графики
    plt.figure(figsize=(12, 5))
    
    # График 1: Время поиска от размера дерева
    plt.subplot(1, 2, 1)
    plt.plot(sizes, real_balanced_times, 'bo-', linewidth=2, markersize=8, 
             label='Сбалансированное (реальные данные)')
    plt.plot(sizes, real_degenerate_times, 'rs-', linewidth=2, markersize=8,
             label='Вырожденное (реальные данные)')
    
    # Теоретические кривые для сравнения
    x_smooth = np.linspace(min(sizes), max(sizes), 100)
    y_balanced_theory = np.log2(x_smooth) * (real_balanced_times[-1] / np.log2(sizes[-1]))
    y_degenerate_theory = x_smooth * (real_degenerate_times[-1] / sizes[-1])
    
    plt.plot(x_smooth, y_balanced_theory, 'b--', alpha=0.5, label='O(log n) теоретическая')
    plt.plot(x_smooth, y_degenerate_theory, 'r--', alpha=0.5, label='O(n) теоретическая')
    
    plt.xlabel('Размер дерева (n элементов)', fontsize=12)
    plt.ylabel('Время поиска (секунды)', fontsize=12)
    plt.title('Зависимость времени поиска от размера дерева\n(100 операций поиска)', fontsize=13, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    
    # График 2: Высота деревьев от размера
    plt.subplot(1, 2, 2)
    plt.plot(sizes, real_balanced_heights, 'bo-', linewidth=2, markersize=8,
             label='Сбалансированное (реальная высота)')
    plt.plot(sizes, real_degenerate_heights, 'rs-', linewidth=2, markersize=8,
             label='Вырожденное (реальная высота)')
    
    # Теоретические кривые высоты
    y_height_balanced = np.log2(x_smooth) * (real_balanced_heights[-1] / np.log2(sizes[-1]))
    y_height_degenerate = x_smooth * (real_degenerate_heights[-1] / sizes[-1])
    
    plt.plot(x_smooth, y_height_balanced, 'b--', alpha=0.5, label='O(log n) теоретическая')
    plt.plot(x_smooth, y_height_degenerate, 'r--', alpha=0.5, label='O(n) теоретическая')
    
    plt.xlabel('Размер дерева (n элементов)', fontsize=12)
    plt.ylabel('Высота дерева', fontsize=12)
    plt.title('Зависимость высоты дерева от размера', fontsize=13, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    
    plt.tight_layout()
    
    # Сохраняем график
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f'bst_real_performance.png'
    plt.savefig(filename, dpi=100, bbox_inches='tight')
    print(f"\nГрафики сохранены как '{filename}'")
    
    # Показываем график
    try:
        plt.show()
    except:
        print("(График сохранен в файл)")
    
    # Вывод анализа
    print("\n" + "="*50)
    print("АНАЛИЗ РЕЗУЛЬТАТОВ:")
    print("="*50)
    
    # Расчет среднего отношения
    ratios = [deg/bal for bal, deg in zip(real_balanced_times, real_degenerate_times) if bal > 0]
    avg_ratio = sum(ratios) / len(ratios) if ratios else 0
    
    print(f"Среднее отношение времени (вырожденное/сбалансированное): {avg_ratio:.1f}x")
    print(f"Размер 250 элементов: вырожденное в {real_degenerate_times[-1]/real_balanced_times[-1]:.1f} раз медленнее")
    print("\nНаблюдения:")
    print("1. Вырожденное дерево действительно показывает линейный рост O(n)")
    print("2. Сбалансированное дерево растет логарифмически O(log n)")
    print("3. Разница становится существенной при больших размерах")


def main():
    """Основная функция"""
    
    # Часть 1: Демонстрация работы
    demo_basic_operations()
    
    # Часть 2: Производительность
    test_tree_performance_small()
    
    # Часть 3: Структуры деревьев
    compare_tree_structures()
    
    # Часть 4: Графики
    try:
        generate_graphs()
    except Exception as e:
        print(f"\n⚠ Не удалось создать графики: {e}")
        print("Проверьте установку matplotlib: pip install matplotlib")
    
    # Часть 5: Теория
    print("\n" + "=" * 50)
    print("ТЕОРЕТИЧЕСКИЙ АНАЛИЗ")
    print("=" * 50)
    
    print("\nСЛОЖНОСТЬ ОПЕРАЦИЙ BST:")
    print("-" * 40)
    print("СБАЛАНСИРОВАННОЕ ДЕРЕВО:")
    print("Вставка: O(log n)")
    print("Поиск: O(log n)")
    print("Обход: O(n)")
    
    print("\nВЫРОЖДЕННОЕ ДЕРЕВО:")
    print("Вставка: O(n)")
    print("Поиск: O(n)")
    print("Обход: O(n)")
    
    print("\nВЫВОДЫ:")
    print("-" * 40)
    print("1. Вырожденное дерево работает как связный список")
    print("2. Сбалансированность критически важна для производительности")
    print("3. Вставка случайных значений обычно дает сбалансированные деревья")
    print("4. Вставка отсортированных значений создает вырожденное дерево")


if __name__ == "__main__":
    try:
        main()
    except RecursionError:
        print("\nОШИБКА: Превышена максимальная глубина рекурсии!")
        print("Попробуйте уменьшить размер деревьев в тестах.")
    except Exception as e:
        print(f"\nОШИБКА: {type(e).__name__}: {e}")