
from src.product_class import Product



class Category:
    """Класс для работы с категориями"""

    category_count = 0
    product_count = 0

    name = str
    description = str
    products = list

    def __init__(self, name, description, products):
        """Функция инициализации категории"""

        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)



    def add_product(self, product: Product):
        """ Метод добавляющий новый продукт """

        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError






