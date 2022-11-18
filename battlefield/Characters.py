import random
from battlefield import MonsterData

vowels = ["a", "e", "i", "o", "u"]


class Player:
    def __init__(self, data: dict):
        self.data = data

    def do_attack(self):
        pass

    def get_stat(self, stat):
        return self.data[f'{stat}']


class Monster:
    def __init__(self):
        monster = random.choice(list(MonsterData.data.keys()))
        self.data: dict = MonsterData.data[f'{monster}']

    def spawn(self):
        monster: str = f'{"an" if self.data["name"][:1].lower() in vowels else "a"} {self.data["name"]}'
        print(f"You encountered {monster}!")

    def get_stat(self, stat):
        return self.data[f'{stat}']

    def get_health(self) -> int:
        return self.data['health']

    def get_damage(self) -> int:
        return self.data['damage']

    def drops(self):
        try:
            return random.choice(self.data['drops'])
        except IndexError:
            return None

    def give_drop(self):
        drops: list = self.data['drops']
        try:
            return random.choice(drops)
        except IndexError:
            return None

    def experience_gain(self) -> int:
        return self.data['experience']

    def do_attack(self):
        print(f'{self.data["name"]} attacked you for {self.data["damage"]}')
