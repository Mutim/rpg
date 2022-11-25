import player_info
# import interests_points.Town
from utils.GameStates import save_game
from utils.TextUtils import menu_write, game_screen, cont
from utils.Menus import Menu, MenuSelector
from utils.ShopUtils import purchase, exchange
from utils.PlayerStats import get_inventory
import interests_points.Town as Town

import config

buy_goods = {
    "Small Potion": 10,
    "Herb": 4,
    "Vial of Water": 3,
    "Elixir": 14,
    "Charcoal": 6
}

sell_goods = {
    "Herb": 2,
    "Vial of Water": 1,
    "Elixir": 5,
    "Charcoal": 2
}


text = f"""
    [1] -  Buy
    [2] -  Sell
    [3] -  Inventory
    
    [4] -  Talk
    [5] -  Brew Potions

    [6] -  Leave"""


def apothecary_menu(command: Menu) -> None:
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


def buy():
    print(game_screen())
    purchase(buy_goods, 'What new potions do I have? Check them out!')


def sell():
    print(game_screen())
    exchange(sell_goods, "Have you got that eye of newt for me?")


def talk():
    talk_text = [f"How are you doing"]  # Fill this with better dialog. Like, mentioning some hint about brewing, etc
    menu_write(f"Talk", talk_text, config.text_delay)


def main() -> None:
    while True:
        MenuSelector.selector(text, "Apothecary", apothecary_menu)
