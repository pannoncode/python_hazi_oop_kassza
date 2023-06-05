from utils.stock_handler import Stock, Product
from utils.cart_handler import Cart, CashRegister, cart_dummy
from utils.db_handler import StockHandler


# új termék létrehozása
prod = Product("kenyér", 400, 3)
prod2 = Product("tej", 500, 3)
prod3 = Product("csoki", 200, 7)


# új termék hozzáadása a készlethez
sto1 = Stock(prod.create_new_product)
sto2 = Stock(prod2.create_new_product)
sto3 = Stock(prod3.create_new_product)


# # kosár létrehozása
# cart = Cart(sto.complet_set, "kenyér", 2)
# cart2 = Cart(sto.complet_set, "tej", 1)
# cart3 = Cart(sto.complet_set, "csoki", 2)
# cart4 = Cart(sto.complet_set, "banán", 2)
# cart5 = Cart(sto.complet_set, "alma", 3)

# # blokk generálás
# recipe = CashRegister()
# recipe.generate_receipt(cart_dummy)
