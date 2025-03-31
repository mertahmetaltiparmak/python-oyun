
class Monster():
    def __init__(self, name, health, attack, level):
        self.name = name
        self.health = health
        self.attack = attack
        self.level = level

    def basic_attack(self, hero):
        print("Rakip saldiriyor...")
        hero.health -= self.attack
        print_hero_health(hero.health)

    def specialAttack(self, hero):
        print("Rakip guclu bir saldiri yapacakmis gibi gozukuyor.")
        hero.health -= self.attack + 30
        print_hero_health(hero.health)

    def print_stats(self):
        print(f"Karsilastigin canavar: {self.name}\tLevel: {self.level}")


def print_hero_health(health):
    if health <= 0:
        print("Öldün!")
    else:
        print(f"Hasar aldin! Canin: {health}")