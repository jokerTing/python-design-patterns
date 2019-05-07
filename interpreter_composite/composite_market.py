class Tab(object):
    def __init__(self, customer):
        self.items = [] #商品
        self.discount = [] #优惠金额
        self.customer = customer

    def calculate_cost(self):
        return sum(x.cost for x in self.items)

    def calculate_discount(self):
        return sum(x for x in self.discount)
'''
class Discounts(object):
    def __init__(self):
        self.children = []

    def calculate(self, tab):
        return sum(x.calculate(tab) for x in self.children)

    def add(self, child):
        self.children.append(child)
    
    def remove(self, child):
        self.children.remove(child)

class Discount(object):
    def __init__(self, test_function, discount_function):
        self.test = test_function
        self.discount = discount_function
    
    def calculate(self, tab):
        return sum(self.discount(item) 
            for item in tab.items if self.test(item))
'''        
class Discount(object):
    def __init__(self, amount):
        self.amount = amount

class Item(object):
    def __init__(self, name, item_type, cost): 
        self.name = name
        self.item_type = item_type
        self.cost = cost
    
class ItemType(object):
    def __init__(self, name):
        self.name = name

class Customer(object):
    def __init__(self, customer_type, name):
        self.customer_type = customer_type
        self.name = name
    
    def is_a(self, customer_type):
        return self.customer_type == customer_type

class CustomerType(object):
    def __init__(self, customer_type):
        self.customer_type = customer_type

class AndConditions(object):
    def __init__(self):
        self.conditions = []
    
    def evaluate(self, tab):
        return all(x.evaluate(tab) for x in self.conditions)
    
    def add(self, condition):
        self.conditions.append(condition)
    
    def remove(self, condition):
        self.conditions.remove(condition)

class OrConditions(object):
    def __init__(self):
        self.conditions = []
    
    def evaluate(self, tab):
        return any(x.evaluate(tab) for x in self.conditions)
    
    def add(self, condition):
        self.conditions.append(condition)
    
    def remove(self, condition):
        self.conditions.remove(condition)

class condition(object):
    def __init__(self, condition_function):
        self.test = condition_function
    
    def evaluate(self, tab):
        return self.test(tab)

class Rule(object):
    def __init__(self, tab):
        self.tab = tab
        #self.conditions = AndConditions()
        #self.discounts = Discounts()
        self.conditions = []
        self.discounts = []
    
    def add_condition(self, conditions):
        #self.conditions.add(conditions)
        self.conditions.append(conditions)
    '''
    def add_discount(self, test_function, discount_function):
        discount = Discount(test_function, discount_function)
        self.discounts.add(discount)
    '''
    def add_percentage_discount(self, item_type, percent):
        if item_type == "any item":
            f = lambda x: True
        else:
            f = lambda x: x.item_type == item_type
        #折扣商品
        items_to_discount = [item for item in self.tab.items if f(item)]
        for item in items_to_discount:
            discount = Discount(item.cost * (percent/100.0))
            self.discounts.append(discount)
    
    def apply(self):
        if all(self.conditions):
            return sum(x.amount for x in self.discounts)
        return 0
    
if __name__ == "__main__":
    member = CustomerType("Member")
    member_customer = Customer(member, "John")
    tab = Tab(member_customer)

    pizza = ItemType("pizza")
    burger = ItemType("burger")
    drink = ItemType("drink")

    tab.items.append(Item("Margarita", pizza, 15))
    tab.items.append(Item("Cheddar Melt", burger, 6))
    tab.items.append(Item("Latte", drink, 4))
    # Members always get 15% off their total tab
    rule = Rule(tab)
    rule.add_condition(tab.customer.is_a(member))
    rule.add_percentage_discount("any item", 15)

    tab.discount.append(
        rule.apply()
    )

    print (
        "Calculated cost: {}\nDiscount applied: {}\n{}% Discount applied".
        format(
            tab.calculate_cost(),
            tab.calculate_discount(),
            100 * tab.calculate_discount() / tab.calculate_cost()
        )
    )
