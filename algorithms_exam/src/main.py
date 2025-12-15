from algorithms_exam.src.configs.app import settings
from algorithms_exam.src.schemas.product import Product
from algorithms_exam.src.service.file_service import FileService
from algorithms_exam.src.service.jaccard_service import JaccardService
from algorithms_exam.src.service.string_service import StringService

string_service = StringService()
file_service = FileService()
jaccard_service = JaccardService()


def main():
    catalog = file_service.read_catalog()
    new_items = file_service.read_new_items()
    if settings.USE_PREPROCESSING:
        normalise_product_list_names(products=catalog)
        normalise_product_list_names(products=new_items)
    similar_products_result = {}
    for new_item in new_items:
        similar_products_result[new_item.id] = []
        for catalog_element in catalog:
            similarity = jaccard_service.get_similarity(catalog_element.name, new_item.name)
            if similarity >= settings.SIMILARITY_THRESHOLD:
                similar_products_result[new_item.id].append({
                    "catalog_id": catalog_element.id,
                    "similarity_score": similarity
                })
    file_service.write_json_to_file(result=similar_products_result,
                                    path_to_file=settings.files.result_file_path)


def normalise_product_list_names(products: list[Product]):
    for item in products:
        item.name = string_service.normalize(item.name)


if __name__ == '__main__':
    main()
