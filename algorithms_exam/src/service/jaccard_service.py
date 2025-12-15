class JaccardService:
    shingle_size: int = 3  # длина символьного шингла

    def get_similarity(self, first: str, second: str) -> float:
        """Считает Жаккар по символьным 3-граммам исходных строк (без нормализации)."""
        if first == second:
            return 1.0

        first_shingles = self._split_text_to_shingles(first)
        second_shingles = self._split_text_to_shingles(second)

        if not first_shingles and not second_shingles:
            return 1.0
        if not first_shingles or not second_shingles:
            return 0.0

        intersection = len(first_shingles & second_shingles)
        union = len(first_shingles | second_shingles)
        if union == 0:
            return 0.0
        return round(intersection / union, 2)

    def _split_text_to_shingles(self, text: str) -> set[str]:
        """Возвращает множество символьных шинглов фиксированной длины по всей строке."""
        if not text:
            return set()
        n = self.shingle_size
        if len(text) < n:
            return set()
        return {text[i:i + n] for i in range(len(text) - n + 1)}
