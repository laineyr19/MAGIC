# Now we have a premise. We are in a room and we have two door to choose from.
# We are still in the blue room. What do we do with the treasure chest?
# New code starts at line 33
#
# Loop and another way of doing if statment
#
# Run this code a few times and see what happens with different choices.
# It's good to test all options and see if that's what you expected.

##### ACTIONS #####
def you_died(why):
    # You expect a reason why the player died. It's a string.
    print("{}. Good job!".format(why))

    # This exits the program entirely.
    exit(0)

### END ACTIONS ###

##### ROOMS #####
def blue_door_room():
    # So our treasure_chest list contains 4 items.
    treasure_chest = ["diamonds", "gold", "silver", "sword"]
    print("You see a room with a wooden treasure chest on the left, and a sleeping guard on the right in front of the door")

    # Ask player what to do.
    action = raw_input("What do you do? > ")

    # This is a way to see if the text typed by player is in the list
    if action.lower() in ["treasure", "chest", "left"]:
        print("Oooh, treasure!")

        print("Open it? Press '1'")
        print("Leave it alone. Press '2'")
        choice = raw_input("> ")

        if choice == "1":
            print("Let's see what's in here... /grins")
            print("The chest creaks open, and the guard is still sleeping. That's one heavy sleeper!")
            print("You find some")


            # FOR LOOP
            # for each treasure (variable created on the fly in the for loop)
            # in the treasure_chest list, print the treasure.
            for treasure in treasure_chest:
                print(treasure)
        elif choice == "2":
            print("you trip while walking and make a big noise.  The guard wakes up!")
            r = raw_input("what do you do?")    
            pink_room(r)
    else:
        print("The guard is more interesting, let's go that way!")

def pink_room(choice_2):
    print("the pink room is full of candy")
    c = raw_input("what candy do you want?")
    candy(c)

def candy(yay):
    if yay == "snickers":
        print("you start laughing")
    elif yay == "kit kat":
        print("a cat falls and lands on your head")


def red_door_room():
    print("There you see a great red dragon.")
    print("It stares at you through one narrowed eye.")
    print("Do you flee for your life or stay?")

    next_move = raw_input("> ")

    # Flee to return to the start of the game, in the room with the blue and red door or die!
    if "flee" in next_move:
        start_adventure()
    else:
        # You call the function you_died and pass the reason why you died as
        # a string as an argument.
        you_died("It eats you. Well, that was tasty!")
### END ROOMS ###

def start_adventure():
    print("You enter a room, and you see a red door to your left and a blue door to your right.")
    door_picked = raw_input("Do you pick the red door or blue door? > ")

    # Pick a door and we go to a room and something else happens
    if door_picked == "red":
        red_door_room()
    elif door_picked == "blue":
        blue_door_room()
    else:
        print("Sorry, it's either 'red' or 'blue' as the answer. You're the weakest link, goodbye!")

def main():
    player_name =  raw_input("What's your name? >")
    print("Your name is {}".format(player_name.upper()))

    start_adventure()

if __name__ == '__main__':
    main()