
import utility

# import shopping.more_shopping.shopping_cart
# print(shopping.more_shopping.shopping_cart.buy('apple'))
# print(shopping.more_shopping.shopping_cart)


# from shopping.more_shopping.shopping_cart import buy
from shopping.more_shopping import shopping_cart

print(utility.divide(2, 3))

print(shopping_cart.buy('apple'))

print(shopping_cart.buy)

print("In the module main :", __name__)

if __name__ == '__main__':
    print("This should be the __main__ module :", __name__)