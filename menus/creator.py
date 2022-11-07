import random

import config
import player_info
import time
from config import text_delay
from utils.ChangeLocation import change_location
from utils.GameStates import save_game
from utils.TextUtils import cont, clear_screen, think, write, menu_write, vowels


class Creator:
    name = ''
    race = ''
    prof = ''

    def build(self):
        clear_screen()
        build_text = [f"[ Grundle ] - Welcome to the world of {config.world_name.title()}!",
                      "You must be a bit confused. Let me introduce myself.",
                      "My name is Grundle, the helpful Green Mage that nursed you back to life with magic herbs.",
                      "If I may run some test on you... don't look so scared, they won't hurt!\n", ]
        menu_write('Character Creator', build_text, text_delay)

        input(f'\n[ Press ENTER to Continue ]')
        clear_screen()
        write([f"Just a little to the left..."], text_delay)
        time.sleep(1.3)
        write(["""
                        ...and put this here..."""], text_delay)
        time.sleep(1.3)
        write(["""
        ..                                 ...and a ting of the crystal!"""], text_delay)
        time.sleep(1)
        write(["\nThere we go, good as new! Now, some questions....\n"], text_delay)
        time.sleep(1.3)
        self.build_name()

    def build_name(self):
        menu_write('Character Name', ['What do people call you?', '(12 characters max)'], text_delay)
        while True:
            self.name = input('\n >> ')
            if len(self.name) <= 12:
                break
            else:
                print(f'{self.name} is greater than 12 characters. Try again')
        print(f'\nI see, so your name is {self.name}! Two more questions, are you ready?')
        cont()
        player_info.info.update({'name': f'{self.name}'})
        self.build_race()

    def build_race(self):
        menu_write(
            'Character Race',
            ["Do you remember your race? You look a bit... Dwarfish, to me."],
            text_delay)
        while True:
            self.race = input('\n >> ')
            if len(self.race) <= 12:
                break
            else:
                print(f'{self.race} is greater than 12 characters. Try again')
        print(f'\nAhhhh, I can see that! My mothers half-sister, twice removed was also '
              f'{"an" if self.race[:1].lower() in vowels else "a"} {self.race}!')
        cont()
        player_info.info.update({'race': f'{self.race}'})
        self.build_prof()

    def build_prof(self):
        menu_write('Class Selection', ['Final question. What job did you have before I found you?',
                                       '\n(Archer, Mage, Warrior)'], text_delay)
        while True:
            self.prof = input(f'\n >> ')
            denied_text = [f"{self.prof} isn't a real job you know...",
                           f"You expect me to believe you were a {self.prof.title()}?",
                           f"Serioiusly? A {self.prof}? That's not even a word!",
                           f"I can't let you out of my sight until I know your real job.",
                           f"A {self.prof} can't be right. Maybe you are sick..."]
            if self.prof.lower() not in config.possible_classes:
                print(f"\n{random.choice(denied_text)}")
            else:
                break
        write(
            [f'\nOh? So you claim you were {"an" if self.prof[:1].lower() in vowels else "a"} {self.prof.title()}?\n',
             f'\t{think("They look more like a carriage driver to me, but who am I to say...")}'],
            text_delay)

        cont()
        player_info.info.update({'prof': f'{self.prof}'})

        menu_write("Character Confirm",
                   [f"So, let's see if we got this right. Your name is {self.name}\n",
                    f"And you are {'an' if self.race[:1].lower() in vowels else 'a'} {self.race.title()}\n",
                    f"And you **claim** that you were {'an' if self.prof[:1].lower() in vowels else 'a'} {self.prof.title()}",
                    f"                    ",
                    f"Did I hear you right? ",
                    "   [1] -  Yes",
                    "   [2] -  No"], text_delay)
        confirm = input(f'\n  >> ')
        if not confirm == '1':
            print(f"Oh, I must have misheard you. Let's try this again then, shall we?")
            cont()
            self.build_name()
        clear_screen()
        menu_write("Character Creator",
                   [f"[ Grundle ] - That settles it then {self.name}! You seem like a healthy {self.race} to me.",
                    f"This town could really use someone like you. Every {self.prof.title()} worth their salt",
                    f"can find work posted in the *Tavern. Just leave my *Apothecary, and head North!",
                    f"    ",
                    f"Anyone can make a name for themselves if they put their mind to it. Good Luck to you!",
                    "              ",
                    f"\t{think('They wont last a week...')}"], text_delay)

        input(f'\n[ Press ENTER to Continue ]')
        save_game()
        change_location('apothecary')
        clear_screen()


def main():
    pass
