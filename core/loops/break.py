"""
    Using the break keyword to exit a loop.

    @datetime:: October 16, 2023 11:47 am (UTC-5)
    @author:: jac0der
"""

#*** 1 => role playing game
"""
    Create a role player game where a player health is attacked by an enemy with
    a random attack power.

    If the player's health becomes 30, theb break out of the while loop.
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

    if playerhp == 30:
        print("You have low health. You've been teleported to the nearest inn.")
        break


print('\n')
#*** 2 => Generate a List of Dictionaries
"""
    Creating 30 players with their specified offences and defensies.
    Change the 2nd to last players offensies to have no offensies.
    loop through List of dictionaries and when the player with no
    offenssies is reached, break from the loop.
"""

# create empty List to store dictionary of players
players = []

# loop 30 times - use the range() function
for loop_count in range(30):
    #create a new player dictionary.
    new_player = {
        'health': 260,
        'offensies': ['spear', 'knife', 'ak-47', 'bazuka'],
        'defensies': ['sheild', 'smoke', 'coat']
    }

    # add new player to players List
    players.append(new_player)

# get 2nd to last player
second_to_last_player = players[-2]

# set 2nd to last player to have no offensies - clear offensies List
second_to_last_player['offensies'].clear()

count = 0

# loop through the players List and break when player with no 
# offensies is reached. 
# so after the 28th player is passed, at the 29th player the loop
# will break, NOT processing player 30
for player in players:

    if len(player['offensies']) == 0: # get length of List
        break
    
    count+=1
    print(f"Count is {count}")

#print(players)