import random

import player_info
import config
from utils.TextUtils import menu_write, cont, event_text

import battlefield.EventsData
import battlefield.MonsterData

monster_list = battlefield.MonsterData.enemies_list
monster_data = battlefield.MonsterData.data

event_data = battlefield.EventsData.data


def walk():
    pass


def rest():
    pass


def roll_event():
    hit = random.randint(0, 100)
    if hit <= 100:  # 10% chance to find treasure
        event_treasure()
    else:
        event_fight()


def event_treasure():
    index = random.randint(0, len(event_data)-1)
    event = event_data[index]
    print(event_text(event))
    cont()


def event_fight():
    monster = monster_data[random.choice(monster_list)]
    player = player_info.info
    monster = monster['name']
    text = [
        f"You encountered a {monster} while on the battlefield",
        f"What would you like to do?"
    ]

    menu_write('Monster Encountered!', text, config.text_delay)
    select = input('''
        [1] -  Fight
        [2] -  Use Item
        [3] -  Run
        ''')
    cont()


def use_item(item: str) -> bool:
    inventory = player_info.info['inventory']
    if item in inventory and inventory[item] > 0:
        inventory[item] -= 1
        if inventory[item] == 0:
            inventory.pop(item)
        return True
    else:
        return False


def run():
    # Base chance to run away
    chance: float = 20.0
    luck: float = player_info.info['luck']
    calculated = (luck * 100) + chance

    if random.randint(0, 100) <= calculated:
        print('Ran Away')


