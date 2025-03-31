from time import sleep
class Hero():
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def fight():
        print()


class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, 100,  50)
        self.armor = 20
    def fight(self, monster):
        print("1 - Kilicini savur")
        user_input = int(input("Secimini yap: "))
        if user_input == 1:
            self.sword_swing(monster)
    def sword_swing(self, monster):
        print("Kilicini savurdun!")
        monster.health -= self.attack
        sleep(1)
        print_monster_health(monster.health)
        sleep(1)
        
class Mage(Hero):
    def __init__(self, name):
        super().__init__(name, 85, 10)
        self.mana = 50
    def fight(self, monster):
        print("1 - Ates topu firlat")
        user_input = int(input("Secimini yap: "))
        if user_input == 1:
            self.fireball(monster)        
    def fireball(self, monster):       
        print("Ates topu attin! ")
        monster.health -= self.mana * 0.8
        self.mana -= 10
        print_monster_health(monster.health)

def print_monster_health(health):
    if health <= 0:
        print("Canavar Öldü!")
    else:
        print("Canavarin Cani: ", health)
