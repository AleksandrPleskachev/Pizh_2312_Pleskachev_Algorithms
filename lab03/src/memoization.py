import time
import matplotlib.pyplot as plt
from recursion import fibonacci

# Кеш для хранения вычисленных значений
fib_cache = {}

def fibonacci_memo(n):
    """
    Вычисление чисел Фибоначчи с мемоизацией
    Сложность: O(n) вместо O(2^n)
    """
    if n in fib_cache:  # Если уже вычисляли
        return fib_cache[n]
    
    if n <= 1:  # Базовый случай
        result = n
    else:  # Рекурсивный шаг
        result = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    
    fib_cache[n] = result  # Сохраняем в кеш
    return result


def compare_performance():
    """Сравнение производительности наивной и мемоизированной версий"""
    n = 30
    
    print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ")
    print("=" * 35)
    
    # Наивная версия
    start = time.time()
    fib_naive = fibonacci(n)
    time_naive = time.time() - start
    
    # Мемоизированная версия
    # Очищаем кеш перед вычислением
    global fib_cache
    fib_cache = {}
    
    start = time.time()
    fib_memo = fibonacci_memo(n)
    time_memo = time.time() - start
    
    print(f"Вычисление F({n}):")
    print(f"Наивная рекурсия: {fib_naive} (время: {time_naive:.6f} сек)")
    print(f"С мемоизацией: {fib_memo} (время: {time_memo:.6f} сек)")
    
    if time_memo > 0:
        print(f"Ускорение: {time_naive/time_memo:.1f} раз")
    else:
        print("Ускорение: очень большое (мемоизация слишком быстрая)")
    
    # Покажем размер кеша
    print(f"\nРазмер кеша: {len(fib_cache)} значений")


def demo_memoization():
    """Демонстрация работы мемоизации"""
    print("ДЕМОНСТРАЦИЯ МЕМОИЗАЦИИ")
    print("=" * 30)
    
    # Очищаем кеш
    global fib_cache
    fib_cache = {}
    
    # Первое вычисление - вычисляем все
    start = time.time()
    result1 = fibonacci_memo(25)
    time1 = time.time() - start
    print(f"Первое вычисление F(25): {time1:.6f} сек")
    
    # Второе вычисление - используем кеш
    start = time.time()
    result2 = fibonacci_memo(25)
    time2 = time.time() - start
    print(f"Повторное вычисление F(25): {time2:.6f} сек")
    
    if time2 > 0:
        print(f"Ускорение: {time1/time2:.0f} раз")
    else:
        print(f"Ускорение: мгновенное (время < 0.000001 сек)")


def build_performance_graph():
    """Построение графика сравнения производительности"""
    print("\nПОСТРОЕНИЕ ГРАФИКА")
    
    # Значения n для тестирования
    n_values = [10, 15, 20, 25, 30, 35]
    naive_times = []
    memo_times = []
    
    print("Тестирование для разных n:")
    for n in n_values:
        print(f"\nn = {n}:")
        
        # Наивная версия
        start = time.time()
        fib_naive = fibonacci(n)
        time_naive = time.time() - start
        naive_times.append(time_naive)
        print(f"  Наивная: {time_naive:.6f} сек")
        
        # Мемоизированная версия (очищаем кеш)
        global fib_cache
        fib_cache = {}
        
        start = time.time()
        fib_memo = fibonacci_memo(n)
        time_memo = time.time() - start
        memo_times.append(time_memo)
        print(f"  С мемоизацией: {time_memo:.6f} сек")
        
        if time_memo > 0:
            speedup = time_naive / time_memo
            print(f"  Ускорение: {speedup:.1f} раз")
    
    # Построение графика
    plt.figure(figsize=(10, 6))
    
    plt.plot(n_values, naive_times, 'ro-', linewidth=2, markersize=8, label='Наивная рекурсия')
    plt.plot(n_values, memo_times, 'go-', linewidth=2, markersize=8, label='С мемоизацией')
    
    plt.xlabel('n (номер числа Фибоначчи)', fontsize=12)
    plt.ylabel('Время выполнения (секунды)', fontsize=12)
    plt.title('Сравнение производительности вычисления чисел Фибоначчи', fontsize=14)
    
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Сохраняем график
    plt.savefig('fibonacci_performance.png', dpi=300, bbox_inches='tight')
    
    # Показываем график
    plt.show()
    
    # Дополнительный график в логарифмической шкале
    plt.figure(figsize=(10, 6))
    
    plt.semilogy(n_values, naive_times, 'ro-', linewidth=2, markersize=8, label='Наивная рекурсия')
    plt.semilogy(n_values, memo_times, 'go-', linewidth=2, markersize=8, label='С мемоизацией')
    
    plt.xlabel('n (номер числа Фибоначчи)', fontsize=12)
    plt.ylabel('Время выполнения (log scale)', fontsize=12)
    plt.title('Логарифмическая шкала времени выполнения', fontsize=14)
    
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig('fibonacci_performance_log.png', dpi=300, bbox_inches='tight')
    
    plt.show()


def analyze_complexity():
    """Анализ сложности алгоритмов"""
    print("\nАНАЛИЗ СЛОЖНОСТИ")
    print("=" * 40)
    
    print("1. НАИВНАЯ РЕКУРСИЯ:")
    print("   • Сложность: O(2^n)")
    print("   • Причина: Каждый вызов порождает 2 новых вызова")
    print("   • Для n=35: ~2^35 = 34 миллиарда операций")
    
    print("\n2. РЕКУРСИЯ С МЕМОИЗАЦИЕЙ:")
    print("   • Сложность: O(n)")
    print("   • Причина: Каждое значение вычисляется один раз")
    print("   • Для n=35: всего 35 операций")
    
    print("\n3. ВЫВОД:")
    print("   • Мемоизация меняет сложность с экспоненциальной на линейную")
    print("   • Ускорение растет экспоненциально с увеличением n")
    print("   • Для больших n разница в производительности огромна")


if __name__ == "__main__":
    compare_performance()
    print("\n")
    demo_memoization()
    print("\n")
    analyze_complexity()
    build_performance_graph()