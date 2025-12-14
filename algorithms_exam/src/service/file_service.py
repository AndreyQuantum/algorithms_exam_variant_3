from pathlib import Path

from algorithms_exam.src.configs.app import settings
from algorithms_exam.src.schemas.product import Product


class FileService:
    def read_catalog(self) -> list[Product]:
        return self._parse_file(settings.files.catalog_file_path)

    def _parse_file(self, path_to_file: Path) -> list[Product]:
        with open(path_to_file) as f:
            content = f.read()
            return self._parse_product(content)

    def _parse_product(self, file_data: str) -> list[Product]:
        result = []
        for line in file_data.splitlines():
            data = line.split()
            product = Product(id=int(data[0]), name=data[1])
            result.append(product)
        return result

    def read_new_items(self) -> list[Product]:
        return self._parse_file(settings.files.new_items_file_path)
