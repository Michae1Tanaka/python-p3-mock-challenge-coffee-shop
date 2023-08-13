class Customer:
    def __init__(self, name):
        if isinstance(name, str) and 0 < len(name) <= 15:
            self._name = name
        else:
            raise Exception(
                "Name must be a string and the length must be in between 0 and 16 characters."
            )

        self._orders = list()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 0 < len(new_name) <= 15:
            self._name = new_name
        else:
            raise Exception(
                "Your new name must be a string and the length must be in between 0 and 16 characters."
            )

    def orders(self, new_order=None):
        if isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders

    def coffees(self):
        return list(set([order.coffee for order in self._orders]))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)


from classes.order import Order
