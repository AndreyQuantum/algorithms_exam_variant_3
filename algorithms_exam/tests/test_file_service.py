from pathlib import Path

from algorithms_exam.src.schemas.product import Product
from algorithms_exam.src.service.file_service import FileService


def test_parse_file_catalog_parses_txt_into_product_list():
    service = FileService()

    products = service._parse_file(Path("catalog.txt"))

    assert isinstance(products, list)
    assert all(isinstance(p, Product) for p in products)
    assert len(products) == 5
    # С учетом текущей реализации name берется как второй токен строки
    assert products[0].id == 1001
    assert products[0].name == "Смартфон"
    assert products[-1].id == 1005
    assert products[-1].name == "HUAWEI"


def test_parse_file_new_items_parses_txt_into_product_list():
    service = FileService()

    products = service._parse_file(Path("new_items.txt"))

    assert isinstance(products, list)
    assert all(isinstance(p, Product) for p in products)
    assert len(products) == 5
    assert products[0].id == 2001
    assert products[0].name == "Xiaomi"


def test_read_catalog_expected_to_return_product_list():
    service = FileService()

    products = service.read_catalog()

    assert isinstance(products, list)
    assert all(isinstance(p, Product) for p in products)
    assert len(products) == 5


def test_read_new_items_expected_to_return_product_list():
    service = FileService()

    products = service.read_new_items()

    assert isinstance(products, list)
    assert all(isinstance(p, Product) for p in products)
    assert len(products) == 5
