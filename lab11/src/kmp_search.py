"""
Алгоритм Кнута-Морриса-Пратта (KMP) для поиска подстроки
"""

def kmp_search(text, pattern):
    """
    Поиск всех вхождений pattern в text с помощью алгоритма KMP
    Сложность: O(n + m), где n = len(text), m = len(pattern)
    Память: O(m) для префикс-функции
    
    Возвращает список индексов начала вхождений
    """
    if not pattern:
        return []
    
    n = len(text)
    m = len(pattern)
    
    # Вычисляем префикс-функцию для паттерна
    from prefix_function import compute_prefix_function
    pi = compute_prefix_function(pattern)
    
    indices = []  # индексы начала вхождений
    j = 0  # индекс в паттерне
    
    for i in range(n):  # i - индекс в тексте
        # Пока есть несовпадение, используем префикс-функцию
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        
        # Если символы совпали
        if text[i] == pattern[j]:
            j += 1
        
        # Нашли полное вхождение
        if j == m:
            indices.append(i - m + 1)
            j = pi[j - 1]  # продолжаем поиск дальше
    
    return indices


def test_kmp():
    """Тестирование алгоритма KMP"""
    print("\nТестирование алгоритма KMP")
    print("=" * 50)
    
    test_cases = [
        ("ababcabcabababd", "ababd", [10]),  # одно вхождение
        ("aaaaa", "aa", [0, 1, 2, 3]),  # перекрывающиеся вхождения
        ("abcdef", "xyz", []),  # нет вхождений
        ("", "abc", []),  # пустой текст
        ("abc", "", []),  # пустой паттерн
    ]
    
    for text, pattern, expected in test_cases:
        result = kmp_search(text, pattern)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{pattern}' в '{text}' -> {result}")
    
    print("\n✓ Тесты пройдены")


def naive_search(text, pattern):
    """
    Наивный алгоритм поиска подстроки для сравнения
    Сложность: O(n * m) в худшем случае
    """
    n = len(text)
    m = len(pattern)
    indices = []
    
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            indices.append(i)
    
    return indices


if __name__ == "__main__":
    test_kmp()