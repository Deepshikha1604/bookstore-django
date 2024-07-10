from .cart import Cart

# create context processor so are cart works on all pages
def cart(request):
    #return default data from our cart
    return{'cart': Cart(request)}