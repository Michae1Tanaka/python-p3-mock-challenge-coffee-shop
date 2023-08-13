class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 2:
            self._name = name
        else:
            raise Exception(
                "Name must be a string and its length must be greater than 2 characters."
            )
        self._orders = list()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_coffee):
        if hasattr(self, "_name"):
            raise Exception("You cannot change the name of the coffee.")
        else:
            self._name = new_coffee

    def orders(self, new_order=None):
        if isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders

    def customers(self, new_customer=None):
        return list(set([order.customer for order in self._orders]))

    def num_orders(self):
        orders = [order.coffee for order in self._orders if order.coffee == self]
        return len(orders)
        # or
        # counter = 0
        # for order in self._orders:
        # if order.coffee == self:
        # counter += 1
        # return counter
        # Not sure which is better since the larger the amount of orders, the more space a list takes.

    def average_price(self):
        order_prices = [order.price for order in self._orders]
        return sum(order_prices) / len(order_prices)


from classes.order import Order
