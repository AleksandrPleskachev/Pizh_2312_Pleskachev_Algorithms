# graph_traversal.py
"""
Алгоритмы обхода графов: BFS и DFS
"""

from collections import deque

def bfs_adj_list(graph, start_vertex):
    """
    Поиск в ширину (BFS) для списка смежности
    Сложность: O(V + E) - посетим все вершины и ребра
    """
    visited = [False] * len(graph.adj_list)
    distances = [-1] * len(graph.adj_list)
    parents = [-1] * len(graph.adj_list)
    
    queue = deque([start_vertex])
    visited[start_vertex] = True
    distances[start_vertex] = 0
    
    while queue:
        current = queue.popleft()
        
        for neighbor, _ in graph.get_neighbors(current):
            if not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[current] + 1
                parents[neighbor] = current
                queue.append(neighbor)
    
    return distances, parents


def bfs_adj_matrix(graph, start_vertex):
    """
    Поиск в ширину (BFS) для матрицы смежности
    Сложность: O(V²) - нужно проверять все вершины на смежность
    """
    visited = [False] * graph.num_vertices
    distances = [-1] * graph.num_vertices
    parents = [-1] * graph.num_vertices
    
    queue = deque([start_vertex])
    visited[start_vertex] = True
    distances[start_vertex] = 0
    
    while queue:
        current = queue.popleft()
        
        # В матрице нужно проверить все вершины
        for neighbor in range(graph.num_vertices):
            if graph.matrix[current][neighbor] != 0 and not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = distances[current] + 1
                parents[neighbor] = current
                queue.append(neighbor)
    
    return distances, parents


def dfs_recursive_adj_list(graph, start_vertex):
    """
    Поиск в глубину (DFS) рекурсивный для списка смежности
    Сложность: O(V + E)
    """
    visited = [False] * len(graph.adj_list)
    result = []
    
    def dfs(vertex):
        visited[vertex] = True
        result.append(vertex)
        
        for neighbor, _ in graph.get_neighbors(vertex):
            if not visited[neighbor]:
                dfs(neighbor)
    
    dfs(start_vertex)
    return result


def dfs_iterative_adj_list(graph, start_vertex):
    """
    Поиск в глубину (DFS) итеративный для списка смежности
    Сложность: O(V + E)
    """
    visited = [False] * len(graph.adj_list)
    stack = [start_vertex]
    result = []
    
    while stack:
        current = stack.pop()
        
        if not visited[current]:
            visited[current] = True
            result.append(current)
            
            # Добавляем соседей в обратном порядке для упорядоченного обхода
            neighbors = graph.get_neighbors(current)
            for neighbor, _ in reversed(neighbors):
                if not visited[neighbor]:
                    stack.append(neighbor)
    
    return result


def test_traversals():
    """Тестируем BFS и DFS"""
    print("\nТестирование обходов графов")
    print("=" * 50)
    
    # Создаем тестовый граф
    from graph_representation import GraphAdjList, GraphAdjMatrix
    
    V = 6
    edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 5)]
    
    # Для списка смежности
    print("\n1. Список смежности:")
    g_list = GraphAdjList(V, directed=False)
    for u, v in edges:
        g_list.add_edge(u, v)
    
    # BFS
    distances, parents = bfs_adj_list(g_list, 0)
    print(f"BFS расстояния от 0: {distances}")
    print(f"BFS родители: {parents}")
    
    # DFS рекурсивный
    dfs_rec = dfs_recursive_adj_list(g_list, 0)
    print(f"DFS рекурсивный: {dfs_rec}")
    
    # DFS итеративный
    dfs_iter = dfs_iterative_adj_list(g_list, 0)
    print(f"DFS итеративный: {dfs_iter}")
    
    # Для матрицы смежности
    print("\n2. Матрица смежности:")
    g_matrix = GraphAdjMatrix(V, directed=False)
    for u, v in edges:
        g_matrix.add_edge(u, v)
    
    distances, parents = bfs_adj_matrix(g_matrix, 0)
    print(f"BFS расстояния от 0: {distances}")
    print(f"BFS родители: {parents}")


if __name__ == "__main__":
    test_traversals()