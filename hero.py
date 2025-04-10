from time import sleep

def universal_sleep(x):
    return sleep(x)

class Hero():
    def __init__(self, name, health, attack, armor, mana):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        self.mana = mana
    def fight():
        print()


class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, 100,  30, 5, 0)

    def fight(self, monster, hero):
        universal_sleep(0.7)
        print("\nSaldiri Yeteneklerin:")
        print("1 - Kilicini savur")
        print("2 - Zirhini geliştir")
        print("3 - Aci Yok")
        print("4 - Öfke Patlamasi (20 Mana)")

        while True:
            try:
                user_input = int(input("Secimini yap: "))
                if user_input in [1, 2, 3, 4]:
                    break 
                else:
                    print("Geçersiz seçim! Lütfen 1, 2, 3 veya 4 giriniz.")
            except ValueError:
                print("Geçersiz giriş! Lütfen geçerli bir sayi girin.")

        if user_input == 1:
            self.sword_swing(monster)
        if user_input == 2:
            self.armor_upgrade()
        if user_input == 3:
            self.attack_upgrade()
        if user_input == 4:
            self.rage_burst(monster)

    def sword_swing(self, monster):
        print("Kilicini savurdun!")
        monster.health -= self.attack
        universal_sleep(1)
        print_monster_health(monster.health)
        universal_sleep(1)

    def armor_upgrade(self):
        print("Zirhinin bedenindeki boşluklari kapattigini hissediyorsun...")
        universal_sleep(0.8)
        self.armor += 5
        print(f"Yeni zırh değerin: {self.armor}")
        universal_sleep(0.8)

    def attack_upgrade(self):
        print("Kilicini kendini bedenine sapladin...")
        universal_sleep(0.8)
        print("Acinin kendini güclendirdigini hissediyorsun!")
        self.health -= 25
        self.attack += 5
        print(f"Yeni saldırı gücün: {self.attack}")

    def rage_burst(self, monster):
        if self.mana < 20:
            print("Yeterli manan yok! (20 mana gerekli)")
            return 
        print("Öfke Patlaması! Tüm gücünü kılıcına yükledin!")
        universal_sleep(1)
        damage = self.attack * 2
        monster.health -= damage
        self.mana -= 20
        print(f"{damage} hasar verdin! Kalan Mana: {self.mana}")
        universal_sleep(0.8)
        print_monster_health(monster.health)


        
class Mage(Hero):
    def __init__(self, name):
        super().__init__(name, 85, 10, 0, 50)
    def fight(self, monster):
        universal_sleep(0.7)
        print("\nSaldiri Yeteneklerin:")
        print("1 - Ates topu firlat")
        user_input = int(input("Secimini yap: "))
        if user_input == 1:
            self.fireball(monster)

    def fireball(self, monster):       
        print("Ates topu attin! ")
        universal_sleep(1)
        monster.health -= self.mana * 0.8
        self.mana -= 10
        universal_sleep(0.5)
        print("Kalan Mana: ", self.mana)
        universal_sleep(0.8)
        print_monster_health(monster.health)

def print_monster_health(health):
    if health <= 0:
        print("Canavar Öldü!")
    else:
        print("Canavarin Cani: ", health)
