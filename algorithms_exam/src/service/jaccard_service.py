class JaccardService:
    """
    Сервис для оценки схожести двух строк по коэффициенту Жаккара.

    Текст разбивается на набор шинглов фиксированного размера,
    затем считается |A ∩ B| / |A ∪ B| с округлением до сотых.
    """

    shingle_size: int = 3

    def get_similarity(self, first: str, second: str) -> float:
        """
        Возвращает значение схожести строк first и second в диапазоне [0..1].

        1. Быстрая проверка на полное равенство — сразу 1.0
        2. Разбиение строк на множества шинглов длины shingle_size
        3. Жаккард по множествам шинглов; пустые одновременно множества => 1.0
        4. Округление до 2 знаков после запятой
        """
        if first == second:
            return 1.0
        first_shingles = self._split_text_to_shingles(first)
        second_shingles = self._split_text_to_shingles(second)
        if not first_shingles and not second_shingles:
            return 1.0
        if second_shingles:
            result = len(first_shingles & second_shingles) / len(
                first_shingles | second_shingles
            )
            return round(result, 2)
        return 0.0

    def _split_text_to_shingles(self, text: str) -> set[str]:
        """Разбивает строку на шинглы фиксированной длины (как множество)."""
        result = set()
        for i in range(len(text)):
            shingle = text[i: i + self.shingle_size]
            if len(shingle) == self.shingle_size:
                result.add(shingle)
        return result
