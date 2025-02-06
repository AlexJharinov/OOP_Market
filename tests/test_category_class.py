

def test_category_class(first_cat, second_cat):
    assert second_cat.name == "Не хлеб"
    assert second_cat.description == "Все кроме хлеба"
    assert len(second_cat.products) == 2

    assert second_cat.category_count == 2

    assert  first_cat.product_count == 4
    assert second_cat.product_count == 4