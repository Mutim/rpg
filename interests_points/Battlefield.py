import player_info
from utils.BattleField import Battlefield


def main() -> None:
    player_level = player_info.info['level']
    bf = Battlefield(player_level)
