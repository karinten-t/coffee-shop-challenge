import pytest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer:
    def test_customer_init(self):
        c = Customer("Alice")
        assert c.name == "Alice"

    def test_customer_name_validation(self):
        with pytest.raises(TypeError):
            Customer(123)
        with pytest.raises(ValueError):
            Customer("")
        with pytest.raises(ValueError):
            Customer("ThisNameIsWayTooLong")

    def test_customer_orders(self):
        c = Customer("Alice")
        cof = Coffee("Latte")
        o = Order(c, cof, 5.0)
        assert o in c.orders()

    def test_customer_coffees(self):
        c = Customer("Alice")
        cof1 = Coffee("Latte")
        cof2 = Coffee("Cappuccino")
        Order(c, cof1, 5.0)
        Order(c, cof2, 4.5)
        assert cof1 in c.coffees()
        assert cof2 in c.coffees()