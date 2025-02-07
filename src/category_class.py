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
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
