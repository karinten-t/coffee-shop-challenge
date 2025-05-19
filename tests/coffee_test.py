import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee:
    def test_coffee_init(self):
        cof = Coffee("Latte")
        assert cof.name == "Latte"

    def test_coffee_name_validation(self):
        with pytest.raises(TypeError):
            Coffee(123)
        with pytest.raises(ValueError):
            Coffee("A")
        cof = Coffee("Latte")
        with pytest.raises(AttributeError):
            cof.name = "Mocha"

    def test_coffee_orders(self):
        cof = Coffee("Latte")
        c = Customer("Alice")
        o = Order(c, cof, 5.0)
        assert o in cof.orders()

    def test_coffee_customers(self):
        cof = Coffee("Latte")
        c1 = Customer("Alice")
        c2 = Customer("Bob")
        Order(c1, cof, 5.0)
        Order(c2, cof, 6.0)
        assert c1 in cof.customers()
        assert c2 in cof.customers()

    def test_num_orders(self):
        cof = Coffee("Latte")
        c = Customer("Alice")
        Order(c, cof, 5.0)
        Order(c, cof, 6.0)
        assert cof.num_orders() == 2

    def test_average_price(self):
        cof = Coffee("Latte")
        c = Customer("Alice")
        Order(c, cof, 5.0)
        Order(c, cof, 7.0)
        assert cof.average_price() == 6.0