from Characters import Monster


class Goblin(Monster):
    def __init__(self, data):
        super().__init__(data)
        self.data = data['goblin']


class Troll(Monster):
    def __init__(self, data):
        super().__init__(data)
        self.data = data['troll']


class Slime(Monster):
    def __init__(self, data):
        super().__init__(data)
        self.data = data['slime']


class Wolf(Monster):
    def __init__(self, data):
        super().__init__(data)
        self.data = data['wolf']


class Rat(Monster):
    def __init__(self, data):
        super().__init__(data)
        self.data = data['rat']


class BloodLizard(Monster):
    def __init__(self, data):
        super().__init__(data)
        self.data = data['lizard']


class Necromancer(Monster):
    def __init__(self, data):
        super().__init__(data)
        self.data = data['necromancer']


class Skeleton(Monster):
    def __init__(self, data):
        super().__init__(data)
        self.data = data['skeleton']


class Shroom(Monster):
    def __init__(self, data):
        super().__init__(data)
        self.data = data['shroom']
