stock_dummy = [
    {"product_name": "kenyér", "price": 400, "quantity": 3},
    {"product_name": "tej", "price": 500, "quantity": 3},
    {"product_name": "csoki", "price": 200, "quantity": 7}
]


class Product:
    """
    Létrehoz egy új terméket, amit hozzá lehet adni a stock_dummy-hoz
    """

    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity
        self.create_new_product = self.create_product()

    def create_product(self):
        self.new_product = {
            "product_name": self.product,
            "price": float(self.price),
            "quantity": int(self.quantity)
        }
        return self.new_product


class Stock:
    """
    Hozzáadja a létrehozott terméket a stock_dummy-hoz
    """

    def __init__(self, product, complet_set=list):
        self.product = product
        self.complet_set = complet_set
        self.stock = self.add_product_to_stock()

    def add_product_to_stock(self):
        self.complet_set.append(self.product)
