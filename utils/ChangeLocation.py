import interests_points
import player_info
from utils.TextUtils import cont, menu_write
import traceback


def change_location(location: str):
    def no_location():
        print(f'It seems that you have no location saved. Moving you to the the Apothecary*')
        player_info.info["location"] = 'apothecary'
        cont()
        interests_points.Apothecary.main()

    try:
        player_info.info["location"] = location
        # Add key to TextUtils
        locations = {
            '': no_location,
            'town': interests_points.Town.main,

            'apothecary': interests_points.Apothecary.main,
            'blacksmith': interests_points.Blacksmith.main,
            'bubbling_cauldron': interests_points.BubblingCauldron.main,
            'fletcher': interests_points.Fletcher.main,
            'guild_hall': interests_points.GuildHall.main,
            'mystic_emporium': interests_points.MysticEmporium.main,
            'tavern': interests_points.Tavern.main,

            'battlefield': interests_points.Battlefield.main
        }
        locations[f'{location}']()
    except Exception as e:
        menu_write(title="Exception", text=traceback.format_exception(e), delay=0.01)
        input()
