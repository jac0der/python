'''
    Exploring python modules setup and usages.
    @datetime:: August 8, 2024 3:05 am (UTC-5)
    @author:: jac0der
'''

# import all definitions from the load module
import load

# import specific definitions, not the whole pause module
from pause import is_paused, something_other_method

# import from the standard python library
import math

# import all definitions from a module
from play import *

# importing module from folder structure - use dot syntax
import boss.boss_player
from boss.boss_player import get_life


# caling methods from the load module
load.load()
load.is_loaded(True)
print()

# calling method from the pause module
is_paused(False)
print()

# calling methos from the python math module
print(math.sqrt(16))
print(math.factorial(7))
print()

# calling methods from the play module
play()
is_playing(True)
print()

# calling boss player methods
print(boss.boss_player.get_powers())
print(get_life())