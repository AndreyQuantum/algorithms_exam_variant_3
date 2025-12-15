class KMPService:
    """
    Сервис для поиска подстрок в строке
    с использованием алгоритма Кнута — Морриса — Пратта (KMP).
    """

    @staticmethod
    def build_prefix_function(pattern: str) -> list[int]:
        """
        Строит префикс-функцию для шаблона.

        prefix[i] — длина наибольшего собственного префикса строки pattern[0:i+1],
        который одновременно является её суффиксом.

        Время: O(m)
        Память: O(m)
        """
        pattern_length = len(pattern)
        prefix = [0] * pattern_length

        current_prefix_length = 0

        for i in range(1, pattern_length):
            while (
                    current_prefix_length > 0
                    and pattern[i] != pattern[current_prefix_length]
            ):
                current_prefix_length = prefix[current_prefix_length - 1]

            if pattern[i] == pattern[current_prefix_length]:
                current_prefix_length += 1
                prefix[i] = current_prefix_length

        return prefix

    @staticmethod
    def search_all(text: str, pattern: str) -> list[tuple[int, int]]:
        """
        Ищет все вхождения подстроки pattern в строке text.

        Возвращает список диапазонов (start, end),
        где end — эксклюзивная граница.

        Время: O(n + m)
        Память: O(m)
        """
        text_length = len(text)
        pattern_length = len(pattern)

        if pattern_length == 0:
            # Пустой шаблон совпадает в каждой позиции
            return [(i, i) for i in range(text_length + 1)]

        if pattern_length > text_length:
            return []

        prefix = KMPService.build_prefix_function(pattern)
        result_ranges: list[tuple[int, int]] = []

        matched_length = 0

        for text_index in range(text_length):
            while (
                    matched_length > 0
                    and text[text_index] != pattern[matched_length]
            ):
                matched_length = prefix[matched_length - 1]

            if text[text_index] == pattern[matched_length]:
                matched_length += 1

                if matched_length == pattern_length:
                    start = text_index - pattern_length + 1
                    end = start + pattern_length
                    result_ranges.append((start, end))

                    # Разрешаем перекрывающиеся совпадения
                    matched_length = prefix[matched_length - 1]

        return result_ranges

    @staticmethod
    def search_first(text: str, pattern: str) -> tuple[int, int] | None:
        """
        Ищет первое вхождение подстроки pattern в строке text.

        Возвращает диапазон (start, end) или None, если совпадений нет.

        Время: O(n + m)
        Память: O(m)
        """
        text_length = len(text)
        pattern_length = len(pattern)

        if pattern_length == 0:
            return (0, 0)

        if pattern_length > text_length:
            return None

        prefix = KMPService.build_prefix_function(pattern)
        matched_length = 0

        for text_index in range(text_length):
            while (
                    matched_length > 0
                    and text[text_index] != pattern[matched_length]
            ):
                matched_length = prefix[matched_length - 1]

            if text[text_index] == pattern[matched_length]:
                matched_length += 1

                if matched_length == pattern_length:
                    start = text_index - pattern_length + 1
                    end = start + pattern_length
                    return (start, end)

        return None
