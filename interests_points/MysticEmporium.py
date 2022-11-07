from utils.Menus import MenuSelector

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

text = """

"""


def emporium_menu():
    pass


def main() -> None:
    while True:
        MenuSelector.selector(text, "Mystic Emporium", emporium_menu)
