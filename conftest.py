import pytest
from main import BooksCollector


# фикстура для добавления новой книги
@pytest.fixture(scope="function")
def collector():
    return BooksCollector()