from item import Item
# from phone import Phone (This would be as good as the previous line: Inheritance)
# Phone is the child class of Item and inherited all the attributes
# instantiate by Item1 = Phone("MyPhone", 1000, 8)

# comment
# testing Class Method and Static Method
'''
print(Item.is_integer(5.5))  # returns False
print(Item.is_integer(7.0))  # returns True
Item.instantiate_from_db()
print(Item.all)
'''
# comment
'''phone1 = Phone("Apple Iphone X", 500, 5)
phone2 = Phone("Apple Iphone 13", 700, 5)
print(Item.all)
print(Phone.all)'''
# comment

Item.instantiate_from_db()
print(Item.all)

Item1 = Item("XYZ", 700, 3)
print(Item1.Name)
# edit the attribute
# 1. will throw error (length > 10)
'''Item1.Name = "abcdefxyzomnpqstuv"
print(Item1.Name)'''
# 2. won't throw error
Item1.Name = "abcdef"
print(Item1.Name)
print(Item1.Price)
Item1.apply_increment(0.5)
print(Item1.Price)
