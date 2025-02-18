


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