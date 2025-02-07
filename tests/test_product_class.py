def test_product_class_init(product):
    assert product.name == "Пейджер"
    assert product.description == "Работает до сих пор"
    assert product.price == "15,3"
    assert product.quantity == "3"
