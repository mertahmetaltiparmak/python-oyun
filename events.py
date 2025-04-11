import monster
import random
import hero
import time
import room
import item
from time import sleep

def death_screen(hero):
    if hero.health <= 0:
        universal_sleep(0.9)
        print("Öldünüz !")
        exit(True)

# event kaçış

def hero_regeneration(hero):
    hero.health += 50
    hero.mana += 25

def universal_sleep(x):
    return sleep(x)

def random_int(start, end):
    random.seed(time.time())
    return random.randint(start, end)


def pick_random_event(hero):
    randomizer = random_int(1, 3)
    if randomizer == 1:
        event_statue(hero)        
    elif randomizer == 2:
        event_fight(hero)
    elif randomizer == 3:
        event_fountain(hero)

def event_fountain(hero):
    oda = room.Room()
    oda.describe_fountain_room()
    print("Mavi işiklarla parlayan bir çeşmeyle karşilaştin\n1-Suyu iç \t2-Yolunu Devam et\t")
    userInput = int(input("Seciminiz: "))
    if userInput == 1:
        randomizer_fountain = random_int(1,2)
        if randomizer_fountain == 1:
            hero.health += item.DrinkableItem.drinkable_items["Su"]
        elif randomizer_fountain == 2:
            hero.health += item.DrinkableItem.drinkable_items["Zehirli Su"]
        print("Suyun içini yaktığını hissediryorsun...")
        if hero.health <= 0:
            death_screen(hero)
        else:
            universal_sleep(1)
            print("Canin: ", hero.health)
            universal_sleep(1)
            print("Dikkatli adımlarla diğer odaya ilerliyorsun")
            universal_sleep(1.5)
    elif userInput == 2:
        print("Yoluna devam etmeye karar verdin")


def monster_generator():
    names = ["Seytan", "Hiclik Canavari", "Zeng,"]
    selected_name = random.choice(names)
    level = random.randint(1, 10)
    health = random.randint(20, 100) + (level * 5) 
    attack = random.randint(5, 25) + (level * 2)
    return monster.Monster(selected_name, health, attack, level)


def event_fight(hero):
    print("Canavar gördün...")
    universal_sleep(2)
    monster = monster_generator()
    monster.print_stats()
    universal_sleep(2)

    while True:
        print("1 - Savaş \t 2 - Kaç")
        try:
            fight_choice = int(input("Seçimini yap: "))
            if fight_choice in [1, 2]:
                break  
            else:
                print("Geçersiz seçim, lütfen 1 veya 2 giriniz.")
                universal_sleep(0.6)
        except ValueError:
            print("Geçersiz giriş! Lütfen geçerli bir sayı girin.")
            universal_sleep(0.6)

    if fight_choice == 1:
        while True:
            hero.fight(monster, hero)
            if monster.health <= 0:
                print("Canavar yavaşcana toza dönüştü...")
                universal_sleep(0.7)
                print("Canavardan çikan toz etrafinda donup derinin icine girdi...")
                universal_sleep(0.8)
                hero_regeneration(hero)
                print(f"Canin: {hero.health}\t Manan: {hero.mana}")
                universal_sleep(1)
                break
            monster.basic_attack(hero)
            universal_sleep(1.5)
            death_screen(hero)

    elif fight_choice == 2:
        print("Canavara gözükmeden uzaklaşmaya çalişiyorsun...")
        universal_sleep(2)
        runaway_chance = random_int(1, 7)
        if runaway_chance < 4:
            print("Canavar seni farketmeden odadan uzaklaştin.")
        elif runaway_chance >= 4:
            print("Canavar ayak sesini duydu ve sana karşı saldiriya geçti")
            universal_sleep(1.5)
            while True:
                monster.basic_attack(hero)
                universal_sleep(1.5)
                death_screen(hero)      # ölüp ölmediğini kontrol etmek için
                hero.fight(monster, hero)
                if monster.health <= 0:
                    universal_sleep(0.8)
                    print("Canavar yavaşcana toza dönüştü...")
                    universal_sleep(1)
                    print("Canavardan çikan toz etrafinda donup derinin icine girdi...")
                    universal_sleep(1.3)
                    hero_regeneration(hero)
                    print(f"Canin: {hero.health}\t Manan: {hero.mana}")
                    universal_sleep(1.6)
                    break

def event_statue(hero):
    oda = room.Room()
    oda.describe_statue_room()
    # 1 iksir 2 bıçak 3 kılıç
    while True:
        try:
            statue_choice = int(input("Seçiminizi Yapin:"))
            if statue_choice in [1,2,3]:
                break
            else:
                print("Geçersiz seçim lütfen 1, 2 veya 3 giriniz !")
        except ValueError:
            print("Geçersiz giriş! Lütfen geçerli bir sayı girin.")
            universal_sleep(0.6)

    if statue_choice == 1: # iksir
        print("Yavaşca iksire doğru uzanıyorsun ve kapağını açıyorsun iksirin içindeki sıvının garip görünüşüne aldırmadan içmeye karar veriyorsun...")
        universal_sleep(1.5)
        drink_chace = random_int(1, 3)

        if drink_chace == 1:
            universal_sleep(0.5)
            print("Kemiklerinin ısındığını ve görünüşünün netleştiğini hissediyorsun")
            universal_sleep(1.5)
            hero_regeneration(hero)
            print("Canin artti...")
            universal_sleep(1)
            print(f"Canin: {hero.health}\t Manan: {hero.mana}")

        elif drink_chace == 2:
            print("Karadelikimsi siyah sıvının boğazını yaktığını hissediyorsun...")
            universal_sleep(1.5)
            hero.health -= item.DrinkableItem.drinkable_items["Siyah iksir"]
            death_screen(hero)
            print("Canin azaldi...")
            universal_sleep(0.8)
            print(f"Canin: {hero.health}\t Manan: {hero.mana}")
            universal_sleep(0.9)

        elif drink_chace == 3:
            print("Karadeliğimsi sıvıyı yavşacana yuttun...")
            print("Kendini garip hissediyorsun onun dışında hiçbir şey olmuyor. ")

    if statue_choice == 2: # biçak
        print("Bu garip ritueli tamamlamaya karar veriyorsun...")
        universal_sleep(1.6)
        print("Elin titreyerek bıçağa uzanıyor, soğuk metal parmaklarını uyuşturuyor.")
        universal_sleep(1.8)
        print("Avucunu kesiyorsun, sıcak kan yavaşça taş zemine damlıyor.")
        universal_sleep(1.8)
        hero.health -= 30
        death_screen(hero)
        print("Kan, heykelin önündeki sembole ulaştığında, taş hafifçe parlamaya başlıyor.")
        universal_sleep(1.8)
        print("Zemin titriyor, meşaleler bir anlığına sönüp neredeyse görünmez bir alevle yanmaya devam ediyor.")
        universal_sleep(1.8)
        print("Heykelin gözleri mavi bir ışıkla parlıyor, sanki seni tanımış gibi.")
        universal_sleep(1.8)
        print("Kulağında yankılanan bir fısıltı duyuyorsun: 'Adak verildi... kapı açılıyor ve odadan çıkıyorsun.'")
        universal_sleep(1.8)
        print(f"Canin: {hero.health}")
        universal_sleep(1.6)


    if statue_choice == 3: # kılıç
        print("Elin tereddütsüz bir şekilde kılıca uzanıyor.")
        universal_sleep(1.8)
        print("Parmakların kılıç kabzasına değdiği an, vücudundan bir enerji dalgası geçiyor.")
        universal_sleep(1.8)
        print("Kılıç hafifçe titreşiyor, sanki seninle bir bağ kurmuş gibi.")
        universal_sleep(1.8)
        print("Kasların geriliyor, zihnin berraklaşıyor... kendini her zamankinden güçlü hissediyorsun.")
        universal_sleep(1.8)
        print("Ancak o anda, taş zemin aniden çatlamaya başlıyor.")
        universal_sleep(1.8)
        print("Çatlaklardan yükselen dumanın içinden devasa bir yaratık ortaya çıkıyor.")
        universal_sleep(1.8)
        print("Yüzü maskelenmiş, derisi taş gibi sert ve gözleri sönük maviyle parlayan bu varlık sana kükreyerek saldırıyor.")
        universal_sleep(1.8)
        print("Kadim muhafız: *Graveth* uyanmış.")
        universal_sleep(1.8)
        hero.attack += 20
        hero.health += 40
        hero.mana += 25

        guardin = monster.Monster("Graveth", 300, 25, 10)
        guardin.print_stats()

        print("Savaş Başladı !")
        
        while True:
            hero.fight(guardin, hero)
            if guardin.health <= 0:
                print("Canavar yavaşcana toza dönüştü...")
                universal_sleep(0.7)
                print("Canavardan çikan toz etrafinda donup derinin icine girdi...")
                universal_sleep(0.8)
                hero_regeneration(hero)
                print(f"Canin: {hero.health}\t Manan: {hero.mana}")
                universal_sleep(1)
                break
            i = 0
            i += 2.5
            if i % 2 == 0:
                guardin.specialAttack(hero)
            if i % 2 != 0:
                guardin.basic_attack(hero)
                universal_sleep(1.5)
            death_screen(hero)