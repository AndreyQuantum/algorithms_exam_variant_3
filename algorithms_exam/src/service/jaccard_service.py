class JaccardService:
    shingle_size: int = 3

    def compare_first_with_second(self, first: str, second: str) -> float:
        pass

    def _split_text_to_shingles(self, text: str) -> set[str]:
        result = set()
        for i in range(len(text)):
            shingle = text[i: i + self.shingle_size]
            if len(shingle) == self.shingle_size:
                result.add(shingle)
        return result
