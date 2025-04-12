from time import sleep

def universal_sleep(x):
    return sleep(x)

class Monster():
    def __init__(self, name, health, attack, level):
        self.name = name
        self.health = health
        self.attack = attack
        self.level = level

    def basic_attack(self, hero):
        print("Rakip saldiriyor...\n")
        universal_sleep(0.9)
        hero.health -= (self.attack - (hero.armor - 17))
        print_hero_health(hero, self)

    def specialAttack(self, hero):
        print("Rakip guclu bir saldiri yapacakmis gibi gozukuyor.")
        hero.health -= self.attack + 40
        hero.health += hero.armor
        print_hero_health(hero, self)

    def print_stats(self):
        print(f"Karsilastigin canavar: {self.name}\t\tLevel: {self.level}\tCani:{self.health}")


def print_hero_health(hero, monster):
    if hero.health <= 0:
        pass
    else:
        print(f"Hasar aldın!\nCanın: {hero.health}")
        universal_sleep(0.8)
        print(f"Manan: {hero.mana}\n")
        universal_sleep(0.7)
        print(f"{monster.name}'in Canı: {monster.health}\n")
        universal_sleep(0.7)

