from item import Item


# Inheritance
class Phone(Item):
    all = []

    def __init__(self, Name: str, Price: float, Quantity=0.0, Broken_Phones=0):
        # call super function to access everything from Parent Class (Item)
        super().__init__(
            Name, Price, Quantity
        )
        assert Broken_Phones >= 0, f"Broken Phones {Broken_Phones} count less that zero"

        self.Broken_Phones = Broken_Phones
