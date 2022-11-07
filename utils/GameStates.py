import time
import json

import config
import player_info
from utils.TextUtils import cont


def load_resources():
    print('Loading Resources...')
    new_game()
    time.sleep(1)


def save_game():
    with open("save_data.txt", "w+") as f:
        j = json.dumps(player_info.info, ensure_ascii=True, indent=4)
        f.write(str(j))


def delete_game():
    with open('save_data.txt', 'w+') as f:
        f.flush()


def load_game():
    try:
        with open('save_data.txt', 'r') as f:
            data = f.read()
            fi = json.loads(data)
            player_info.info.update(fi)
    except FileNotFoundError:
        print('Save file not found. Please start a new game.')
        cont()
    except KeyError:
        print('Corrupted Save File.')
        cont()


def new_game():
    player_data = json.dumps(config.info, ensure_ascii=True, indent=4)
    player_info.info = json.loads(player_data)

