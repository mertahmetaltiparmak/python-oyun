import monster
import random
import hero
import time
import room
import item
from time import sleep

def universal_sleep(x):
    return sleep(x)

def random_int(start, end):
    random.seed(time.time())
    return random.randint(start, end)


def pick_random_event(hero):
    randomizer = random_int(1, 6)
    if randomizer == 1:
        event_fountain(hero)
    elif randomizer == 2:
        event_fight(hero)

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
        universal_sleep(1)
        print("Canin: ", hero.health)
        universal_sleep(1)
        print("Dikkatli adımlarla diğer odaya ilerliyorsun")
    elif userInput == 2:
        print("Yoluna devam etmeye karar verdin")


def monster_generator():
    randomizer = random_int(1, 3)
    if randomizer == 1:
        return monster.Monster("Seytan", 100, 25, 4)
    elif randomizer == 2:
        return monster.Monster("Hiclik Canavari", 200, 40, 10)
    elif randomizer == 3: 
        return monster.Monster("Zeng", 90, 50, 1)

def event_fight(hero):
    print("Canavar gördün...")
    universal_sleep(2)
    monster = monster_generator()
    monster.print_stats()
    universal_sleep(2)
    print("1 - Savaş \t 2 - Kaç")
    fight_choice = int(input("Seçimini yap:"))
    if fight_choice == 1:
        while True:
            hero.fight(monster)
            if monster.health <= 0:
                break
            monster.basic_attack(hero)
            universal_sleep(2)
            if hero.health <= 0:
                break        
    elif fight_choice == 2:
        print("Canavara gözükmeden uzaklaşmaya çalişiyorsun...")
        universal_sleep(2)
        runaway_chance = random_int(1, 6)
        if runaway_chance < 4:
            print("Canavar seni farketmeden odadan uzaklaştin.")
        elif runaway_chance > 4:
            print("Canavar ayak sesini duydu ve sana karşı saldiriya geçti")
            universal_sleep(2)
            while True:
                monster.basic_attack(hero)
                universal_sleep(2)
                if hero.health <= 0:
                    break        
                hero.fight(monster)
                if monster.health <= 0:
                    universal_sleep(2)
                    print("Canavar yavaşcana toza dönüştü...\tYoluna devam ediyorsun.")
                    break

        