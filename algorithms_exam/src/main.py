from algorithms_exam.src.service.file_service import FileService


def main():
    file_service = FileService()
    catalog = file_service.read_catalog()
    new_items = file_service.read_new_items()


if __name__ == '__main__':
    main()
