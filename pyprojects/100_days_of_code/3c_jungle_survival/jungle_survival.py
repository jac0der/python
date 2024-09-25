'''
    Program to guide a player to survive or escape 
    the jungle based on selected options.

    @datetime:: September 21, 2024 5:25 am (UTC-5)
    @author:: jacoder
'''


def main():
    draw_banner()
    survive_jungle()


def draw_banner():
    print('''
        d8b                         888         
        Y8P                         888         
                                    888         
        8888888  88888888b.  .d88b. 888 .d88b.  
        "888888  888888 "88bd88P"88b888d8P  Y8b 
        888888  888888  888888  88888888888888 
        888Y88b 888888  888Y88b 888888Y8b.     
        888 "Y88888888  888 "Y88888888 "Y8888  
        888                     888            
       d88P                Y8b d88P            
    888P"                  "Y88P" 
    ''')


def survive_jungle():
    print("Welcome to Jungle Survival.")
    print("Your mission is to survive by finding an escape route out of the Jungle.")
    print("You are deep in the jungle, at your feet is a waterproof back pack and a few resource items.")
    print("Pack your backpack or leave the backpack.")
    print(''' 
                0. Knife
                1. Rope (50 feet)
                2. Scuba Gears (suit, goggles, tank and fin)
                3. Drinking Water
                4. Juice
                5. Large Meat
                6. Flashlight
                7. Boots
                8. Horn
                9. Flare
                10. Compass
                11. Bread
                12. Rifle
                13. Bow and Arrows
                14. Parashoot
                15. Saw
                16. Warm Sleeping bag (for very cold weathers)
                17. Map
                18. First Aid Kit

    \n''')

    signaling_items_dict = {
        '6': 'Flashlight',
        '8': 'Horn',
        '9': 'Flare',
        '12': 'Rifle'
    }

    chosen_items = None

    while True:

        choice = input("Choose only '5' items (0,1,2...) or type 'none' to leave backpack or 'q' to quit:   ").rstrip().lower()
        
        if choice == "q":
            print("Bye...")
            return 0

        elif choice == "none":
            break

        elif len(choice) == 0:
            print("Select resource items.\n")
     
        elif len(choice) > 0:
            chosen_items = choice.split(",")

            if len(chosen_items) > 5:
                print("Too many resource items selected. Please reselect items.\n")
            else:
                break
        
    direction = input("Let's Go! You can go 'North' or 'South' or 'q' to quit:\n").rstrip().lower()

    if direction == "q":
        print("Bye...")
        return 0
    
    elif direction == "south":

        if chosen_items == None:
            print("You cannot survive this jungle with nothing. A Black Momba has poisoned you with venom. Game Over!".upper())
            return 0

        print("After walking for many hours you come to a cliff approximately 50 feet.")
        cliff_decision = input("    Type 'down' to go down the cliff or 'up' to return to starting point. or 'q' to quit\n").rstrip().lower()

        if cliff_decision == "q":
            print("Bye...")
            return 0
        
        elif cliff_decision == 'down':

            # check if the Rope or Parashoot was packed.
            if '1' in chosen_items or '14' in chosen_items:
                print("You have made it to the bottom of the cliff safely where there is now a flowing river.")
                river_decision = input("     Type 'swim' to swim accross the river or 'walk' to walk to a shallow section to walk across or 'q' to quit.\n").rstrip().lower()

                if river_decision == "q":
                    print("Bye...")
                    return 0
                
                elif river_decision == "swim":

                    # check if scoba diving gears were packed.
                    if '2' in chosen_items:
                        print("You have crossed the river safely. Do you now stop to eat and rest before night fall?")
                        eat_decision = input(" Type 'eat' to eat and rest or 'walk' to continue or 'q' to quit.\n")

                        if eat_decision == "q":
                            print("Bye...")
                            return 0
                        
                        elif eat_decision == "eat":
                            
                            if '3' in chosen_items or '4' in chosen_items or '5' in chosen_items or '11' in chosen_items:

                                print("Your feast has lasted into the night but you are full and replenished.")
                                
                                # check if flashlight was packed
                                if '6' in chosen_items:
                                    print("Do you wish to turn on your flashlight?")
                                    flashlight = input("        yes/no or 'q' to quit\n")

                                    if flashlight == "yes":
                                        print("Light has brought unnecessary attention by wild animals to kill you in your sleep. Game Over!")
                                        return 0

                                    elif flashlight == "q":
                                        print("Bye...")
                                        return 0

                                # check if warm sleeping bag was not packed
                                if '16' not in chosen_items:
                                    print("You have no proper cover to withstand the freezing temperature and with lack off food you freeze to death. Game Over!") 
                                    return 0

                                print("It is not morning time, and the brigthness of the day also reveals in the distance civilization a few miles away.")
                                print("Congratulations, you have survived the jungle.")
                            

                            elif '3' not in chosen_items and '4' not in chosen_items and '5' not in chosen_items and '11' not in chosen_items:

                                print("You packed nothing to eat or drink. It is now night time, do you want to make camp now?")
                                make_camp = input(" Type 'yes' or 'no' or 'q' to quit.\n").rstrip().lower()

                                if make_camp == "q":
                                    print("Bye...")
                                    return 0
                                
                                elif make_camp =="yes":
                                    print("You have successfully made camp.")

                                    # check if flashlight was packed
                                    if '6' in chosen_items:
                                        print("Do you wish ao turn on your flashlight?")
                                        flashlight = input("        yes/no or 'q' to quit\n")

                                        if flashlight == "q":
                                            print("Bye...")
                                            return 0
                                        
                                        elif flashlight == "yes":
                                            print("Light has brought unnecessary attention by wild animals to kill you in your sleep. Game Over!")
                                            return 0

                                    # check if warm sleeping bag was not packed
                                    if '16' not in chosen_items:
                                        print("You have no proper cover to withstand the freezing temperature and with lack off food you freeze to death. Game Over!") 
                                        return 0

                                    print("It is not morning time, and the brigthness of the day also reveals in the distance civilization a few miles away.")
                                    print("Congratulations, you have survived the jungle.")


                                else:
                                    print("Wild animals have ambushed you in the unknown jungle teritory at night and devoured your flesh.")
                                    print("Game Over!")
                                    return 0

                        elif eat_decision == "walk":
                            print("Your body has shut down and caused sudden death due to the extreme pressures of walking and carrying load and lack of food and rest.")
                            print("Game Over!")
                            return 0

                        else:
                            print("Inhaling excessive toxic gas from the jungle air has fried your lungs and you suffocate. Game Over!")
                            return 0
                    else:
                        print("You have been drowned by the depth of the water an its current without proper resource gears. Game Over!")
                        return 0

                elif(river_decision == "walk"):

                    print("You have successfully crossed the river with more strenght to spare compared to if you had swam across.")
                    print("In the distance you can finally see civilization. You keep walking to reach before nightfall or make camp for the night then continue tomorrow?")
                    camp  = input("     Type 'camp' or 'walk' or 'q' to quit.\n").rstrip().lower()

                    if camp == "q":
                        print("Bye...")
                        return 0
                    
                    elif camp == "walk":
                        print("Congratualtions, persistence with reserved energy from the river crossing decision has made you survived the Jungle before nightfall")

                    elif camp == "camp":       
                        # check if sleeping bag was packed                                                     # check if warm sleeping bag was not packed
                        if '16' not in chosen_items:
                            print("You have no proper cover to withstand the freezing temperature so you freeze to death. Game Over!") 
                            return 0

                        if '0' not in chosen_items and '12' not in chosen_items and '15' not in chosen_items:
                            print("You have nothing to defend rourself with so animals devoured you. Game Over!")
                            return 0 
                        
                        # check if flashlight was packed
                        if '6' in chosen_items:
                            print("Do you wish to turn on your flashlight?")
                            flashlight = input("        yes/no or 'q' to quit.\n")

                            if flashlight == "q":
                                print("Bye...")
                                return 0
                            
                            elif flashlight == "yes":
                                print("Light has brought unnecessary attention by wild animals to kill you in your sleep. Game Over!")
                                return 0

                        print("You have survived the night and can now walk safely to civilization just a few miles away.")
                        print("You have survived the Jungle!")

                    else:
                        print("A large Gorilla has bashed your head in. Game Over!")
                        return 0
                else:
                    print("A 15 foot CROC has had its belly full today. You are no match for the mighty Nile man eating CROC. Game Over!")
                    return 0

            elif '1' not in chosen_items and '14' not in chosen_items:
                print("You have fallen 50 feet to your death from the cliff. You have no resource item to go down the cliff. Game Over!")
                return 0

        elif cliff_decision == "up":

            if '5' in chosen_items:
                print("On your way south, you left the scent of your large meat in the air picked up by a pride of Lions.")
                print("The Lions attacked you and killed you for the meat. Game Over!")
                return 0

            else:
                print("The thunder of scattering preys due to a Tiger attack has cause a bowlder to roll down and crush you. Game Over!")
                return 0   

        else:
            print("As the rain pour down on the jungle, lightening stroke you. Game Over!")
            return 0

    elif direction == "north":
        
        print("Up north is a steep mountain that if you get to the top you will be rescude or eaten by tigers.")
        print("You come to an old broken down hut, do you enter to rest or keep walking?")
        enter = input("     Type 'enter' to rest or 'walk' to keep going or 'q' to quit.\n").rstrip().lower()

        if enter == "q":
            print("Bye...")
            return 0

        elif enter == "walk":
            print("A pack of wolves have picked up your trail, do you defend yourself or run?")
            defend = input("        Type 'defend' or 'run' or 'q' to quit.\n")

            if defend == "q":
                print("Bye...")
                return 0
            
            elif defend == "defend":

                if chosen_items == None:
                    print("You cannot survive this jungle with nothing. A Rhino has punched your chest. Game Over!".upper())
                    return 0

                if '0' not in chosen_items and '12' not in chosen_items and '15' not in chosen_items:
                    print("You have nothing to defend rourself with so the wolves devoured you. Game Over!")
                    return 0 
                
                else:
                    print("You have successfully ran off the wolves with either your rifle, knife or saw.\n")
                    print("While walking you slipped and cut your leg on an old rusty tiger poucher trap.")
                    firstaid = input("      Do you have first aid medicine to clean wound? 'y' or 'n' or 'q' to quit.\n").rstrip().lower()

                    if firstaid == "q":
                        print("Bye...")
                        return 0
                    
                    elif firstaid == "y" and '18' in chosen_items:

                        print("Wound cleaned and wrapped successfully.\n\n")
                        print("Though hopping, you have finally reached the top of the mountain at night.")
                        print("To be rescude you must signal the rescuers who have been searching for you in a Hellicoptor with beam lights.")
                        rescueitems = input("        Type 'view' to view your rescue items or 'q' to quit.\n").rstrip().lower()

                        if rescueitems == "view":
                            has_signaling_item = False

                            for signaling_key, signaling_item in signaling_items_dict.items():

                                if signaling_key in chosen_items:
                                    has_signaling_item = True
                                    print(f"     {signaling_key}. {signaling_item}")

                            if has_signaling_item == False:
                                print("You have no items to signal the recure Helicopter, so you are left alone in the Jungle with a bad wound.")
                                print("With no more medicine, you die either of infection and dehydration or you are eaten by the moutain Tigers. Game Over!")
                                return 0

                            signalitem = input("Select rescue item(s) to signal the Helicopter (6,8,9...) or 'q' to quit.\n")

                            if signalitem == "q":
                                print("Bye...")
                                return 0
                            
                            elif signalitem == '6':
                                print("Your Flashlight beam has been spotted by the helicopter. You have been rescued and survived the Jungle.")
                                    
                            elif signalitem == '8':
                                print("Your Horn has been heard by the helicopter pilots who have pinpointed your location and using their spot light have found you.")
                                print("You have been rescued and survived the Jungle.")

                            elif signalitem == '9':
                                print("The bright light from your Flare has caused the helicopter Pilots to quickly locate you're location. You have been rescued and survived the Jungle.")

                            elif signalitem == '12':
                                print("Your Rifle has been heard by the helicopter pilots who have pinpointed your location and using their spot light have found you.")
                                print("You have been rescued and survived the Jungle.")

                            else:
                                print("You do not know how to use your resource items, you have missed the helicopter. Have fun with the Tigers. Game Over!")         
                        
                        else:
                            print("Bye...")
                            return 0

                    else:
                        print("Your wound was badly infected causing blood poison. Game Over!")
                        return 0

            else:
                print("You cannot out run a pack of wolves, you have been wolf meat. Game Over!")
                return 0

        else:
            print("You have been bitten by a large King Cobra that was resting at the door of the hut.")
            print("You have been poisoned by the snake's Venom. Game Over!")
            return 0
    else:
        print("Invalid selection. Game over!")


if __name__ == "__main__":
    main()