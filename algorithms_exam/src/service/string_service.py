import re


class StringService:
    def normalize(self, text: str) -> str:
        text = (text or "").lower()
        text = re.sub(r"[^a-zа-яё0-9+\-\s]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text
