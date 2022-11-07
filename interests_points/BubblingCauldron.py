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
Bubbling Cauldron -
Shop Owner: Pepper
Shop Sells:
    tbd

Shop Buys:
    potions

"""

buy_goods = {
    "Small Potion": 2,
    "Medium Potion": 18,
    "Large Potion": 150,
    "Elixir": 5,
    "": ""
}

sell_goods = {
    "Slime Jelly": 1,
    "Troll Fur": 2,
    "Broken Spear": 2,
    "Rusted Sword": 4,
}

text = f"""
    [1] -  Buy
    [2] -  Sell
    [3] -  Inventory

    [4] -  Talk
    [5] -  Use Cauldron

    [6] -  Leave"""
name = player_info.info.get('name', "unloaded")
prof = player_info.info.get('prof', 'unloaded')
talk_text: list = [
    f"If you have a moment, walk up to my cauldron, and I could teach you",
    f"a thing or two about potion making. I've known many {prof}'s who are master",
    "potion makers."
    "     ",
    f"Just speak to me again to *Use my Cauldron."
]


def cauldron_menu(command: Menu) -> None:
    """Main Menu -
    :option 1 - Buy
        Opens the interests_points buy screen
    :option 2 - Sell
        Opens the interests_points sell screen
    :option 3 - Talk
        Opens the dialog with the shop owner
    :option 4 - Take Guild Quest
        Opens the guild quest menu
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
            menu_write("Bubbling Cauldron", talk_text, config.text_delay)

        case Menu(command='5'):
            input(f'Should open the potion crafting menu')
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
        MenuSelector.selector(text, "Bubbling Cauldron", cauldron_menu)
