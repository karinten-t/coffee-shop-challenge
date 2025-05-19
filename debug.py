from customer import Customer
from coffee import Coffee
from order import Order

def debug_relationships():
    # Clear previous data
    Order.all.clear()
    Coffee.all.clear()
    
    # Create instances
    c1 = Customer("Alice")
    c2 = Customer("Bob")

    cof1 = Coffee("Latte")
    cof2 = Coffee("Cappuccino")

    o1 = Order(c1, cof1, 5.0)
    o2 = Order(c1, cof2, 4.5)
    o3 = Order(c2, cof1, 6.0)

    # Test relationships
    print(f"{c1.name}'s orders: {[o.coffee.name for o in c1.orders()]}")
    print(f"{cof1.name} customers: {[c.name for c in cof1.customers()]}")
    print(f"{cof1.name} average price: {cof1.average_price()}")

if __name__ == "__main__":
    debug_relationships()