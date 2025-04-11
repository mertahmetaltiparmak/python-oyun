class Item():
    def __init__(self, name):
        self.name = name
        

class DrinkableItem(Item):
    def __init__(self, name, hp):
        super().__init__(name)
        self.hp = hp
    drinkable_items = {"Su": 25, "Zehirli Su": -20, "Can İksiri" : 50, "Mana İksiri" : 50, "Siyah iksir" : -30}