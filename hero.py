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
        pass


class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, 100,  30, 20, 5)

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
        print_monster_health(monster, self)
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
        print("Acinin kendini güclendirdigini hissediyorsun!\n")
        universal_sleep(0.7)
        self.health -= 25
        self.attack += 5
        print(f"Yeni saldırı gücün: {self.attack}")
        universal_sleep(0.7)

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
        print_monster_health(monster, self)


        
class Mage(Hero):
    def __init__(self, name):
        super().__init__(name, 85, 10, 0, 50)

    def fight(self, monster, hero):
        while monster.health > 0 and self.health > 0:
            universal_sleep(0.7)
            print("\nSaldiri Yeteneklerin:")
            print("1 - Ates topu firlat (10 Mana)")
            print("2 - Hançerini salla")
            print("3 - Yenilenme (15 Mana)")
            print("4 - Ejder Nefesi (30 Mana)")
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
                if self.mana < 10:
                    print("Yetersiz Mana!")
                    continue
                self.fireball(monster)
            if user_input == 2:
                self.dagger_swing(monster)
            if user_input == 3:
                if self.mana < 15:  # bunu daha kısaltabilirim function içine alarak **
                    print("Yetersiz Mana !")
                    continue
                self.regenerition()
            if user_input == 4:
                if self.mana < 30:
                    print("Yetersiz Mana!")
                    continue
                self.dragon_breath(monster)


    def fireball(self, monster):       
        print("Ates topu attin! ")
        universal_sleep(1)
        monster.health -= self.mana * 0.8
        self.mana -= 10
        universal_sleep(0.7)
        print("Kalan Mana: ", self.mana)
        universal_sleep(0.8)
        print_monster_health(monster, self)
        universal_sleep(0.9)
    
    def dagger_swing(self, monster):
        universal_sleep(0.8)
        print("Gizlediğin hançeri çıkarıp sallıyorsun...")
        universal_sleep(1)
        monster.health -= self.attack
        print_monster_health(monster, self)
        universal_sleep(1)

    def regenerition(self):
        print("Kadim bir buyu ile kendini yeniliyorsun...")
        universal_sleep(1)
        self.mana -= 15
        self.health += 20
        print("Canin artti...")
        universal_sleep(0.6)
        print(f"Canin: {self.health}")
        universal_sleep(1)

    def dragon_breath(self, monster):
        print("Ateşten bir ejder oluşturuyorsun...")
        universal_sleep(0.8)
        print("Ejder canavara ateş püskürttüyor !")
        universal_sleep(1)
        monster.health -= (self.mana * 2) - 25
        self.mana -= 30
        print_monster_health(monster, self)
        universal_sleep(1)

def print_monster_health(monster, hero):
    if monster.health <= 0:
        print("Canavar Öldü!")
    else:
        print(f"Canavarın Cani: {monster.health}\n")
        universal_sleep(0.8)
        print(f"{hero.name}'in Cani: {hero.health}")
        universal_sleep(0.7)
        print(f"{hero.name}'in Manasi: {hero.mana}\n")
        universal_sleep(0.7)
