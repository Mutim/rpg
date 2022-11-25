from items.materials import materials
import random
material: str = random.choice(materials)

data = {
    'goblin': {
        'name': 'Goblin',
        'health': 10,
        'damage': 2,
        'drops': [material],
        'experience': 2
    },
    'troll': {
        'name': 'Troll',
        'health': 1,
        'damage': 1,
        'drops': ['Troll Fur', material],
        'experience': 1
    },
    'slime': {
        'name': 'Slime',
        'health': 1,
        'damage': 1,
        'drops': ['Slime Jelly', 'Goo', material],
        'experience': 1
    },
    'wolf': {
        'name': 'Wolf',
        'health': 1,
        'damage': 1,
        'drops': ['Wolf Pelt', 'Wolf Tooth', material],
        'experience': 1
    },
    'rat': {
        'name': 'Rat',
        'health': 1,
        'damage': 1,
        'drops': ['Rat Tail', 'Rat Fur', 'Whisker', material],
        'experience': 1
    },
    'lizard': {
        'name': 'Lizard',
        'health': 1,
        'damage': 1,
        'drops': ['Lizard Eye', 'Small Scale', material],
        'experience': 1
    },
    'skeleton': {
        'name': 'Skeleton',
        'health': 1,
        'damage': 1,
        'drops': ['Bone Dust', material],
        'experience': 1
    },
    'necromancer': {
        'name': 'Necromancer',
        'health': 1,
        'damage': 1,
        'drops': ['Bone Dust', material],
        'experience': 1
    },
    'shroom': {
        'name': 'Shroom',
        'health': 1,
        'damage': 1,
        'drops': ['Red Mushroom', 'Green Mushroom', 'Blue Mushroom', material],
        'experience': 1
    }
}

enemies_list = [k for k in data.keys()]
