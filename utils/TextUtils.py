import sys
import subprocess
import time
import textwrap

import config
import player_info
from utils.Colors import Colors

c = Colors


def clear_screen():
    subs = {
        'posix': 'clear',
        'linux': 'clear',
        'win32': 'cls'
    }
    if sys.platform in subs:
        subprocess.call(subs[sys.platform], shell=True)
    else:
        print(f'The OS: {sys.platform}, is not defined.')


def think(*args) -> str:
    return f'*[{" ".join([a for a in args])}]*\n'


def write(text: list, delay: float):
    for row in text:
        for c in row:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(delay)
        print()


def cont():
    print(f'\n\n{config.line_break_fancy}')
    input(f'\n[ Press ENTER to Continue ]')
    clear_screen()


def menu_static(title: str, text: str):
    print(f"""
{config.line_break_bold}
\t{title}
{config.line_break_bold}
{text}

{config.line_break_fancy}
""")


def menu_write(title: str, text: list, delay: float):
    print(f"""
{config.line_break_bold}
\t{title}
{config.line_break_bold}
""")
    write(text, delay)
    print(f"\n{config.line_break_fancy}")


def bars(val: int, val_max: int) -> str:
    fi: str = f'▓' * int(round((val / val_max) * 50))

    return f'{fi:░<50}'


vowels = ["a", "e", "i", "o", "u"]

runes = {
    'a': 'ᚢ', 'b': 'ᛋ', 'c': 'ᚣ', 'd': 'ᚤ', 'e': 'ᚦ', 'f': 'ᛄ', 'g': 'ᛇ',
    'h': 'ᚸ', 'i': 'ᚻ', 'j': 'ᛃ', 'k': 'ᛕ', 'l': 'ᚫ', 'm': 'ᛗ', 'n': 'ᛸ',
    'o': 'ᛜ', 'p': 'ᛈ', 'q': 'ᛩ', 'r': 'ᚹ', 's': 'ᛤ', 't': 'ᛞ', 'u': 'ᛟ',
    'v': 'ᛒ', 'w': 'ᛠ', 'x': 'ᛝ', 'y': 'ᚱ', 'z': 'ᚼ'}


def runic(*args: str) -> str:
    n = []
    for w in args:
        for l in w:
            n.append(runes.get(f'{l.lower()}', l))

    return f'{" ".join([a for a in n])}\n'


# What gets displayed at the point of interest the character is at
def screen_texts():
    location = player_info.info["location"]
    text = {
        '': '',  # In the event that the player data doesn't load, this prevents erroring before it's called
        'town': f"[ {config.world_name} ] - \n\n\tLooking around, there's not much going on in this town.",
        'apothecary': "[ Grundle ] - \n\n\t*kekeke* Welcome back! Might I interest you in a tincture?",
        'battlefield': "[ General Otis ] - \n\n\tGet in line soldier! We need a hand on the *Western Flank!",
        'blacksmith': "[ Cedric ] - \n\n\tIt's nice to see a new face around. Can you handle the heat?",
        'bubbling_cauldron': "[ Pepper ] - \n\n\tOh. hello there deary. Here to stir up some trouble? *kekeke*",
        'fletcher': "[ Striker ] - \n\n\tGrab that string from on the *Workbench, and come lend me a hand.",
        'guild_hall': "[ Llana ] - \n\n\tHere to join the cause? Or just cause a scene...",
        'mystic_emporium': "[ Solana ] - \n\n\tWell hello there my child. Have you seen our newest stock?",
        'tavern': "[ Borna ] - \n\n\t*Oi! Get yer feet off tha table!* -- Hey there, Wanna drink?"
    }
    return text[f'{location}']


def game_screen() -> str:
    clear_screen()
    # Defined variables every time function is called
    name = player_info.info["name"]
    race = player_info.info["race"]
    prof = player_info.info["prof"]
    health_max = player_info.info["health"]["max"]
    health_current = player_info.info["health"]["current"]
    mana_max = player_info.info["mana"]["max"]
    mana_current = player_info.info["mana"]["current"]
    xp_next = player_info.info['experience']['next']
    xp_current = player_info.info['experience']['current']
    rations = player_info.info["rations"]
    sanity = player_info.info["sanity"]
    gold = player_info.info["gold"]
    location = player_info.info["location"]
    events = player_info.info["world_info"]["event"]

    clear_screen()
    game_menu = f"""
■╠═══════════════════════════════════════════════════════════╣■
    Location:
        Name: {location.replace('_', " ").title()}
        Events: {events}
■╠═══════════════════════════════════════════════════════════╣■
 ║   Name: {name.title(): <12}Class: {prof.title(): <12}Race: {race.title(): <12} ║    
 ║                                                           ║                           
 ║   HP: {c.fg('green')}{bars(health_current, health_max)}{c.fmt('reset')}  ║                           
 ║   MP: {c.fg('blue')}{bars(mana_current, mana_max)}{c.fmt('reset')}  ║
 ║   XP: {c.fg('yellow')}{bars(xp_current, xp_next)}{c.fmt('reset')}  ║
 ║                                                           ║
 ║   Rations: {rations:0>3}      Sanity: {sanity:0>3}      Gold: {gold:0>10}     ║
■╠═══════════════════════════════════════════════════════════╣■

"""

    return game_menu


# Helper for event_text
def word_wrap(args):
    n: list = textwrap.wrap(
        args,
        51,
        break_long_words=True)
    f = []
    for chunk in n:
        f.append(f' ║  {"".join([a for a in chunk]): <55}  ║')
    return "\n".join([a for a in f])


def event_text(event):
    name = event['name']
    message = event['text']
    text = f"""
■╠═══════════════════════════════════════════════════════════╣■
\t Random Encounter!\n
■╠═══════════════════════════════════════════════════════════╣■
 ║  {name: <40}                 ║
 ║                                                           ║
{word_wrap(message)}
 ║                                                           ║
■╠═══════════════════════════════════════════════════════════╣■
    """
    return text
