# graph_representation.py
"""
Два представления графов: матрица смежности и список смежности
"""

class GraphAdjMatrix:
    """Граф через матрицу смежности"""
    def __init__(self, num_vertices, directed=False):
        """
        Инициализация матрицы смежности
        Сложность: O(V²) памяти, V = количество вершин
        """
        self.num_vertices = num_vertices
        self.directed = directed
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, u, v, weight=1):
        """
        Добавление ребра
        Сложность: O(1)
        """
        self.matrix[u][v] = weight
        if not self.directed:
            self.matrix[v][u] = weight
    
    def remove_edge(self, u, v):
        """
        Удаление ребра
        Сложность: O(1)
        """
        self.matrix[u][v] = 0
        if not self.directed:
            self.matrix[v][u] = 0
    
    def get_neighbors(self, vertex):
        """
        Получение соседей вершины
        Сложность: O(V) - нужно проверить всю строку
        """
        neighbors = []
        for v in range(self.num_vertices):
            if self.matrix[vertex][v] != 0:
                neighbors.append((v, self.matrix[vertex][v]))
        return neighbors
    
    def has_edge(self, u, v):
        """
        Проверка наличия ребра
        Сложность: O(1)
        """
        return self.matrix[u][v] != 0
    
    def print_graph(self):
        """Вывод графа"""
        print("Матрица смежности:")
        for row in self.matrix:
            print(row)


class GraphAdjList:
    """Граф через список смежности"""
    def __init__(self, num_vertices, directed=False):
        """
        Инициализация списка смежности
        Сложность: O(V) памяти
        """
        self.num_vertices = num_vertices
        self.directed = directed
        self.adj_list = [[] for _ in range(num_vertices)]
    
    def add_edge(self, u, v, weight=1):
        """
        Добавление ребра
        Сложность: O(1) в среднем
        """
        self.adj_list[u].append((v, weight))
        if not self.directed:
            self.adj_list[v].append((u, weight))
    
    def remove_edge(self, u, v):
        """
        Удаление ребра
        Сложность: O(degree(u)) - нужно найти ребро в списке
        """
        self.adj_list[u] = [neighbor for neighbor in self.adj_list[u] if neighbor[0] != v]
        if not self.directed:
            self.adj_list[v] = [neighbor for neighbor in self.adj_list[v] if neighbor[0] != u]
    
    def get_neighbors(self, vertex):
        """
        Получение соседей вершины
        Сложность: O(degree(vertex)) - просто вернуть список
        """
        return self.adj_list[vertex]
    
    def has_edge(self, u, v):
        """
        Проверка наличия ребра
        Сложность: O(degree(u)) - поиск в списке
        """
        for neighbor, _ in self.adj_list[u]:
            if neighbor == v:
                return True
        return False
    
    def print_graph(self):
        """Вывод графа"""
        print("Список смежности:")
        for i, neighbors in enumerate(self.adj_list):
            print(f"{i}: {neighbors}")


def test_representations():
    """Тестируем оба представления"""
    print("Тестирование представлений графов")
    print("=" * 50)
    
    # Создаем одинаковый граф в двух представлениях
    V = 5  # 5 вершин
    
    # Матрица смежности
    print("\n1. Матрица смежности:")
    g1 = GraphAdjMatrix(V, directed=False)
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 3)
    g1.add_edge(2, 4)
    g1.add_edge(3, 4)
    g1.print_graph()
    
    # Проверяем операции
    print(f"\nСоседи вершины 0: {g1.get_neighbors(0)}")
    print(f"Есть ли ребро 0-1? {g1.has_edge(0, 1)}")
    print(f"Есть ли ребро 1-4? {g1.has_edge(1, 4)}")
    
    # Список смежности
    print("\n2. Список смежности:")
    g2 = GraphAdjList(V, directed=False)
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(1, 3)
    g2.add_edge(2, 4)
    g2.add_edge(3, 4)
    g2.print_graph()
    
    # Проверяем операции
    print(f"\nСоседи вершины 0: {g2.get_neighbors(0)}")
    print(f"Есть ли ребро 0-1? {g2.has_edge(0, 1)}")
    print(f"Есть ли ребро 1-4? {g2.has_edge(1, 4)}")


if __name__ == "__main__":
    test_representations()