import player_info
from utils.TextUtils import cont


def shop_wares(wares: dict):
    l: list = [f'{"ID:":<5}{"Item:":<20}{"Price:"}\n{"":_<25}\n\n']
    index: int = 1
    for k in wares.keys():
        l.append(f'{index:<5}{k:<20}{wares[f"{k}"]}\n')
        index += 1
    return l


def purchase(wares: dict, message: str):
    purchasing = True
    ware = input(f'\n{message} (1 - {len(wares)})\n >> ')
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
