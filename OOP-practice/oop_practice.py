from datetime import datetime

# ----- MENU STUFF -----
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def get(self, name):
        for i in self.items:
            if i.name == name:
                return i
        return None

# ----- PEOPLE -----
class Customer:
    def __init__(self, name, birthday=False):
        self.name = name
        self.birthday = birthday

class Waiter:
    def __init__(self, name):
        self.name = name

    def take_order(self, cust):
        return Order(cust, self)

# ----- ORDER -----
class Order:
    def __init__(self, cust, waiter):
        self.cust = cust
        self.waiter = waiter
        self.items = []
        self.pricing = Standard()

    def add_item(self, item):
        self.items.append(item)

    def set_pricing(self, pricing):
        self.pricing = pricing

    def total(self):
        return self.pricing.calc(self.items, self.cust)

    def pay(self):
        t = self.total()
        return Receipt(self, t)

# ----- RECEIPT -----
class Receipt:
    def __init__(self, order, total):
        self.order = order
        self.total = total
        self.time = datetime.now()

    def print_it(self):
        print("Customer:", self.order.cust.name)
        print("Waiter:", self.order.waiter.name)
        for it in self.order.items:
            print(it.name, "-", it.price)
        print("TOTAL:", self.total)
        print("TIME:", self.time)

# ----- RESTAURANT -----
class Rest:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.waiters = []

    def add_waiter(self, w):
        self.waiters.append(w)

# ----- PRICING -----
class Pricing:
    def calc(self, items, cust):
        t = 0
        for i in items:
            t += i.price
        return t

class Standard(Pricing):
    pass

class Birthday(Pricing):
    def calc(self, items, cust):
        t = 0
        for i in items:
            t += i.price
        if cust.birthday:
            t *= 0.8
        return t

class Lunch(Pricing):
    def calc(self, items, cust):
        t = 0
        for i in items:
            t += i.price
        t *= 0.9
        return t

# ----- PAYMENT -----
class Payment:
    def pay(self, amount):
        print("Paid:", amount)

# ----- DEMO -----
r = Rest("CafeX")
w1 = Waiter("Ali")
r.add_waiter(w1)

p1 = Item("Pizza", 100)
p2 = Item("Burger", 80)
p3 = Item("Cola", 20)

r.menu.add(p1)
r.menu.add(p2)
r.menu.add(p3)

c1 = Customer("Alper", birthday=True)
o1 = w1.take_order(c1)
o1.add_item(p1)
o1.add_item(p3)

o1.set_pricing(Birthday())
print("Total:", o1.total())

pay = Payment()
pay.pay(o1.total())

rec = o1.pay()
rec.print_it()

# extra normal price
o1.set_pricing(Standard())
print("Normal price:", o1.total())
