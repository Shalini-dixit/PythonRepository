class Shop:
    def __init__(self, name, items):
        self.name = name
        self. items = items
    
    def get_items_count(self):
        return len(self.items)

shop = Shop("ABC",['Apples','Banana','Oranges'])
print(shop.get_items_count())

shop = Shop("xyz",['Tomato','onion','chillies','Strawberry'])
print(shop.get_items_count())
    