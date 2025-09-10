# Scenario:
# You are building the backend logic of a product and order management system for an e-commerce platform like Amazon or Flipkart. 
# The system needs to handle products, users, payments, discounts, and different order behaviors dynamically.

# Q1. Product Search System (Static Polymorphism) 
# Problem Statement:
# Implement a class ProductSearch that allows searching products with different combinations of criteria (name, category, price range). 
# Requirements: 
# Use default arguments and/or *args, **kwargs to simulate method overloading. 
# Allow the following types of searches: 
# Only by name 
# Name and category 
# Name, category, and price range 

class ProductSearch:
    def __init__(self, products):
        self.products = products 

    def search(self, name=None, category=None, price_range=None):
        results = self.products
        result= "Not Found"

        if name and category and price_range:
            min_price, max_price = price_range
            for p in results:
                if min_price <= p['price'] <= max_price:
                    result= "Found"
                    break
        elif name and category and not price_range:
            for p in results:
                if  p['category'].lower() == category.lower() and  p['name'].lower() == name.lower():
                    result= "Found"
                    break
        elif name and not category and not price_range:
              for p in results:
                if  p['name'].lower() == name.lower():
                    result= "Found"
                    break
        
        return result

products = [
    {"name": "Laptop", "category": "Electronics", "price": 800},
    {"name": "Pizza", "category": "Food", "price": 150},
    {"name": "Mobile", "category": "Electronics", "price": 500},
]

searcher = ProductSearch(products)
print(f"Products search with name:{searcher.search('Laptop')}")
print(f"Products search with name: Phone and category: Electronics:{searcher.search('Phone','Electronics')}")
print(f"Products search  with name: Mobile, category: Electronics and within price range: (100,200) {searcher.search('Mobile', 'Electronics', (100, 200))}")



# Q2. Cart System with Quantity Variations (Static Polymorphism) 
# Problem Statement:
# Design a class Cart that can add multiple products with variable quantities using *args or **kwargs. 
# Requirements: 
# Add multiple products at once with name and quantity 
# Simulate static polymorphism using variable arguments 
 
class Cart:
    def __init__(self):
        self.items = {}  # {product_name: quantity}

    def add_products(self, **kwargs):
        for product, quantity in kwargs.items():
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity

    def view_cart(self):
        return self.items


cart = Cart()
cart.add_products(Phones=15)
print(f"Total Products added:{len(cart.view_cart())}")
cart.add_products(Lights=10, Batteries =30)
print(f"Total Products added:{len(cart.view_cart())}")
cart.add_products(Pens=11, Pencils=8, Eraser=40)
print(f"Total Products added:{len(cart.view_cart())}")



# Q3. Discount Application (Static Polymorphism) 
# Problem Statement:
# Create a class Discount that allows applying different types of discounts: 
# Flat discount 
# Percentage discount 
# Buy One Get One 
# Use static polymorphism to overload the method using default parameters or *args
 
class Discount:
    def apply_discount(self, amount, flat=None, percent=None, buyGet_quantity=None, price_per_item=None):
        if flat is not None:
            return amount - flat
        elif percent is not None:
            return amount * (percent / 100)
        elif buyGet_quantity is not None and price_per_item is not None:
            payable_items = (buyGet_quantity // 2) + (buyGet_quantity % 2)
            return payable_items * price_per_item
        else:
            return amount

discount = Discount()
print(f"{discount.apply_discount(amount=50,flat = 10)}")
print(f"{discount.apply_discount(amount=1000, percent=10)}")
print(f"{discount.apply_discount(amount=0,buyGet_quantity= 2, price_per_item=2)}")

# Q4. Payment System (Dynamic Polymorphism) 
# Problem Statement:
# Implement a base class Payment and subclasses CreditCardPayment, UPIPayment, and CODPayment. Each should override a method pay(). 
# Requirements: 
# Override pay() method in each class to simulate different payment methods

class Payment:
    def pay(self, amount):
        print(f"Payment {amount}")
    
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class UPIPayment(Payment):
    def pay(self, amount):
       print(f"Paid {amount} using UPI.")

class CODPayment(Payment):
    def pay(self, amount):
        print(f"Pay {amount} on order delivery.")


payment = Payment()
payment.pay(2000)

payment = CreditCardPayment()
payment.pay(2000)

payment = UPIPayment()
payment.pay(2000)

payment = CODPayment()
payment.pay(2000)
