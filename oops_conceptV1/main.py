import csv

# creating a class
# methods (function) inside in a class
class Item:
    true_pay_factor = 0.8   # 20% discount to items
    all = []

    # assigned quantity default as 0
    # assigned data types for all the arguments - ": str / : int"
    def __init__(self, Name: str, Price: float, Quantity=0.0):

        # print(f"An instance has been created", {Name})
        # Run validations to the received arguments
        assert Price >= 0, f"Price {Price} is less than zero!"
        assert Quantity >= 0, f"Quantity {Quantity} is less than zero!"
        # assign to self project
        self.Name = Name
        self.Price = Price
        self.Quantity = Quantity

        # Detailed description of attributes and total stock price
        # comment
        '''print(f"Details of the instance:", "\n",
              "Product Name - ", self.Name, "\n",
              "Price - ", self.Price, "\n",
              "Quantity - ", self.Quantity)
        print("Total Stock Value: ", self.Price * self.Quantity)'''
        # comment

        Item.all.append(self)  # Single list for all instances - all the instances will be appended inside the list

    # also returns total stock value
    def calculate_total_price(self):
        return self.Price * self.Quantity

    # applying discount to all the instances
    def apply_discount(self):
        self.Price = self.Price * self.true_pay_factor
        return self.Price

    # reading data from csv and creating instances
    @classmethod
    def instantiate_from_db(cls):  # (cls) not (self) this needs to be defined as a class method because you can't access from an instance
        with open('db.csv', 'r') as f: # r is permission to read file
            reader = csv.DictReader(f)
            Items = list(reader)
        for x in Items:
            Item(
                Name=x.get('Name'),
                Price=float(x.get('Price')),
                Quantity=float(x.get('Quantity')),
            )

    # for printing Item.all properly
    def __repr__(self):
        return f"Item('{self.Name}', '{self.Price}', '{self.Quantity}')"


# comments for learning purpose
# instances of class item (Remove Line 85 triple quotation to access)
'''Item1 = Item("Phone", 100, 5)
# print(f"TOTAL STOCK PRICE", Item1.calculate_total_price())
Item2 = Item("Laptop", 1000, 3)
# "item2.has_numpad = False"  (For Special Characteristics of a product; which can be added later on)

# comment
# print(f"TOTAL STOCK PRICE", Item2.calculate_total_price())
# comment

Item3 = Item("Speaker", 50, 3)   # as quantity is by default 0 -- no need to assign value if not in stock

# comment
# print(f"TOTAL STOCK PRICE", Item3.calculate_total_price())
# comment

Item5 = Item("Mouse", 50, 5)
Item6 = Item("Keyboard", 75, 5)'''
# access all the attributes from line (39) class level and line(40) instance level
# comment
'''print(Item.__dict__)
print(Item3.__dict__)'''
# comment

# print prices after discount
# comment
'''Item1.apply_discount()
print(f"Discounted Price of {Item1.Name}s: ", Item1.Price)

# "assigning different discount for Item 2"

Item2.true_pay_factor = 0.7 #separate discount for Item 2
Item2.apply_discount()
print(f"Discounted Price of {Item2.Name}s: ", Item2.Price)
Item3.apply_discount()
print(f"Discounted Price of {Item3.Name}s: ", Item3.Price)'''
# comment
# comments for learning purpose
# print(Item.all)  # printing the all item  list

'''for instance in Item.all:
    print(instance.Name)'''

Item.instantiate_from_db()
print(Item.all)
