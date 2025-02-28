import pytest
from src.category_class import Category




def test_category_class(first_cat, second_cat):
    assert second_cat.name == "Не хлеб"
    assert second_cat.description == "Все кроме хлеба"

    assert second_cat.category_count == 2

    assert first_cat.product_count == 4
    assert second_cat.product_count == 4


def test_add_product(product, for_test_new_product):
    assert product + for_test_new_product == 137.3


def test_invalid_add_product():
    with pytest.raises(TypeError):
        Category.add_product("Что-то не то")




