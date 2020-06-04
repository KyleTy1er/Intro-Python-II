from room import Room
from player import Player
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

# Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

# Main

import getpass

# instantiates a player class based on the getuser method of getpass:
playerName = Player(getpass.getuser().title())
# prints welcome message to player using playerName __str__ method:
print("Welcome{}".format(playerName),"press a directional key ('W,A,S,D') to move...")

# placeholder for tries while loop:
tries = 0
# limits the amount of possible moves to 10.
while tries < 10:
    tries += 1
    # stores the command line input into the variable entry:
    entry = str(input())
    # uses the input variable to call the change_rooms function:
    playerName.change_rooms(entry)
    # stores current room in variable cr:
    cr = playerName.get_current_room()
    # use cr variable as the key to print the current room from the Room class dict:
    print(room[cr])
    # print statement to inform player of current room:
    print(f" You are now in the '{playerName.get_current_room()}'")


