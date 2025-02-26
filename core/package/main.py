'''
    Exploring python package setup and usages.
    @datetime:: August 16, 2024 10:12 am (UTC-5)
    @author:: jac0der
'''

# import module start from package and rename
import game.level.start as s

# import all functions from load module
from game.level.load import *

# import specific functions from over module
from game.level.over import get_level_details, apply_level_cheat_code

# importing from the sound package
import game.sound.load as sl

# import the open module
from game.image import open

s.start_game()
s.start_level()
s.is_level_started(True)
print()


# access all load methods
get_level()
load_level(2)
get_final_level()
print()


# using specific imported functions from the over module
get_level_details()
apply_level_cheat_code('coffee')
print()


# access function from the load module within the sound package
sl.load_sound()
print()

# access function from the open module
open.open_image()