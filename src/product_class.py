class Product:
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_element):
        """ Создает объект класса из словаря """

        name = new_element["name"]
        description = new_element["description"]
        price = new_element["price"]
        quantity = new_element["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """ Возвращает приватный атрибут "price" """

        return self.__price

    @price.setter
    def price(self, cost):
        """ Проверяет "price" на положительность """

        if cost <= 0:
            print("Цена не должна быть нулевая или отрицательная")

        else:
            self.__price = cost

    def __str__(self):
        """ Выводит строку с именем, ценой и колличеством продукта """

        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."






