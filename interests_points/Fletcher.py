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
Silver Crest Hall -
Shop Owner: Llana
Shop Sells:
    tbd

Shop Buys:
    monster drops

"""

buy_goods = {
    "Raw Metal": 60,
    "Wood": 35
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
    [5] -  Take Guild Quest

    [6] -  Leave"""
name = player_info.info.get('name', "unloaded")
talk_text: list = [
    f'Ahh, you must be {name}. Grundle said I might see you around.',
    f"If you're interested in joining the Guild* we have some quests to offer you.",
    "     ",
    f"Just speak to me again taking up a guild quest. There's gold to be made in",
    f"protecting {config.world_name.title()}!"
]


def guild_menu(command: Menu) -> None:
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
            menu_write("Silver Crest Hall", talk_text, config.text_delay)

        case Menu(command='5'):
            input(f'Should open the guild quest manager')
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
        MenuSelector.selector(text, "Silver Crest Hall", guild_menu)
