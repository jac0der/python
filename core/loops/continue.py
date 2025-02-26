"""
    Using the continue keyword to force a next loop 
    iteration, ignoring codes whic comes after.

    @datetime:: October 16, 2023 12:15 pm (UTC-5)
    @author:: jac0der
"""
import random


playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:

    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enenmy strikes for ", dmg, " points of damage. Current HP is", playerhp)

    # once player is healthy (have enough health points), continue looping.
    if playerhp > 30:
        continue
    
    # once playerhp becomes less than 30, THEN, I run these 2 last code lines..
    print("You have low health. You've been teleported to the nearest inn.")
    break
