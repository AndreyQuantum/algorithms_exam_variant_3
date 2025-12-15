import re

from algorithms_exam.src.service.kmp_service import KMPService


class StringService:
    """
    Сервис нормализации строковых данных.
    - приведение к нижнему регистру;
    - удаление спецсимволов (оставляем буквы/цифры/+, точки и пробелы);
    - удаление «лишних» ключевых слов (через KMP, допускает перекрытия);
    - схлопывание повторных пробелов и обрезка краёв.
    """

    FILTER_KEYWORDS = {
        "дюйм",
        "телефон",
        "смартфон",
        "планшет",
        "mm",
        "гб",
        "мм",
        "синий",
        "black",
        "черный",
        "робот",
        "пылесос",
        "vacuum",
        "cleaner",
        "robot",
    }

    def normalize(self, text: str) -> str:
        """Приводит входную строку к канонической форме для сравнения."""
        text = self._make_text_lower(text)
        text = self._remove_special_symbols(text)
        text = self._remove_extensive_keywords(text)
        text = self._remove_extensive_spaces(text)
        return text.strip()

    def _remove_extensive_spaces(self, text: str) -> str:
        """Заменяет последовательности пробелов на один и обрезает края."""
        return re.sub(r"\s+", " ", text).strip()

    def _remove_special_symbols(self, text: str) -> str:
        """Удаляет все символы, кроме букв/цифр/пробелов, плюс и точки."""
        return re.sub(r"[^a-zа-яё0-9+.\s]", " ", text)

    def _make_text_lower(self, text: str) -> str:
        """Безопасно приводит строку к нижнему регистру (None -> пустая)."""
        text = (text or "").lower()
        return text

    def _remove_extensive_keywords(self, text: str) -> str:
        """
        Удаляет заранее известные «шумовые» слова/фразы из текста.

        Поиск вхождений выполняется KMP-алгоритмом, что позволяет эффективно
        находить все перекрывающиеся совпадения и удалять их из строки.
        """
        kmp = KMPService()
        for pattern in self.FILTER_KEYWORDS:
            found_indexes_to_remove = kmp.search_all(text, pattern)
            for indexes in found_indexes_to_remove:
                text = text[: indexes[0]] + text[indexes[1]:]
        return text
