import datetime
WEEK_DAY = ["Monday", 
            "Tuesday", 
            "Wednesday", 
            "Thursday",
            "Friday", 
            "Saturday", 
            "Sunday"]

class Rule(object):
    def __init__(self, conditions, discounts):
        self.conditions = conditions
        self.discounts = discounts
    
    def evaluate(self, tab):
        if self.conditions.evaluate(tab):
            return self.discounts.calculate(tab)
        return 0
'''
class Conditions(object):
    def __init__(self, expression):
        self.expression = expression
    
    def evaluate(self, tab):
        return self.expression.evaluate(tab)
'''    
class And(object):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2
    
    def evaluate(self, tab):
        return self.expression1.evaluate(tab) and self.expression2.evaluate(tab)
    
class Or(object):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2
    
    def evaluate(self, tab):
        return self.expression1.evaluate(tab) or self.expression2.evaluate(tab)

class PercentageDiscount(object):
    def __init__(self, item_type, percentage):
        self.item_type = item_type
        self.percentage = percentage
    
    def calculate(self, tab):
        cost_list = []
        for x in tab.items:
            if x.item_type == self.item_type or self.item_type == "any_item":
                cost_list.append(x.cost)
        discount = (sum(cost_list) * self.percentage) / 100
        return discount

class CheapestFree(object):
    def __init__(self, item_type):
        self.item_type = item_type
    
    def calculate(self, tab):
        try:
            return min([x.cost for x in tab.items if x.item_type == 
            self.item_type])
        except:
            return 0

class TodayIs(object):
    def __init__(self, day_of_week):
        self.day_of_week = day_of_week

    def evaluate(self, tab):
        return WEEK_DAY[datetime.datetime.today().weekday()] == self.day_of_week.name
    
class TimeIsBetween(object):
    def __init__(self, from_time, to_time):
        self.from_time = from_time
        self.to_time = to_time
    
    def evaluate(self, tab):
        hour_now = datetime.datetime.today().hour
        minute_now = datetime.datetime.today().minute
        from_hour, from_minute = [int(x) for x in self.from_time.split(":")]
        to_hour, to_minute = [int(x) for x in self.to_time.split(":")]

        hour_in_range = from_hour <= hour_now < to_hour
        begin_edge = hour_now == from_hour and minute_now > from_minute
        end_edge = hour_now == to_hour and minute_now < to_minute

        return any([hour_in_range, begin_edge, end_edge])

class TodayIsAWeekDay(object):
    def __init__(self):
        pass

    def evaluate(self, tab):
        week_days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
        ]
        print(datetime.datetime.today().weekday())
        return WEEK_DAY[datetime.datetime.today().weekday()] in week_days

class TodayIsAWeekedDay(object):
    def __init__(self):
        pass
    
    def evaluate(self, tab):
        weekend_days = [
            "Saturday",
            "Sunday"
        ]
        return WEEK_DAY[datetime.datetime.today().weekday()] in weekend_days

class DayOfTheWeek(object):
    def __init__(self, name):
        self.name = name

class ItemIsA(object):
    def __init__(self, item_type):
        self.item_type = item_type
    
    def evaluate(self, item):
        return self.item_type == item.item_type
    
class NumberOfItemsOfType(object):
    def __init__(self, item_type, number_of_items):
        self.number = number_of_items
        self.item_type = item_type
    
    def evaluate(self, tab):
        return len([x for x in tab.items if x.item_type == self.item_type]) == self.number

class CustomerIsA(object):
    def __init__(self, customer_type):
        self.customer_type = customer_type
    
    def evaluate(self, tab):
        return tab.customer.customer_type == self.customer_type

class Tab(object):
    def __init__(self, customer):
        self.items = []
        self.discounts = []
        self.customer = customer
    
    def calculate_cost(self):
        return sum(x.cost for x in self.items)
    
    def calculate_discount(self):
        return sum(x for x in self.discounts)

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
    
class CustomerType(object):
    def __init__(self, customer_type):
        self.customer_type = customer_type

member = CustomerType("Member")
pizza = ItemType("pizza")
burger = ItemType("Burger")
drink = ItemType("Drink")

monday = DayOfTheWeek("Monday")
    
def setup_demo_tab():
    member_customer = Customer(member, "John")
    tab = Tab(member_customer)

    tab.items.append(Item("Margarita", pizza, 15))
    tab.items.append(Item("Cheddar Melt", burger, 6))
    tab.items.append(Item("Hawaian", pizza, 12))
    tab.items.append(Item("Latte", drink, 4))
    tab.items.append(Item("Club", pizza, 17))
    tab.items.append(Item("Cheddar Melt2", burger, 6))

    return tab

if __name__ == "__main__":
    tab = setup_demo_tab()

    rules = []

    # Members always get 15% off their total tab
    rules.append(
        Rule(
            CustomerIsA(member),
            PercentageDiscount("any_item", 15)
        )
    )

    # During happy hour,which happens from 17:00 to 19:00 weekdays, all drinks are less 10%
    rules.append(
        Rule(
            And(TimeIsBetween("17:00", "22:00"), TodayIsAWeekDay()),
            PercentageDiscount(drink, 10)
        )
    )

    # Mondays are buy one get one free burger nights
    rules.append(
        Rule(
            And(TodayIs(monday), NumberOfItemsOfType(burger, 2)),
            CheapestFree(burger)
        )
    )

    for rule in rules:
        tab.discounts.append(rule.evaluate(tab))
    
    print(
        "Calculated cost: {}\nDiscount applied: {}\n".format(
            tab.calculate_cost(),
            tab.calculate_discount()
        )
    )