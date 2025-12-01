import time
import matplotlib.pyplot as plt
from hash_table_chaining import HashTableChaining

def plot_load_factor_vs_time():
    """График зависимости времени от коэффициента заполнения"""
    print("📈 ПОСТРОЕНИЕ ГРАФИКА: КОЭФФИЦИЕНТ ЗАПОЛНЕНИЯ vs ВРЕМЯ")
    print("=" * 60)
    
    load_factors = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    insert_times = []
    search_times = []
    delete_times = []
    
    table_size = 100
    
    for load in load_factors:
        print(f"\nТестируем коэффициент: {load}")
        
        # Создаем новую таблицу для каждого теста
        ht = HashTableChaining(capacity=table_size)
        elements_count = int(table_size * load)
        
        # Вставка
        start = time.time()
        for i in range(elements_count):
            ht.insert(f"key_{i}", f"value_{i}")
        insert_time = time.time() - start
        
        # Поиск
        start = time.time()
        for i in range(elements_count):
            ht.search(f"key_{i}")
        search_time = time.time() - start
        
        # Удаление
        start = time.time()
        for i in range(elements_count):
            ht.delete(f"key_{i}")
        delete_time = time.time() - start
        
        insert_times.append(insert_time)
        search_times.append(search_time)
        delete_times.append(delete_time)
        
        print(f"  Вставка: {insert_time:.6f} сек")
        print(f"  Поиск:   {search_time:.6f} сек")
        print(f"  Удаление: {delete_time:.6f} сек")
    
    # Строим график
    plt.figure(figsize=(12, 8))
    
    # График 1: Все операции
    plt.subplot(2, 2, 1)
    plt.plot(load_factors, insert_times, 'ro-', linewidth=2, markersize=6, label='Вставка')
    plt.plot(load_factors, search_times, 'go-', linewidth=2, markersize=6, label='Поиск')
    plt.plot(load_factors, delete_times, 'bo-', linewidth=2, markersize=6, label='Удаление')
    plt.xlabel('Коэффициент заполнения (α)', fontsize=12)
    plt.ylabel('Время выполнения (секунды)', fontsize=12)
    plt.title('Зависимость времени от коэффициента заполнения', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # График 2: Вставка отдельно
    plt.subplot(2, 2, 2)
    plt.plot(load_factors, insert_times, 'ro-', linewidth=2, markersize=6)
    plt.xlabel('Коэффициент заполнения (α)', fontsize=12)
    plt.ylabel('Время вставки (секунды)', fontsize=12)
    plt.title('Время вставки vs α', fontsize=14)
    plt.grid(True, alpha=0.3)
    
    # График 3: Поиск отдельно
    plt.subplot(2, 2, 3)
    plt.plot(load_factors, search_times, 'go-', linewidth=2, markersize=6)
    plt.xlabel('Коэффициент заполнения (α)', fontsize=12)
    plt.ylabel('Время поиска (секунды)', fontsize=12)
    plt.title('Время поиска vs α', fontsize=14)
    plt.grid(True, alpha=0.3)
    
    # График 4: Удаление отдельно
    plt.subplot(2, 2, 4)
    plt.plot(load_factors, delete_times, 'bo-', linewidth=2, markersize=6)
    plt.xlabel('Коэффициент заполнения (α)', fontsize=12)
    plt.ylabel('Время удаления (секунды)', fontsize=12)
    plt.title('Время удаления vs α', fontsize=14)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('hash_table_performance.png', dpi=300, bbox_inches='tight')
    print("\n✅ График сохранен как 'hash_table_performance.png'")
    plt.show()

def plot_collision_distribution():
    """Гистограмма распределения длины цепочек"""
    print("\n📊 ГИСТОГРАММА РАСПРЕДЕЛЕНИЯ ЦЕПОЧЕК")
    print("=" * 60)
    
    # Создаем таблицу
    ht = HashTableChaining(capacity=20)
    
    # Вставляем элементы
    elements_count = 100
    for i in range(elements_count):
        ht.insert(f"key_{i}", f"value_{i}")
    
    # Считаем длину цепочек
    chain_lengths = []
    for i in range(ht.capacity):
        length = 0
        current = ht.table[i]
        while current:
            length += 1
            current = current.next
        chain_lengths.append(length)
    
    # Строим гистограмму
    plt.figure(figsize=(10, 6))
    
    plt.hist(chain_lengths, bins=range(0, max(chain_lengths) + 2), 
             alpha=0.7, color='blue', edgecolor='black')
    
    plt.xlabel('Длина цепочки', fontsize=12)
    plt.ylabel('Количество ячеек', fontsize=12)
    plt.title(f'Распределение длины цепочек (n={elements_count}, m={ht.capacity})', fontsize=14)
    plt.grid(True, alpha=0.3, axis='y')
    
    # Добавляем среднее значение
    avg_length = sum(chain_lengths) / len(chain_lengths)
    plt.axvline(avg_length, color='red', linestyle='--', 
                label=f'Средняя: {avg_length:.2f}')
    plt.legend()
    
    plt.savefig('collision_distribution.png', dpi=300, bbox_inches='tight')
    print("✅ Гистограмма сохранена как 'collision_distribution.png'")
    
    # Выводим статистику
    print(f"\nСтатистика цепочек:")
    print(f"Всего ячеек: {ht.capacity}")
    print(f"Всего элементов: {ht.size}")
    print(f"Коэффициент заполнения: {ht.get_load_factor():.2f}")
    print(f"Средняя длина цепочки: {avg_length:.2f}")
    print(f"Максимальная длина: {max(chain_lengths)}")
    print(f"Пустых ячеек: {chain_lengths.count(0)}")
    
    plt.show()

if __name__ == "__main__":
    plot_load_factor_vs_time()
    plot_collision_distribution()