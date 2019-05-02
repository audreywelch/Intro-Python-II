from room import Room
from player import Player
from lib import Description
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Mysterious Entrance",
                     "North of you, the yellow & blue shimmer beckons"),

    'foyer':    Room("IKEA Foyer", """Dim light filters in from the south.
Blaring white passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'cafeteria': Room("Treasure Chamber AKA Cafeteria", """You've found the long-lost treasure chamber
# of juicy swedish meatballs and tart lingonberry sauce! Sadly, all remaining swedish meatballs have
# already been devoured by earlier adventurers. The only exit is back the way you came. Good luck."""),
}

item_strings = [
['\nEktorp-Sofa', 'This couch really seals your committment to that quintessential Scandinavian aesthetic.\n$379'],
['\nLack-Side-Table', 'Yep, you just scored a side table for less than you spent on lunch yesterday. Nice.\n$7.99'],
['\nRens-Sheepskin-Rug', 'In case you were wondering whether sheepskin rugs are still trending - the answer is yes.\n$29.99'],
['\nIngabritta-Throw', 'If that doesn\'t scream pure hygge, I don\'t know what does!\n$24.99'],
['\nFärgrik-Mug', 'A 99-cent mug doesn\'t need much of an explanation. It holds coffee. It costs a buck.\n$0.99'],
['\nKryddnejlika', 'Hmmm, nope, we don\'t know what that is either.\n$5.99'],
['\nFree-Snowman', 'Some assembly required 🤷‍♀️']
]

items = [Item(item[0], item[1]) for item in item_strings]
print(items)

room['foyer'].storage = items[0:2]
room['overlook'].storage = items[2:5]
room['narrow'].storage = items[5]
room['treasure'].storage = items[6]


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Helper functions that turns the string input into a class property
def get_room(cmd, current_room):
    if cmd == 'n':
        return current_room.n_to
    if cmd == 's':
        return current_room.s_to
    if cmd == 'e':
        return current_room.e_to
    if cmd == 'w':
        return current_room.w_to

# def get_action(cmd, )

## Valid Directions
directions = ['n', 's', 'e', 'w']

## Valid Verb Commands
actions = ['get', 'drop']




#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Audrey", room['outside'])

# Write a loop that:
while True:

    print(f'\nYou are in the: {player.current_room}')
    print(f'\nItems in this room: {player.current_room.storage}\n')

    # * Waits for user input and decides what to do.
    raw_input = input("Where do you want to go? -> ")
    cmd = raw_input.split()

    # If user enters ONE word
    ## If the user enters a cardinal direction, attempt to move to the room there.
    if len(cmd) < 2:   
        if cmd[0] in directions:
            new_room = get_room(cmd[0], player.current_room)
            if new_room is not None:
                player.current_room = new_room
            else:
                print("You can't move any farther in that direction - you must stick to the maze- ahem, I mean the path.")
    
        elif cmd == 'i' or 'inventory':
            print(f'My shopping cart: {player.storage}')
        
        elif cmd == 'q':
            print("Goodbye!")
            break
    
        else:
            print("Please enter a key to continue...\n [n]orth\n [s]outh \n [e]ast \n [w]est \n or [q]uit")

    # If user enters TWO words
    elif len(cmd) == 2:
        # cmd[0] // Action Verb
        # cmd[1] // Item

        # If user wants to GET an item...
        if cmd[0] == 'get':

            # if the current room has the item...
            if cmd[1] in player.current_room.storage:
                # remove it from the room's contents...
                player.current_room.storage.remove(cmd[1])
                # and add it to the player's contents
                player.storage.append(cmd[1])

                # tell user they now have the item

            else:
                print(f'Sorry, there is no {cmd[1]} in this room.')

        elif cmd[0] == 'drop':

            # if the player has the item...
            if cmd[1] in player.storage:
                #remove it from the player's contents...
                player.storage.remove(cmd[1])
                # and add it to the room's contents
                player.current_room.storage.append(cmd[1])
            else:
                print(f'Sorry, you don\'t have a {cmd[1]}.')

        else:
            print("Invalid input.")

       

    # if cmd == 'n':
    #     if player.current_room.n_to is not None:
    #         player.current_room = player.current_room.n_to

    #         # Prints the current room name
    #         print(f"You are in the: {player.current_room.name}")
    #         # Prints the current description
    #         print(player.current_room.description)
    #     else:
    #         print("Please enter a valid command. Choose 'n' to go north, 's' to go south, 'e' to go east, 'w' to go west, or 'q' to quit.")

    # elif cmd == 's':
    #     if player.current_room.s_to is not None:
    #         player.current_room = player.current_room.s_to

    #         # Prints the current room name
    #         print(f"You are in the: {player.current_room.name}")
    #         # Prints the current description
    #         print(player.current_room.description)
    #     else:
    #         print("Please enter a valid command. Choose 'n' to go north, 's' to go south, 'e' to go east, 'w' to go west, or 'q' to quit.")

    # elif cmd == 'e':
    #     if player.current_room.e_to is not None:
    #         player.current_room = player.current_room.e_to

    #         # Prints the current room name
    #         print(f"You are in the: {player.current_room.name}")
    #         # Prints the current description
    #         print(player.current_room.description)
    #     else:
    #         print("Please enter a valid command. Choose 'n' to go north, 's' to go south, 'e' to go east, 'w' to go west, or 'q' to quit.")

    # elif cmd == 'w':
    #     if player.current_room.w_to is not None:
    #         player.current_room = player.current_room.w_to

    #         # Prints the current room name
    #         print(f"You are in the: {player.current_room.name}")
    #         # Prints the current description
    #         print(player.current_room.description)
    #     else:
    #         print("Please enter a valid command. Choose 'n' to go north, 's' to go south, 'e' to go east, 'w' to go west, or 'q' to quit.")

    # # If the user enters "q", quit the game.
    # elif cmd == 'q':
    #     print("Goodbye!")
    #     break

    # # Print an error message if the movement isn't allowed.
    # else:
    #     print("Please enter a valid command. Choose 'n' to go north, 's' to go south, 'e' to go east, 'w' to go west, or 'q' to quit.")