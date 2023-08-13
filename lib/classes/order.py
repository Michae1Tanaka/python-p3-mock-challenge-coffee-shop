class Order:
    all = list()

    def __init__(self, customer, coffee, price):
        self._customer = None
        self._coffee = None

        self.customer = customer
        self.coffee = coffee

        if 1.0 <= price <= 10.0 and isinstance(price, float):
            self._price = price
        else:
            raise Exception("Price must be in between 0 and 11 and must be a float.")

        coffee.orders(self)
        coffee.customers(customer)
        customer.orders(self)
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("customer must be instances of the Customer class.")

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception("coffee must be instances of the Coffee class.")


from classes.customer import Customer
from classes.coffee import Coffee
