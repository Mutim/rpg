import player_info
from utils.GameStates import save_game
from utils.TextUtils import menu_write, game_screen, cont
from utils.Menus import Menu, MenuSelector
from utils.ShopUtils import purchase, shop_wares
from utils.PlayerStats import get_inventory
from menus import main_menu
import interests_points.Town as Town
import config


"""
Guilded Goose Tavern -
Shop Owner: Borna
Shop Sells:
    Beer
    Moldy Bread
    Mushroom Stew
    Crackers
    Wine
    Water

Shop Buys:
    Grain
    Raw Meat
    Flour
    Water
    Wood

"""

buy_goods = {
    "Beer": 10,
    "Mouldy Bread": 4,
    "Mushroom Stew": 3,
    "Crackers": 4,
    "Wine": 8,
    "Water": 7
}

sell_goods = {
    "Grain": 2,
    "Raw Meat": 3,
    "Flour": 3,
    "Water": 2,
    "Wood": 1
}

text = f"""
    [1] -  Buy
    [2] -  Sell
    [3] -  Inventory

    [4] -  Talk
    [5] -  Make Drink

    [6] -  Leave"""


def tavern_menu(command: Menu) -> None:
    """Main Menu -
    :option 1 - Buy
        Opens the interests_points buy screen
    :option 2 - Sell
        Opens the interests_points sell screen
    :option 3 - Talk
        Opens the dialog with the shop owner
    :option 4 - Brew Potions
        Opens the brewing menu
    :option 5 - Leave
        Leaves the shop, opens the city menu
    """

    match command:
        case Menu(command='1'):
            buy()

        case Menu(command='2'):
            sell()

        case Menu(command='3'):
            get_inventory()
            cont()

        case Menu(command='4'):
            pass

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
    menu_write(f"Buying Goods", [shop_wares(buy_goods), "[X] -  Go Back"], config.text_delay)
    purchase(buy_goods, 'Select an item from the shelf!')


def sell():
    print(game_screen())
    menu_write(f"Selling Wares", [shop_wares(sell_goods)], config.text_delay)
    ware = input()
    if ware == '1':
        print('Selected 1')
        input()


def main() -> None:
    while True:
        MenuSelector.selector(text, "Guilded Goose Tavern", tavern_menu)
