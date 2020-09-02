def buy(item):
    cart = []
    cart.append(item)
    return cart

print("In the module shopping_cart :", __name__)

if __name__ == '__main__':
    print("This should be the __main__ module :", __name__)