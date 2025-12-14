import pytest

from algorithms_exam.src.service.jaccard_service import JaccardService


@pytest.fixture
def jaccard_service():
    return JaccardService()


def test_split_text_to_shingles(jaccard_service):
    shingles = jaccard_service._split_text_to_shingles("redmi note")

    assert shingles == {"red", "edm", "dmi", "mi ", "i n", " no", "not", "ote"}
