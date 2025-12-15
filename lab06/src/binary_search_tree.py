class TreeNode:
    """Узел бинарного дерева поиска"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Бинарное дерево поиска"""
    
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """
        Вставка элемента в дерево.
        Сложность: O(log n) в среднем, O(n) в худшем (вырожденное дерево)
        """
        new_node = TreeNode(value)
        
        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
    
    def search(self, value):
        """
        Поиск элемента в дереве.
        Сложность: O(log n) в среднем, O(n) в худшем (вырожденное дерево)
        """
        current = self.root
        
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        
        return False
    
    def in_order_traversal(self):
        """
        Обход дерева in-order (левый-корень-правый).
        Возвращает список элементов в порядке возрастания.
        Сложность: O(n)
        """
        result = []
        
        def _traverse(node):
            if node is not None:
                _traverse(node.left)
                result.append(node.value)
                _traverse(node.right)
        
        _traverse(self.root)
        return result
    
    def get_height(self):
        """
        Вычисление высоты дерева с использованием итеративного подхода.
        Сложность: O(n)
        """
        if self.root is None:
            return 0
        
        # Итеративный DFS с использованием стека
        stack = [(self.root, 1)]  # (узел, текущая глубина)
        max_height = 0
        
        while stack:
            node, depth = stack.pop()
            if depth > max_height:
                max_height = depth
            
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
        
        return max_height
    
    def print_tree(self):
        """Печать дерева в виде скобочной последовательности"""
        def _print(node):
            if node is None:
                return ""
            result = str(node.value)
            if node.left or node.right:
                result += "(" + _print(node.left) + "," + _print(node.right) + ")"
            return result
        
        return _print(self.root)
    
    def is_empty(self):
        """Проверка, пусто ли дерево"""
        return self.root is None