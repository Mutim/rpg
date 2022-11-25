import random

import player_info
import config

from utils.GameStates import save_game
from utils.TextUtils import menu_write, game_screen, cont, clear_screen

from utils.Menus import Menu, MenuSelector
from utils.PlayerStats import get_inventory
from battlefield.BattleUtils import roll_event, rest

import interests_points.Town as Town

text = f"""
    [1] -  Walk
    [2] -  Rest
    [3] -  Inventory
    
    [4] -  Go Home"""


def battlefield_menu(command: Menu) -> None:
    match command:
        case Menu(command='1'):  # Walk
            walking = True

            while walking:
                clear_screen()
                roll_event()
                print(game_screen())
                moving = input('Keep Moving? ')
                if moving.lower() == 'n':
                    break
            # Remove a ration and lower sanity by random amount

        case Menu(command='2'):  # Rest
            game_screen()
            rest()
            # "You build a small campfire. I hope this doesn't attract anything."
            # Chance to spawn mob, or heal small amount of HP

        case Menu(command='3'):  # Get Inventory
            get_inventory()
            cont()

        case Menu(command='4'):
            save_game()
            player_info.info["location"] = 'town'
            Town.main()

        case _:
            input(f'{config.unknown_command} {command!r}.')
            cont()


def talk():
    talk_text = [f"How are you doing"]
    menu_write(f"Talk", talk_text, config.text_delay)


# Main game-loop for the battlefield
def main() -> None:
    while True:
        MenuSelector.selector(text, "Front-line Camp", battlefield_menu)
