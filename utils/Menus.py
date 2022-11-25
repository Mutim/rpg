from dataclasses import dataclass
from utils.TextUtils import clear_screen, game_screen, menu_static, screen_texts
from utils.TextUtils import cont

import shlex


@dataclass
class Menu:
    """Menu command class"""

    command: str
    arguments: list[str]


class MenuSelector:
    """Menu selection class"""

    @staticmethod
    def selector(text: str, shop: str, shop_menu):
        clear_screen()
        print(game_screen())
        print(screen_texts())
        menu_static(shop, text)
        try:
            command, *arguments = shlex.split(input('\nPlease make a selection\n >> '))
            shop_menu(Menu(command, arguments))
        except ValueError:
            print('Invalid Selection')
            cont()

