class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        if hasattr(self, '_price'):
            raise AttributeError("Price cannot be changed after initialization")
        self._price = value

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from customer import Customer  # Import here to avoid circular import
        if not isinstance(value, Customer):
            raise TypeError("Customer must be of type Customer")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee  # Import here to avoid circular import
        if not isinstance(value, Coffee):
            raise TypeError("Coffee must be of type Coffee")
        self._coffee = value