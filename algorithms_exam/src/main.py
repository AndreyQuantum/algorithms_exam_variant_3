from algorithms_exam.src.configs.app import settings
from algorithms_exam.src.schemas.product import Product
from algorithms_exam.src.service.file_service import FileService
from algorithms_exam.src.service.jaccard_service import JaccardService
from algorithms_exam.src.service.string_service import StringService

string_service = StringService()
file_service = FileService()
jaccard_service = JaccardService()


def main():
    """
    Основная точка входа:
    1) читает каталог и новые товары из файлов;
    2) при необходимости выполняет нормализацию названий (preprocessing);
    3) считает схожесть по Жаккару между каждым новым товаром и элементами каталога;
    4) сохраняет результат в JSON.
    """
    # Читаем исходные данные
    catalog = file_service.read_catalog()
    new_items = file_service.read_new_items()

    # Предобработка строк: нормализация для более корректного сравнения
    if settings.USE_PREPROCESSING:
        normalise_product_list_names(products=catalog)
        normalise_product_list_names(products=new_items)

    # Словарь результатов: ключ — id нового товара, значение — список похожих из каталога
    similar_products_result = {}
    for new_item in new_items:
        similar_products_result[new_item.id] = []
        for catalog_element in catalog:
            # Схожесть строк названий товаров по коэффициенту Жаккара
            similarity = jaccard_service.get_similarity(
                catalog_element.name, new_item.name
            )
            # Фильтруем по порогу, задаваемому в настройках (settings.SIMILARITY_THRESHOLD)
            if similarity >= settings.SIMILARITY_THRESHOLD:
                similar_products_result[new_item.id].append(
                    {"catalog_id": catalog_element.id, "similarity_score": similarity}
                )

    # Записываем результаты в JSON-файл
    file_service.write_json_to_file(
        result=similar_products_result, path_to_file=settings.files.result_file_path
    )


def normalise_product_list_names(products: list[Product]):
    """Нормализует поле name у каждого Product в списке."""
    for item in products:
        item.name = string_service.normalize(item.name)


if __name__ == "__main__":
    main()
