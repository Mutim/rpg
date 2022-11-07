
line_break_fancy = "■├──────────────────────────────────────────────────────────┤■"
line_break_bold =  "■╠══════════════════════════════════════════════════════════╣■"

unknown_command = "Bad Selection | "

world_name = "Erawyn"

text_delay = 0.025

possible_classes = ["archer", "mage", "warrior"]
"""
character_info: list
    0 - equipment: dict
        Objects (equipment template)
        0 - head
        1 - body
        2 - hands
        3 - legs
        4 - feet
        5 - primary_hand
        6 - secondary_hand
        7 - jewels
    inventory: list
    effects: list
"""

info = {
    "save": 0,
    "name": "",
    "race": "",
    "prof": "",
    "level": 0,
    "health": {
        "max": 10,
        "current": 10
    },
    "mana": {
        "max": 10,
        "current": 10
    },
    "experience": {
        "current": 0,
        "next": 10
    },
    "location": "",
    "sanity": 100,
    "rations": 0,
    "gold": 0,
    "inventory": {

    },
    "equipment": {
        "head": {},
        "body": {},
        "hands": {},
        "legs": {},
        "feet": {},
        "main_hand": {},
        "off_hand": {},
        "jewels": {}
    },
    "world_info": {
        "event": "None"
    }

}
inventory = {
    "slots": []
}

effects = {
    "effects": []
}

da_rules = """
■╠═══════════════════════════════════════════════════════════╣■
 ║ x  0  1  2  3  4  5  6  7  8  9  10  11  12             ║
 ║ 0 |                                                       ║
 ║ 1 |                                                       ║
 ║ 2 |                                                       ║
 ║ 3 |                                                       ║
 ║ 4 |                                                       ║
 ║ 5 |                                                       ║
 ║ 6 |                                                       ║
 ║ 7 |                                                       ║
 ║ 8 |                                                       ║
 ║ 9 |                                                       ║
 ║ 10|                                                       ║
 ║ 11|                                                       ║
 ║ 12|                                                       ║
■╠═══════════════════════════════════════════════════════════╣■
"""

