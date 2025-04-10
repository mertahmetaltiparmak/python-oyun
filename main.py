import random
import monster
import events
import hero


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
    lvlOne = monster.Monster("Zombie", 100, 10, 1)
    # knight = pick_hero(1, get_user_name()) 
    hero = pick_hero_input()
    print(f"Suanki Canin:{hero.health}\n")
     # for i in range(0,6):
        # events.pick_random_event(hero)
    # events.pick_random_event(hero)
    events.event_fight(hero)
    events.event_fight(hero)
    # events.event_fountain(hero)

main()