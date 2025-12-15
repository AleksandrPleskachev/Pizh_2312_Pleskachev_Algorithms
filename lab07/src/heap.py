"""
Реализация Min-кучи (Min-Heap) на основе массива.
Куча - полное бинарное дерево, где каждый родитель <= своих детей.
"""

class MinHeap:
    """Min-куча (минимальный элемент в корне)"""
    
    def __init__(self):
        """Инициализация пустой кучи"""
        self.heap = []  # Основной массив для хранения элементов
    
    def parent_index(self, i):
        """Индекс родителя элемента с индексом i. Сложность: O(1)"""
        return (i - 1) // 2 if i > 0 else 0
    
    def left_child_index(self, i):
        """Индекс левого ребенка элемента с индексом i. Сложность: O(1)"""
        return 2 * i + 1
    
    def right_child_index(self, i):
        """Индекс правого ребенка элемента с индексом i. Сложность: O(1)"""
        return 2 * i + 2
    
    def swap(self, i, j):
        """Обмен элементов с индексами i и j. Сложность: O(1)"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _sift_up(self, i):
        """
        Всплытие элемента (проталкивание вверх).
        Восстанавливает свойство кучи снизу вверх.
        Сложность: O(log n)
        """
        while i > 0 and self.heap[i] < self.heap[self.parent_index(i)]:
            parent = self.parent_index(i)
            self.swap(i, parent)
            i = parent
    
    def _sift_down(self, i):
        """
        Погружение элемента (проталкивание вниз).
        Восстанавливает свойство кучи сверху вниз.
        Сложность: O(log n)
        """
        size = len(self.heap)
        while True:
            left = self.left_child_index(i)
            right = self.right_child_index(i)
            smallest = i
            
            # Ищем наименьший среди текущего элемента и его детей
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            # Если текущий элемент уже наименьший - свойство кучи восстановлено
            if smallest == i:
                break
            
            # Меняем местами с наименьшим ребенком и продолжаем
            self.swap(i, smallest)
            i = smallest
    
    def insert(self, value):
        """
        Вставка элемента в кучу.
        Сложность: O(log n)
        """
        self.heap.append(value)  # Добавляем в конец
        self._sift_up(len(self.heap) - 1)  # Всплываем
    
    def extract_min(self):
        """
        Извлечение минимального элемента (корня).
        Сложность: O(log n)
        """
        if not self.heap:
            raise IndexError("Куча пуста")
        
        # Минимальный элемент всегда в корне (индекс 0)
        min_val = self.heap[0]
        
        # Перемещаем последний элемент в корень
        last = self.heap.pop()
        if self.heap:  # Если куча не пуста после извлечения
            self.heap[0] = last
            self._sift_down(0)  # Погружаем новый корень
        
        return min_val
    
    def peek(self):
        """
        Просмотр минимального элемента без извлечения.
        Сложность: O(1)
        """
        if not self.heap:
            raise IndexError("Куча пуста")
        return self.heap[0]
    
    def size(self):
        """Количество элементов в куче. Сложность: O(1)"""
        return len(self.heap)
    
    def is_empty(self):
        """Проверка, пуста ли куча. Сложность: O(1)"""
        return len(self.heap) == 0
    
    def build_heap(self, array):
        """
        Построение кучи из произвольного массива.
        Сложность: O(n)
        """
        self.heap = array.copy()
        
        # Начинаем с последнего нелистового узла и идем к корню
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i)
    
    def print_heap(self):
        """Вывод кучи в виде массива и древовидной структуры"""
        print(f"Куча как массив: {self.heap}")
        
        if not self.heap:
            print("Куча пуста")
            return
        
        print("\nДревовидное представление:")
        height = 0
        i = 0
        while i < len(self.heap):
            level_size = 2 ** height
            level_items = self.heap[i:i + level_size]
            indent = " " * (2 ** (3 - height)) if height < 4 else ""
            print(f"{indent}{' '.join(str(x) for x in level_items)}")
            i += level_size
            height += 1