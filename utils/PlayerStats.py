import config
import player_info


def get_inventory():
    inv = player_info.info['inventory']
    print(f'\n{"Item:":<30}{"Quantity:"}\n{config.line_break_fancy}\n\n')
    for k in inv.keys():
        print(f'{k:.<30}{inv[f"{k}"]}')


def get_equipment():
    pass


def get_effects():
    pass


def get_health():
    """Return health info with bars"""
    pass


def get_experience():
    """Return experience info with bars"""
    pass


