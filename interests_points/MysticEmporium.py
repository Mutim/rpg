import player_info
from utils.GameStates import save_game
from utils.TextUtils import menu_write, game_screen, cont
from utils.Menus import Menu, MenuSelector
from utils.ShopUtils import purchase, exchange
from utils.PlayerStats import get_inventory
import interests_points.Town as Town

import config

buy_goods = {
    'Dry Wood': 25,
    'Blank Crystal': 85,
    'Basic Salt': 58,
    'Fire Powder': 20
}

sell_goods = {
    'Wood': 2,
    'crystal': 4,
    'Green Crystal': 10,
    'Blue Crystal': 13,
    'Red Crystal': 22
}

text = f"""
    [1] -  Buy
    [2] -  Sell
    [3] -  Inventory

    [4] -  Talk
    [5] -  Craft Magical Items

    [6] -  Leave"""

"""
Mystic Emporium -
Shop Owner: Salona
Emporium sells:
    Dry Wood
    Blank Crystal
    Basic Salt
    Fire Powder

Shop Buys:
    Wood
    (monster drops)

"""


def emporium_menu(command: Menu):
    match command:
        case Menu(command='1'):
            buy()

        case Menu(command='2'):
            sell()

        case Menu(command='3'):
            get_inventory()
            cont()

        case Menu(command='4'):
            talk()

        case Menu(command='5'):
            pass

        case Menu(command='6'):
            save_game()
            player_info.info["location"] = 'town'
            Town.main()

        case _:
            input(f'{config.unknown_command} {command!r}.')
            cont()
    pass


def buy():
    print(game_screen())
    purchase(buy_goods, 'You in the market for Magical Items?')


def sell():
    print(game_screen())
    exchange(sell_goods, "Crystals, crystals... I need crystals!")


def talk():
    talk_text = [f"How are you doing"]  # Fill this with better dialog.
    menu_write(f"Talk", talk_text, config.text_delay)


def main() -> None:
    while True:
        MenuSelector.selector(text, "Mystic Emporium", emporium_menu)
