from utils.GameStates import save_game
from utils.TextUtils import menu_write, game_screen, cont
from utils.Menus import Menu, MenuSelector
from utils.ShopUtils import shop_wares, purchase
from utils.PlayerStats import get_inventory
from menus import main_menu
import utils.ChangeLocation as c_l

import config


"""
Town Interest Points -
Apothecary (apothecary)
Guilded Goose Tavern (tavern)
Mystic Emporium # (mystic_emporium)
Guild Hall (guild_hall)
Training Grounds (training_grounds)
Blacksmith (blacksmith)
Bubbling Cauldron (bubbling_cauldron)
Fletcher (fletcher)
"""

text = f"""
    [1] -  Apothecary              [5] -  Fletcher
    [2] -  Guilded Goose Tavern    [6] -  Blacksmith
    [3] -  Mystic Emporium         [7] -  Bubbling Cauldron
    [4] -  Silver Crest Hall       [8] -  Battlefield

    [9] -  Main Menu"""


def town_menu(command: Menu) -> None:
    match command:
        case Menu(command='1'):
            c_l.change_location('apothecary')

        case Menu(command='2'):
            c_l.change_location('tavern')

        case Menu(command='3'):
            c_l.change_location('mystic_emporium')

        case Menu(command='4'):
            c_l.change_location('guild_hall')

        case Menu(command='5'):
            c_l.change_location('fletcher')

        case Menu(command='6'):
            c_l.change_location('blacksmith')

        case Menu(command='7'):
            c_l.change_location('bubbling_cauldron')

        case Menu(command='8'):
            c_l.change_location('battlefield')

        case Menu(command='9'):
            main_menu.main()

        case _:
            input(f'{config.unknown_command} {command!r}.')
            cont()


def main() -> None:
    while True:
        MenuSelector.selector(text, f"{config.world_name}'s Town Square", town_menu)
