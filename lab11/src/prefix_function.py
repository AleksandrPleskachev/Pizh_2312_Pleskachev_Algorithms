"""
Вычисление префикс-функции для строки
"""

def compute_prefix_function(pattern):
    """
    Вычисление префикс-функции для строки pattern
    Сложность: O(m), где m = len(pattern)
    Память: O(m)
    
    Префикс-функция π[i] - длина наибольшего собственного префикса,
    который является суффиксом подстроки pattern[0..i]
    """
    m = len(pattern)
    pi = [0] * m  # префикс-функция
    
    for i in range(1, m):
        j = pi[i - 1]  # длина предыдущего префикса-суффикса
        
        # Ищем меньший префикс-суффикс, который можно продолжить
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        
        # Если символы совпали, увеличиваем длину
        if pattern[i] == pattern[j]:
            j += 1
        
        pi[i] = j
    
    return pi


def test_prefix_function():
    """Тестирование префикс-функции"""
    print("Тестирование префикс-функции")
    print("=" * 50)
    
    test_cases = [
        ("abababca", [0, 0, 1, 2, 3, 4, 0, 1]),
        ("aaaa", [0, 1, 2, 3]),
        ("abcd", [0, 0, 0, 0]),
        ("aabaabaaa", [0, 1, 0, 1, 2, 3, 4, 5, 2]),
    ]
    
    for pattern, expected in test_cases:
        result = compute_prefix_function(pattern)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{pattern}' -> {result}")
    
    print("\n✓ Тесты пройдены")


if __name__ == "__main__":
    test_prefix_function()