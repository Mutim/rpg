import player_info
from utils.TextUtils import cont, menu_write
import config


def shop_wares(wares: dict):
    l: list = [f'{"ID:":<5}{"Item:":<25}{"Price:"}\n{"├":─<36}┤\n\n']
    index: int = 1
    for k in wares.keys():
        l.append(f'{index:<5}{k:.<25}{wares[f"{k}"]}\n')
        index += 1
    return l


def purchase(wares: dict, message: str):
    menu_write(f"Buying Goods", [shop_wares(wares), "[X] -  Go Back"], config.text_delay)
    purchasing = True
    ware = input(f'\n{message} (1 - {len(wares)})\n >> ')
    item = ['item']
    if ware.lower() == 'x':
        print(f"Nothing interests you, eh?...")
        cont()
        return
    try:
        item: list = [k for k in wares.keys()][int(ware) - 1]
    except IndexError:
        purchasing = False
        print(f"I don't have an item on that shelf.")
        cont()

    while purchasing:
        count = input(f"\nThe {item} cost {wares[f'{item}']} gold each.\n\n"
                      f"How many {item}* would you like to buy?\n >> ")
        cost = int(count) * wares[f'{item}']
        try:
            if player_info.info['gold'] < cost:
                print(f"\nYou cannot afford {count} {item}*. You only have {player_info.info['gold']} gold!")
                cont()
                break
            else:
                print(f'\nYou have successfully bought {count} {item}*')
                player_info.info['gold'] -= cost
                if item not in player_info.info['inventory']:
                    player_info.info['inventory'][f'{item}'] = int(count)
                else:
                    player_info.info['inventory'][f'{item}'] += int(count)
                cont()
                break
        except Exception as e:
            input(f'An exception has occurred in {purchase.__name__}: {e}')
            break
    return


def exchange(wares: dict, message: str):
    inventory: dict = player_info.info['inventory']
    inventory_list: list = [k for k in inventory.keys()]
    wares_list: list = [k for k in wares.keys()]
    common: dict = {x: wares[x] for x in [y for y in inventory_list if y in wares_list]}
    if len(common) == 0:
        menu_write(f"You've got nothing that I want!", [
            'Well, this is awkward',
            'But you have nothing that interest me',
            'Go out and find something that I might like if you want to sell me something'], config.text_delay)
        cont()
        return
    menu_write(f"I'll take these off of you", [shop_wares(common), "[X] -  Go Back"], config.text_delay)
    ware: str = input(f'\n{message} (1 - {len(common)})\n >> ')

    selling = True
    item = ['item']
    if ware.lower() == 'x':
        print(f"Nothing interests you, eh?...")
        cont()
        return
    try:
        item: list = [k for k in player_info.info['inventory'].keys() if k in wares.keys()][int(ware) - 1]
    except IndexError:
        selling = False
        print(f"I don't need that item!")
        cont()
    while selling:
        count = input(f"\nI'll give you {wares[item]} gold for each {item}.\n\n"
                      f"How many {item}* would you like to sell? (You have {inventory[item]})\n >> ")
        cost = int(count) * wares[f'{item}']
        try:
            if inventory[f'{item}'] < int(count):
                print(f"\nYou can't sell me that many! You only have {inventory[item]} {item}*")
                cont()
                break
            else:
                print(f'\nYou have successfully sold {count} {item}*')
                player_info.info['gold'] += cost
                inventory[f'{item}'] -= int(count)
                if inventory[item] == 0:
                    inventory.pop(item)
                cont()
                break
        except Exception as e:
            input(f'An exception has occurred in {exchange.__name__}: {e}')
            break
    return
