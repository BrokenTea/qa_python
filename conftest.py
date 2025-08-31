import pytest
from main import BooksCollector # Импортируем ваш класс

# Фикстура для создания экземпляра BooksCollector перед каждым тестом
@pytest.fixture
def collector():
    return BooksCollector()