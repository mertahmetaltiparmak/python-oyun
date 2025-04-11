import random
import monster
import events
import hero
import room
from time import sleep

def universal_sleep(x):
    return sleep(x)


def pick_hero_input():
    user_name = get_user_name()
    print("-" * 20)
    print("1 - Savasci\n2 - Buyucu")
    print("-" * 20)
    hero_type = int(input("Seciminizi yapiniz: "))
    return pick_hero(hero_type, user_name)

def pick_hero(type, user_name):
    if type == 1:
        print("\nSavasci sinifini sectiniz.")
        return hero.Warrior(user_name)
    else:
        print("\nBuyucu sinifini sectiniz.")
        return hero.Mage(user_name)

def get_user_name():
    return input("İsminizi giriniz: ")

def main():
    hero = pick_hero_input()
    universal_sleep(0.8)
    baslangic_odasi = room.Room()
    baslangic_odasi.starting_room()
    print(f"\nSuanki Canin:{hero.health}\n")
    universal_sleep(1)

    for i in range(0,4):
        events.event_fight(hero)
        events.pick_random_event(hero)
    son_oda = room.Room()
    son_oda.last_room()    

main()