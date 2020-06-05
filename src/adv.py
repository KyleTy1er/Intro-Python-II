from room import Room
from player import Player
from item import Item

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


item = {
    'Cup': Item('Cup', 'As nondescript as it is underwhelming ... how fun!'),

    'Broken Teleporter': Item('Broken Teleporter', 'The game mechanics for this totally exist - the item is just broken, sorry bout it...'),

    'Key': Item('Key', 'This key has very little value teehee.'),

    'Hand of Ragnaros': Item('Hand of Ragnaros', 'Thats right - Blizzard stole my idea from this game...'),

    'Cauliflower': Item('Cauliflower', 'is a cruciferous vegetable that is naturally high in fiber and B-vitamins. It provides antioxidants and phytonutrients that can protect against cancer. It also contains fiber to enhance weight loss and digestion, choline that is essential for learning and memory, and many other important nutrients.'),
}

# Main

import getpass

# instantiates a player class based on the getuser method of getpass:
playerName = Player(getpass.getuser().title())
# prints welcome message to player using playerName __str__ method:
print("Welcome{}".format(playerName),"press a directional key ('W,A,S,D') to move or Q to quit...")


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
    print("----------------------------------------------")
    # print statement to inform player of current room:
    print(f" You are now in the '{playerName.get_current_room()}'")
    print("----------------------------------------------")
    print("If you would like to check the room for items press f:")
    items = playerName.check_items()
    if items != None:
        print(items)
    print(f" You have {(tries-10)*-1} moves remaining...")
    print("----------------------------------------------")
    if tries > 7:
        print("You're almost dead...")
    if tries >= 10:
        print("You died... try again.")


