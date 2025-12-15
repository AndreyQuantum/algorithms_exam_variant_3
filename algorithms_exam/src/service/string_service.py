import re


class StringService:
    # Минимальный набор стоп-слов - только общие категории и цвета
    FILTER_KEYWORDS = {
        # общие типы устройств (на обоих языках)
        "смартфон", "телефон", "smartphone", "phone",
        "планшет", "tablet",
        "чехол", "зарядка", "держатель", "ноутбук", "стекло",

        # цвета (удаляем, т.к. не важны для определения дубликатов)
        "черный", "белый", "серый", "серебристый",
        "синий", "голубой",
        "красный", "бордовый",
        "зеленый", "салатовый",
        "желтый", "оранжевый",
        "розовый", "фиолетовый",
        "золотой", "бронзовый",
        "бежевый", "коричневый",
        "графит", "матовый", "глянцевый",
        "black", "white", "blue", "grey", "gray",
    }

    # Единицы измерения, которые считаем лишними в названии товара.
    # ВНИМАНИЕ: единицы объёма/памяти (gb/гб/mb/мб/tb/тб) оставляем — они важны для сравнения.
    UNITS = [
        "mm", "мм", "cm", "см", "m", "м",
        "дюйм", "дюймов", '"',
        "мач", "mah", "вт", "w",
        "kg", "кг", "g", "г"
    ]


    def normalize(self, text: str) -> str:
        """Упрощенная нормализация без словарей переводов"""
        text = self._make_text_lower(text)
        text = self._remove_units(text)
        text = self._remove_extensive_keywords(text)
        text = self._remove_special_symbols(text)
        text = self._remove_extensive_spaces(text)
        return text

    def _remove_extensive_spaces(self, text: str) -> str:
        return re.sub(r"\s+", " ", text).strip()

    def _remove_special_symbols(self, text: str) -> str:
        # Сохраняем дефис, т.к. он значим для некоторых моделей (и ожидается тестами)
        # Удаляем прочие спецсимволы, кроме букв, цифр, '+', пробелов и '-'
        return re.sub(r"[^a-zа-яё0-9+\s-]", " ", text)

    def _make_text_lower(self, text: str) -> str:
        text = (text or "").lower()
        return text

    def _remove_extensive_keywords(self, text: str) -> str:
        # Удаляем ключевые слова простыми подстановками (как подстроки),
        # сортируя по длине, чтобы сначала убирать более длинные варианты.
        for kw in sorted(self.FILTER_KEYWORDS, key=len, reverse=True):
            if not kw:
                continue
            text = re.sub(re.escape(kw), " ", text)
        return text

    def _remove_units(self, text: str) -> str:
        """Удаляет единицы измерения"""
        for unit in self.UNITS:
            # Удаляем единицы с границами слов и после цифр
            text = re.sub(rf'\b{re.escape(unit)}\b', ' ', text, flags=re.IGNORECASE)
            # Также удаляем единицы, идущие сразу после цифр (например 256gb)
            text = re.sub(rf'(\d+){re.escape(unit)}\b', r'\1 ', text, flags=re.IGNORECASE)
        return text

    def extract_numbers(self, text: str) -> set[str]:
        """Извлекает все числа из текста"""
        # Находим все числа (включая дробные и через слэш)
        numbers = re.findall(r'\d+(?:[./]\d+)*', text)
        return set(numbers)

    def extract_latin_words(self, text: str) -> set[str]:
        """Извлекает слова на латинице (бренды и модели обычно на английском)"""
        # Находим последовательности латинских букв, цифр и символов +
        latin_words = re.findall(r'[a-z]+[a-z0-9+]*', text.lower())
        # Фильтруем короткие слова (менее 2 символов) и стоп-слова
        stopwords = {'gb', 'mb', 'tb', 'mm', 'cm', 'mah', 'kg', 'black', 'white', 'blue', 'grey', 'gray'}
        return {word for word in latin_words if len(word) >= 2 and word not in stopwords}

    def extract_all_words(self, text: str) -> set[str]:
        """Извлекает все слова из текста"""
        words = text.split()
        return set(words)
