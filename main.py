from utils.stock_handler import Stock, Product, stock_dummy
from utils.cart_handler import Cart, CashRegister, cart_dummy


# új termék létrehozása
prod = Product("alma", 50, 4)
prod2 = Product("banán", 60, 2)

# új termék hozzáadása a készlethez
sto = Stock(prod.create_new_product, stock_dummy)
sto = Stock(prod2.create_new_product, stock_dummy)

# kosár létrehozása
cart = Cart(sto.complet_set, "kenyér", 2)
cart2 = Cart(sto.complet_set, "tej", 1)
cart3 = Cart(sto.complet_set, "csoki", 2)
cart4 = Cart(sto.complet_set, "banán", 2)
cart5 = Cart(sto.complet_set, "alma", 3)

# blokk generálás
recipe = CashRegister()
recipe.generate_receipt(cart_dummy)
