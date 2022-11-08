import random

vowels = ["a", "e", "i", "o", "u"]


class Player:
    def __init__(self, data: dict):
        self.data = data

    def do_attack(self):
        pass


class Monster:
    def __init__(self, data: dict):
        self.data: dict = data['default']

    def spawn(self):
        monster: str = f'{"an" if self.data["name"][:1].lower() in vowels else "a"} {self.data["name"]}'
        print(f"You encountered {monster}!")

    def get_stat(self, stat):
        return self.data[f'{stat}']

    def get_health(self) -> int:
        return self.data['health']

    def get_damage(self) -> int:
        return self.data['damage']

    def drops(self) -> list:
        return self.data['drops']

    def give_drop(self):
        drops: list = self.data['drops']
        try:
            return random.choice(drops)
        except IndexError:
            return None

    def experience_gain(self) -> int:
        return self.data['experience']

    def do_attack(self):
        pass
