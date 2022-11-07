import os
import shlex
import traceback
from dataclasses import dataclass

import config
from utils.TextUtils import clear_screen, menu_static, cont, menu_write
from utils.GameStates import delete_game, new_game, load_game, save_game
from utils.ChangeLocation import change_location

import player_info
from menus import creator


c = creator.Creator()

fresh_load = True


@dataclass
class Menu:
    """Menu command class"""

    command: str
    arguments: list[str]


def main_menu(command: Menu) -> None:
    """Main Menu -
    :option 1 - New Game
        Starts a new game. TODO: replace object save: int, with save += 1
    :option 2 - Load Game
        Loads a save from file. TODO: Prompt user to input save number to load from
    :option 3 - Save Game
        Saves the current player data in save_data.txt.
    :option 4 - Delete Save
        Deletes a save object from file. TODO: Prompt user to which object they wish to delete
    :option 5 - Rules
        Print the rules, and legend for the game.
    :option 6 - Exit
        Exits the program. Saves the game to whichever save is currently loaded. TODO: Create new save profile if none
    """
    path = os.path.join(os.path.dirname(__file__), 'save_data.txt')
    if os.path.exists(path):
        save_file = True
    else:
        save_file = False

    match command:
        case Menu(command='1'):
            new_game()

            c.build()
        case Menu(command='2'):
            print('Loading Game...')
            try:
                load_game()
                change_location(player_info.info['location'])
            except Exception as e:
                menu_write(title="Exception", text=traceback.format_exception(e), delay=0.01)
                input()

        case Menu(command='3'):
            if save_file:
                save_game()
                print('Game Saved!')
                cont()
            else:
                save_game()
                print('New save Created')
                cont()
        case Menu(command='4'):
            if save_file:
                print(config.line_break_fancy)
                print(f'\tDelete Save?')
                print(config.line_break_fancy)
                delete = input(f'\nAre you sure you wish to delete your save? (yes/no)\n >> ')
                if delete.lower() == 'yes':
                    delete_game()
                else:
                    return
        case Menu(command='5'):
            print(f'These are the rules')
        case Menu(command='6'):
            print(config.line_break_fancy)
            print('\nExiting Game...\nSaving player data...')
            save_game()
            exit(0)
        case _:
            print(f'{config.unknown_command} {command!r}.')


def main() -> None:

    while True:
        # path = os.path.join(os.path.dirname(__file__), 'save_data.txt')
        path = 'save_data.txt'
        if os.path.exists(path):
            save_file = True
        else:
            save_file = False

        if save_file:
            text = f"""
    [1] -  New Game
    [2] -  Load Game
    [3] -  Save game
    [4] -  Delete Save

    [5] -  Rules
    [6] -  Exit"""
        else:
            text = f"""
    [1] -  New Game

    [5] -  Rules
    [6] -  Exit"""
        clear_screen()
        menu_static('Main Menu', text)
        try:
            command, *arguments = shlex.split(input('\nPlease make a selection\n >> '))
            main_menu(Menu(command, arguments))
        except ValueError:
            print('Invalid Selection')
            cont()
