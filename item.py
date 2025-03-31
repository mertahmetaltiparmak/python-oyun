class Item():
    def __init__(self, name):
        self.name = name
        

class DrinkableItem(Item):
    def __init__(self, name, hp):
        super().__init__(name)
        self.hp = hp