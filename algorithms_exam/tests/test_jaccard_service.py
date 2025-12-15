import pytest

from algorithms_exam.src.service.jaccard_service import JaccardService


@pytest.fixture
def jaccard_service():
    return JaccardService()


def test_split_text_to_shingles(jaccard_service):
    shingles = jaccard_service._split_text_to_shingles("redmi note")

    assert shingles == {"red", "edm", "dmi", "mi ", "i n", " no", "not", "ote"}


@pytest.mark.parametrize("first,second,expected", [
    ('смартфон xiaomi redmi note 12 pro 8 256gb синий',
     'xiaomi redmi note 12 pro 8 256 синий',
     0.67
     ),
    ('смартфон xiaomi redmi note 12 pro 8 256gb синий',
     "",
     0
     ),
    ('',
     "смартфон xiaomi redmi note 12 pro 8 256gb синий",
     0
     ),
    (
            "",
            "",
            1.0
    ),
    ("kitten",
     "sitting",
     0.12)
])
def test_get_similarity(first, second, expected, jaccard_service):
    assert jaccard_service.get_similarity(first, second) == expected
