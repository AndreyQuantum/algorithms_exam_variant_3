import re

from algorithms_exam.src.service.kmp_service import KMPService


class StringService:

    FILTER_KEYWORDS = {
        # устройства и электроника
        "смартфон", "телефон", "мобильный", "кнопочный",
        "планшет", "фаблет",
        "смарт-часы", "умные часы", "фитнес-браслет",
        "ноутбук", "ультрабук", "нетбук", "хромбук",
        "компьютер", "пк", "системный блок", "моноблок",
        "телевизор", "смарт-тв", "монитор", "проектор",
        "наушники", "гарнитура", "колонка", "саундбар", "микрофон",
        "робот-пылесос", "пылесос",
        "увлажнитель", "очиститель воздуха", "кондиционер",
        "умная лампа", "умная розетка", "камера видеонаблюдения",

        # бытовая техника
        "холодильник", "морозильник",
        "микроволновка", "свч",
        "духовка", "плита", "варочная панель", "вытяжка",
        "кофемашина", "кофеварка", "чайник", "тостер",
        "блендер", "миксер", "мультиварка",
        "стиральная машина", "сушильная машина",
        "посудомоечная машина",
        "утюг", "парогенератор",
        "обогреватель", "тепловентилятор",

        # цвета
        "черный", "белый", "серый", "серебристый",
        "синий", "голубой",
        "красный", "бордовый",
        "зеленый", "салатовый",
        "желтый", "оранжевый",
        "розовый", "фиолетовый",
        "золотой", "бронзовый",
        "бежевый", "коричневый",
        "графит", "матовый", "глянцевый",

        # материалы
        "пластик", "металл", "алюминий", "стекло",
        "керамика", "резина", "силикон",
        "кожа", "экокожа",
        "ткань", "карбон",

        # аксессуары
        "чехол", "бампер",
        "пленка", "защитное стекло",
        "зарядка", "зарядное устройство",
        "кабель", "адаптер", "переходник",
        "док-станция",
        "подставка", "держатель", "кронштейн",
        "аккумулятор", "батарея", "пауэрбанк"
    }


    def normalize(self, text: str) -> str:
        text = self._make_text_lower(text)
        text = self._remove_extensive_keywords(text)
        text = self._remove_special_symbols(text)
        text = self._remove_extensive_spaces(text)
        return text

    def _remove_extensive_spaces(self, text: str) -> str:
        return re.sub(r"\s+", " ", text).strip()

    def _remove_special_symbols(self, text: str) -> str:
        return re.sub(r"[^a-zа-яё0-9+\-\s]", " ", text)

    def _make_text_lower(self, text: str) -> str:
        text = (text or "").lower()
        return text

    def _remove_extensive_keywords(self, text: str) -> str:
        kmp = KMPService()
        for pattern in self.FILTER_KEYWORDS:
            found_indexes_to_remove = kmp.search_all(text, pattern)
            for indexes in found_indexes_to_remove:
                text = text[:indexes[0]] + text[indexes[1]:]
        return text
