class JaccardService:
    shingle_size: int = 3

    def get_similarity(self, first: str, second: str) -> float:
        first_shingles = self._split_text_to_shingles(first)
        second_shingles = self._split_text_to_shingles(second)
        if not first_shingles and not second_shingles:
            return 1.0
        if second_shingles:
            result = len(first_shingles & second_shingles) / len(first_shingles | second_shingles)
            return round(result, 2)
        return 0.0

    def _split_text_to_shingles(self, text: str) -> set[str]:
        result = set()
        for i in range(len(text)):
            shingle = text[i: i + self.shingle_size]
            if len(shingle) == self.shingle_size:
                result.add(shingle)
        return result
