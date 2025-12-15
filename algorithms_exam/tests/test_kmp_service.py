import pytest

from algorithms_exam.src.service.kmp_service import KMPService


@pytest.mark.parametrize(
    "pattern, expected",
    [
        ("", []),  # пустой шаблон -> пустая префикс-функция
        ("a", [0]),
        ("ababaca", [0, 0, 1, 2, 3, 0, 1]),  # классический пример KMP
        ("абаба", [0, 0, 1, 2, 3]),  # кириллица поддерживается
    ],
)
def test_build_prefix_function(pattern, expected):
    assert KMPService.build_prefix_function(pattern) == expected


@pytest.mark.parametrize(
    "text, pattern, expected",
    [
        ("", "", [(0, 0)]),  # пустой шаблон совпадает в каждой позиции
        ("abc", "", [(0, 0), (1, 1), (2, 2), (3, 3)]),
        ("short", "longpattern", []),  # шаблон длиннее текста
        ("aaaa", "aa", [(0, 2), (1, 3), (2, 4)]),  # перекрывающиеся совпадения
        (
                "abcxabcdabxabcdabcdabcy",
                "abcdabcy",
                [(15, 23)],  # известный пример для KMP
        ),
        ("абракадабра", "бра", [(1, 4), (8, 11)]),  # unicode/кириллица
        ("no matches here", "xyz", []),
    ],
)
def test_search_all(text, pattern, expected):
    assert KMPService.search_all(text, pattern) == expected


@pytest.mark.parametrize(
    "text, pattern, expected",
    [
        ("", "", (0, 0)),  # пустой шаблон
        ("abc", "", (0, 0)),
        ("short", "longpattern", None),  # шаблон длиннее текста
        ("aaaa", "aa", (0, 2)),  # первое вхождение
        ("абракадабра", "бра", (1, 4)),  # кириллица
        ("no matches here", "xyz", None),
    ],
)
def test_search_first(text, pattern, expected):
    assert KMPService.search_first(text, pattern) == expected
