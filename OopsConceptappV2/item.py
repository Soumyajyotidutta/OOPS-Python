import csv

# inside a class methods can be private too. Ex. def __MethodName(self):

class Item:
    true_pay_factor = 0.8   # 20% discount to items
    all = []

    def __init__(self, Name: str, Price: float, Quantity=0.0):

        assert Price >= 0, f"Price {Price} is less than zero!"
        assert Quantity >= 0, f"Quantity {Quantity} is less than zero!"

        self.__Name = Name  # making the attribute private
        self.__Price = Price
        self.Quantity = Quantity

        Item.all.append(self)  # Single list for all instances - all the instances will be appended inside the list

    # restricting the value of price so that it can't be set as negative
    # encapsulation
    @property
    def Price(self):
        return self.__Price

    # applying discount to all the instances
    def apply_discount(self):
        self.__Price = self.__Price * self.true_pay_factor
        return self.__Price

    def apply_increment(self, increment_factor):
        self.__Price = self.__Price + self.__Price * increment_factor
        return self.__Price
    # GETTER
    @property
    def Name(self):
        return self.__Name  # making the attribute private

    # Although the previous value is private we can assign a different value with help of the following
    # SETTER
    @Name.setter
    def Name(self, value):
        if len(value) > 10:
            raise Exception("Name is too long!")   # handle exceptions
        else:
            self.__Name = value

    # also returns total stock value
    def calculate_total_price(self):
        return self.__Price * self.Quantity


    # reading data from csv and creating instances
    @classmethod
    def instantiate_from_db(cls):  # (cls) not (self) this needs to be defined as a class method because you can't access from an instance
        with open('db.csv', 'r') as f:
            reader = csv.DictReader(f)
            ''' "r" is permission to read file 
                    (Can be done from
                    JSON or XML file also) '''
            Items = list(reader)
        for x in Items:
            Item(
                Name=x.get('Name'),
                Price=float(x.get('Price')),
                Quantity=float(x.get('Quantity')),
            )

    # for printing Item.all properly
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.Name}', '{self.__Price}', '{self.Quantity}')"

    # initiating a static method (Kinda standalone function; nothing to do with the class instances) inside a class
    # check if the number is .0 float or a simple integer
    # .5/.8 floats will return False
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return

