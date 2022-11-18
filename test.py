from battlefield import Characters
from battlefield import Monsters
from battlefield import MonsterData
import random

monsters = random.choice(list(MonsterData.data.keys()))

m = Characters.Monster()
p = Characters.Player

m.spawn()
m.do_attack()
print(m.drops())

