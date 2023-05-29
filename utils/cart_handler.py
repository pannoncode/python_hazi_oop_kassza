cart_dummy = []


class Cart:
    """
    stock - az aktuális készlet
    cart_item - a kosárba helyezett termék
    cart_quantity - a vásárolni kívánt mennyiség
    """

    def __init__(self, stock, cart_item, cart_quantity):
        self.stock = stock
        self.cart_item = cart_item
        self.cart_quantity = cart_quantity
        self.check_item = self.check_stock_product()
        self.add_cart_item = self.add_item_to_cart()

    def check_stock_product(self):
        """
        Egy egyszerű ellenőrzés, hogy létezik e ilyen termék a készleten és, hogy van e
        belőle a megvásárolni kívánt mennyiség
        """
        for item in self.stock:
            if item["product_name"] == self.cart_item and item["quantity"] >= self.cart_quantity:
                return True
            else:
                continue

        return False

    def add_item_to_cart(self):
        """
        (Ezt nem tudom okosabban)
        Ha a check_stock_product True-val jön vissza akkor létrehozza a kosárba adandó terméket,
        hozzá adja a kosárhoz és utána a stock mennyiségből kivonja a megvásárolt mennyiséget
        """
        if self.check_item:
            for item in self.stock:
                if item["product_name"] == self.cart_item:
                    self.cart_item = {
                        "cart_prod_name": item["product_name"],
                        "cart_prod_quantity": self.cart_quantity,
                        "cart_prod_price_one_item": item["price"],
                        "cart_prod_price_all_item": item["price"] * self.cart_quantity
                    }
                    cart_dummy.append(self.cart_item)
                    item["quantity"] -= self.cart_quantity


class CashRegister:
    def generate_receipt(self, cart):
        cart_items = []
        cart_prices_nett = 0
        cart_prices_brut = 0
        for cartitem in cart:
            item = str(cartitem["cart_prod_quantity"]) + "db " + str(
                cartitem["cart_prod_name"]) + " - " + str(cartitem["cart_prod_price_one_item"])+"Ft/db"
            cart_prices_nett += cartitem["cart_prod_price_all_item"]
            cart_prices_brut += cartitem["cart_prod_price_all_item"] * 1.18
            cart_items.append(item)
        print(f"A blokk tartamla {cart_items}")
        print(f"A Nettó összeg: {cart_prices_nett} Ft")
        print(f"A Bruttó összeg: {cart_prices_brut} Ft")
