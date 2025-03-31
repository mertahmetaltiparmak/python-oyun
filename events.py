import monster
import random
import hero
import time
from time import sleep

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
    print("Mavi işiklarla parlayan bir çeşmeyle karşilaştin\n1-Suyu iç \t2-Yolunu Devam et\t")
    userInput = int(input("Seciminiz: "))
    if userInput == 1:
        hero.health += 10
        print("Suyun içini yaktığını hissediryorsun... Canın doldu.\nCanin:", hero.health)
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
    sleep(2)
    monster = monster_generator()
    monster.print_stats()
    sleep(2)
    while True:
        monster.basic_attack(hero)
        sleep(1)
        if hero.health <= 0:
            break        
        hero.fight(monster)
        if monster.health <= 0:
            break