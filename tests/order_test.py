import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder:
    def test_order_init(self):
        c = Customer("Alice")
        cof = Coffee("Latte")
        o = Order(c, cof, 5.0)
        assert o.customer == c
        assert o.coffee == cof
        assert o.price == 5.0

    def test_order_price_validation(self):
        c = Customer("Alice")
        cof = Coffee("Latte")
        with pytest.raises(TypeError):
            Order(c, cof, "5")
        with pytest.raises(ValueError):
            Order(c, cof, 0.5)
        o = Order(c, cof, 5.0)
        with pytest.raises(AttributeError):
            o.price = 6.0

    def test_order_relationships(self):
        c = Customer("Alice")
        cof = Coffee("Latte")
        o = Order(c, cof, 5.0)
        assert o in c.orders()
        assert o in cof.orders()