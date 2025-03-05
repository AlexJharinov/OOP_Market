from src.product_class import Product


def test_print_mixin(capsys):
    Product("Пейджер", "Работает до сих пор", 15.3, 3)
    message = capsys.readouterr()
    assert message.out == 'Product, Пейджер, Работает до сих пор, 15.3, 3\n'