from store.models import Book

class Cart():
    def __init__(self, request):
        self.session = request.session
        self.request = request
        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # make sure cart is available on all pages
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        quantity = str(quantity)
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.UnitPrice) }
            self.cart[product_id] = int(quantity)
        self.session.modified = True

    def cart_total(self):
        product_ids = self.cart.keys()
        products = Book.objects.filter(id__in = product_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    total = total + (product.UnitPrice * value)
        return total

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids = self.cart.keys()
        products = Book.objects.filter(id__in = product_ids)
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

		# Get cart
        ourcart = self.cart
		# Update Dictionary/cart
        ourcart[product_id] = product_qty

        self.session.modified = True
	

		# Deal with logged in user
        # if self.request.user.is_authenticated:
		# 	# Get the current user profile
        #     current_user = Profile.objects.filter(user__id=self.request.user.id)
		# 	# Convert {'3':1, '2':4} to {"3":1, "2":4}
        #     carty = str(self.cart)
        #     carty = carty.replace("\'", "\"")
		# 	# Save carty to the Profile Model
        #     current_user.update(old_cart=str(carty))


        thing = self.cart
        return thing

    def delete(self, product):
        product_id = str(product)
		# Delete from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

		# # Deal with logged in user
        # if self.request.user.is_authenticated:
		# 	# Get the current user profile
        #     current_user = Profile.objects.filter(user__id=self.request.user.id)
		# 	# Convert {'3':1, '2':4} to {"3":1, "2":4}
        #     carty = str(self.cart)
        #     carty = carty.replace("\'", "\"")
		# 	# Save carty to the Profile Model
        #     current_user.update(old_cart=str(carty))