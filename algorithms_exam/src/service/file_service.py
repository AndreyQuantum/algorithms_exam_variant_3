import json
from pathlib import Path

from algorithms_exam.src.configs.app import settings
from algorithms_exam.src.schemas.product import Product


class FileService:
    """
    Сервис для работы с файловыми источниками данных.

    Отвечает за чтение каталога и списка новых товаров из текстовых файлов,
    а также за запись результата в JSON-файл.
    Формат входных файлов: по одной записи на строку, поля разделены табуляцией.
    Ожидаемые поля: id (int), name (str).
    """

    def read_catalog(self) -> list[Product]:
        """Считывает и парсит файл каталога в список Product."""
        return self._parse_file(settings.files.catalog_file_path)

    def _parse_file(self, path_to_file: Path) -> list[Product]:
        """Читает файл целиком и передает содержимое на парсинг."""
        with open(path_to_file) as f:
            content = f.read()
            return self._parse_product(content)

    def _parse_product(self, file_data: str) -> list[Product]:
        """
        Преобразует текст из файла в список Product.

        Каждая строка распарсивается по табуляции: ожидаются id и name.
        """
        result = []
        for line in file_data.splitlines():
            data = line.split("\t")
            # Простейшая валидация: предполагаем корректный формат входных данных
            product = Product(id=int(data[0]), name=data[1])
            result.append(product)
        return result

    def read_new_items(self) -> list[Product]:
        """Считывает и парсит файл новых товаров в список Product."""
        return self._parse_file(settings.files.new_items_file_path)

    def write_json_to_file(self, path_to_file: Path, result: dict):
        """Записывает результат сопоставления в JSON-файл с отступами."""
        with open(settings.files.result_file_path, "w") as f:
            f.write(json.dumps(result, indent=4))
