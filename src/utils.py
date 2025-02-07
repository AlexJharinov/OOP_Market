import os
import json

from src.category_class import Category
from src.product_class import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as f:
        data = json.load(f)
    return data


def creat_objects(data):
    category_list = []
    for cat in data:
        prod = []
        for p in cat["products"]:
            prod.append(Product(**p))
        cat["products"] = prod
        category_list.append(Category(**cat))

    return category_list


if __name__ == "__main__":
    prod_and_cat = read_json("../data/products.json")
    category_data = creat_objects(prod_and_cat)
    print(category_data)
    print(category_data[0].name)
    print(category_data[0].products)
