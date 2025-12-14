import pytest

from algorithms_exam.src.service.string_service import StringService


@pytest.fixture
def string_service():
    return StringService()


@pytest.mark.parametrize("input_text,expected", [
    ("Xiaomi Redmi Note 12", "xiaomi redmi note 12"),
    ("  multiple   spaces  here ", "multiple spaces here"),
    ("Redmi!!! Note??? 12...", "redmi note 12"),
    ("S10+ Ultra", "s10+ ultra"),
    ("8/256GB", "8 256gb"),
    ("Планшет IRBIS TX97 10.1\"", "планшет irbis tx97 10 1"),
    ("!!!@@@", ""),
])
def test_string_service_normalize(input_text, expected, string_service):
    result = string_service.normalize(input_text)

    assert result == expected
