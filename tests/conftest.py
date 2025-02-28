import pytest

from src.product_class import Product
from src.category_class import Category


@pytest.fixture
def second_cat():
    return Category(
        name="Не хлеб",
        description="Все кроме хлеба",
        products=[
            Product("Пейджер", "Работает до сих пор", "15,3", "3"),
            Product(
                "Стаканы на веревках",
                "Связь ограничена длинной веревки",
                "0,15",
                "1000",
            ),
        ],
    )


@pytest.fixture
def first_cat():
    return Category(
        name="Хлебные изделия",
        description="Все для набора веса если ты дистрофик",
        products=[
            Product("Булочка с маком", "Мало мака", 3.30, 10),
            Product("Буханка белого", "Вкусно с молоком", 1.50, 3),
        ],
    )


@pytest.fixture
def product():
    return Product("Пейджер", "Работает до сих пор", 15.3, 3)

@pytest.fixture
def for_test_new_product():
    return Product("Просто пион", "Подарок подруге", 122.0, 3)

@pytest.fixture
def one_category():
    product1 = Product("a", "b", 1.0, 1)
    product2 = Product("c", "d", 2.0, 2)
    product3 = Product("e", "f", 3.0, 3)
    category = Category("abc", "def", [product1, product2, product3])
    return category