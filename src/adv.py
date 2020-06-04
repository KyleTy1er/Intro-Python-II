from room import Room, Rooms

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
# r = Room('Master Bedroom', 'Nothing good is ever found here.')
# print(r)
# my_rooms = {
#     'master': Room('Master Bedroom', 'Nothing good is ever found here.'),
# }
# print(my_rooms['master'].get_description())
# print(room['outside'].get_description())

for key in room:
    print('key')

# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']



#
# Main
#
#print(room['outside'])
# Make a new player object that is currently in the 'outside' room.

import getpass

# playerName = Player(getpass.getuser().title())
#
# print("Welcome{}".format(playerName.__str__()),"press a directional key ('W,A,S,D') to move...")
#
# # Write a loop that:
#
# tries = 0
# while tries < 10:
#     tries += 1
#     entry = str(input())
#     playerName.change_rooms(entry)
#     # * Prints the current room name
#     print(f" You are now in the '{playerName.get_current_room()}'")
#     # * Prints the current description (the textwrap module might be useful here).






# print(room.__str__())


# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
