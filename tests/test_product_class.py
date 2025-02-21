from src.product_class import Product
from src.category_class import Category


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
    assert Category.product_count == 4


def test_str_product(product):
    assert str(product) == "Пейджер, 15.3 руб. Остаток: 3 шт."