import matplotlib.pyplot as plt
from performance_test import measure_sort_time
from generate_data import generate_random
from sorts import bubble_sort, selection_sort, insertion_sort

def plot_sorting_performance():
    """Построение графика производительности"""
    sizes = [100, 200, 300, 400, 500]
    algorithms = [
        ("Пузырьком", bubble_sort),
        ("Выбором", selection_sort),
        ("Вставками", insertion_sort)
    ]
    
    print("ПОСТРОЕНИЕ ГРАФИКА ПРОИЗВОДИТЕЛЬНОСТИ")
    print("=" * 40)
    
    # Собираем данные
    results = {name: [] for name, _ in algorithms}
    
    for size in sizes:
        print(f"\nРазмер {size}: ", end="")
        arr = generate_random(size)
        
        for name, func in algorithms:
            time_taken = measure_sort_time(func, arr)
            results[name].append(time_taken)
            print(f"{name[0]}={time_taken:.4f} ", end="")
    
    # Строим график
    plt.figure(figsize=(10, 6))
    
    colors = ['red', 'green', 'blue']
    markers = ['o', 's', '^']
    
    for i, (name, times) in enumerate(results.items()):
        plt.plot(sizes, times, 
                color=colors[i], 
                marker=markers[i],
                linewidth=2,
                markersize=8,
                label=name)
    
    plt.title('Сравнение времени сортировки', fontsize=14)
    plt.xlabel('Размер массива (элементов)', fontsize=12)
    plt.ylabel('Время выполнения (секунды)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Сохраняем график
    plt.savefig('sorting_performance.png', dpi=300, bbox_inches='tight')
    print("\n\n✅ График сохранен как 'sorting_performance.png'")
    plt.show()

def plot_data_type_comparison():
    """Сравнение производительности на разных типах данных"""
    size = 500
    data_types = [
        ("Случайный", generate_random(size)),
        ("Отсортированный", list(range(1, size + 1))),
        ("Обратный", list(range(size, 0, -1))),
        ("Почти отсорт.", generate_random(size))
    ]
    
    algorithms = [
        ("Пузырьком", bubble_sort),
        ("Выбором", selection_sort),
        ("Вставками", insertion_sort)
    ]
    
    print("\nСРАВНЕНИЕ НА РАЗНЫХ ТИПАХ ДАННЫХ")
    print("=" * 40)
    
    # Подготовка данных для графика
    results = {name: [] for name, _ in data_types}
    
    for data_name, arr in data_types:
        print(f"\n{data_name}:")
        for algo_name, func in algorithms:
            time_taken = measure_sort_time(func, arr.copy())
            results[data_name].append(time_taken)
            print(f"  {algo_name}: {time_taken:.6f} сек")
    
    # Строим столбчатую диаграмму
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x = range(len(data_types))
    width = 0.25
    
    for i, algo_name in enumerate(["Пузырьком", "Выбором", "Вставками"]):
        times = [results[data_name][i] for data_name, _ in data_types]
        ax.bar([pos + i*width for pos in x], times, width, label=algo_name)
    
    ax.set_xlabel('Тип данных', fontsize=12)
    ax.set_ylabel('Время выполнения (секунды)', fontsize=12)
    ax.set_title('Влияние типа данных на производительность (n=500)', fontsize=14)
    ax.set_xticks([pos + width for pos in x])
    ax.set_xticklabels([name for name, _ in data_types])
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.savefig('data_type_comparison.png', dpi=300, bbox_inches='tight')
    print("\nГрафик сравнения сохранен как 'data_type_comparison.png'")
    plt.show()

if __name__ == "__main__":
    plot_sorting_performance()
    plot_data_type_comparison()