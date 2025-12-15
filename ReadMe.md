# Вариант 3
# Описание проекта

Исходный код проекта находится в `algorithms_exam/src`

Тесты основных сервисов находятся в `algorithms_exam/tests`

Файл запуска расположен в `algorithms_exam/src/main.py`
# Запуск

Для запуска алгоритма необходимо установить [poetry](https://python-poetry.org/docs/#installation)

После установки poetry необходимо перейти в папку проекта и выполнить команду

```bash
make install
```

После этого можно запустить алгоритм командой

```bash
make run
```

# Установка переменных

Переменные ``SIMILARITY_THRESHOLD`` и ``USE_PREPROCESSING`` меняются в файле [settings.yml](settings.yml) в корне
проекта.

Также их можно менять путем установки переменных окружения
Переменная файла | переменная окружения

| Переменная окружения            | Параметр               |
|---------------------------------|------------------------|
| `DYNACONF_SIMILARITY_THRESHOLD` | `SIMILARITY_THRESHOLD` |
| `DYNACONF_USE_PREPROCESSING`    | `USE_PREPROCESSING`    |

Все переменные валидируются благодаря библиотеке pydantic.
