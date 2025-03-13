import pytest

from src.product_class import Product
from src.category_class import Category


from src.product_class import LawnGrass, Smartphone



def test_product_class_init(product):
    assert product.name == "Пейджер"
    assert product.description == "Работает до сих пор"
    assert product.price == 15.3
    assert product.quantity == 3


def test_new_product(for_test_new_product):
    assert for_test_new_product.name == "Просто пион"
    assert for_test_new_product.description == "Подарок подруге"
    assert for_test_new_product.price == 122.0
    assert for_test_new_product.quantity == 3


def test_add_product_to_category():
    product1 = Product("a", "b", 1.0, 1)
    product2 = Product("c", "d", 2.0, 2)
    product3 = Product("e", "f", 3.0, 3)
    category = Category("abc", "def", [product1, product2, product3])
    product4 = Product("g", "i", 4.0, 4)
    category.add_product(product4)
    assert Category.product_count == 14


def test_str_product(product):
    assert str(product) == "Пейджер, 15.3 руб. Остаток: 3 шт."

def test_add_product(product, for_test_new_product):
    assert product + for_test_new_product == 411.9


def test_invalid_add_product():
    with pytest.raises(TypeError):
        Category.add_product("Что-то не то")

def test_init_smartphone():
    phone_for_test = Smartphone("Samsung Galaxy S23 Ultra",
                                "256GB, Серый цвет," "200MP камера",
                                180000.0, 5, 95.5,
                                "S23 Ultra", 256, "Серый")
    assert phone_for_test.efficiency == 95.5
    assert phone_for_test.model == "S23 Ultra"
    assert phone_for_test.memory == 256
    assert phone_for_test.color == "Серый"


def test_init_lawn_grass():
    grass_for_test = LawnGrass("Газонная трава",
                               "Элитная трава для газона", 500.0, 20,
                               "Россия", "7 дней", "Зеленый")
    assert grass_for_test.country == "Россия"
    assert grass_for_test.germination_period == "7 дней"
    assert grass_for_test.color == "Зеленый"