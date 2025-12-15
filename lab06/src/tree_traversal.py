from binary_search_tree import BinarySearchTree

def in_order_recursive(node):
    """
    Рекурсивный обход in-order
    Сложность: O(n)
    """
    if node is None:
        return
    
    in_order_recursive(node.left)
    print(node.value, end=" ")
    in_order_recursive(node.right)


def pre_order_recursive(node):
    """
    Рекурсивный обход pre-order
    Сложность: O(n)
    """
    if node is None:
        return
    
    print(node.value, end=" ")
    pre_order_recursive(node.left)
    pre_order_recursive(node.right)


def post_order_recursive(node):
    """
    Рекурсивный обход post-order
    Сложность: O(n)
    """
    if node is None:
        return
    
    post_order_recursive(node.left)
    post_order_recursive(node.right)
    print(node.value, end=" ")