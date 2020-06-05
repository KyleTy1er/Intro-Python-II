# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player(Item):

    def __init__(self, playerName, current_room='outside'):
        # super().__init__(item_name, item_desc)
        self.playerName = playerName
        self.current_room = current_room
        # self.item_name = []
        # self.item_desc = []

    def __str__(self):
        return f" {self.playerName}, your current location is the: '{self.current_room}'"


    # def get_item(self, item_name, item_desc):
    #     self.item_name = []
    #     self.item_desc = []
    #     inventory = item_name.append(item_desc)
    #     return inventory
    #
    # def check_inventory(self):
    #     print(inventory)

    def change_rooms(self, entry, current_room='outside'):
        self.entry = entry
        options = ['w', 'a', 's', 'd', 'q']
        if entry not in options:
            print("Not a valid direction...Choose W, A, S, D, or Q to quit.")
        if entry == 'q':
            sys.exit()

# Outside -------------------------------------------------
        if self.current_room == 'outside' and entry == 'w':
            self.current_room = 'foyer'
            return current_room
        if self.current_room == 'outside' and entry == 'a':
            self.current_room = 'outside'
            print( "Not an option, please try again")
        if self.current_room == 'outside' and entry == 'd':
            self.current_room = 'outside'
            return "Not an option, please try again"
        if self.current_room == 'outside' and entry == 's':
            self.current_room = 'outside'
            return "Not an option, please try again"
# Foyer --------------------------------------------------
        if self.current_room == 'foyer' and entry == 'w':
            self.current_room = 'overlook'
            return current_room
        if self.current_room == 'foyer' and entry == 'a':
            self.current_room = 'foyer'
            return "Not an option, please try again"
        if self.current_room == 'foyer' and entry == 'd':
            self.current_room = 'narrow'
            return current_room
        if self.current_room == 'foyer' and entry == 's':
            self.current_room = 'outside'
            return f"You've returned to the {self.current_room}"
# Narrow -------------------------------------------------
        if self.current_room == 'narrow' and entry == 'w':
            self.current_room = 'treasure'
            return current_room
        if self.current_room == 'narrow' and entry == 'a':
            self.current_room = 'foyer'
            return current_room
        if self.current_room == 'narrow' and entry == 'd':
            self.current_room = 'narrow'
            return "Not an option, please try again"
        if self.current_room == 'narrow' and entry == 's':
            self.current_room = 'narrow'
            return "Not an option, please try again"
# Treasure ------------------------------------------------
        if self.current_room == 'treasure' and entry == 'w':
            self.current_room = 'treasure'
            return "Not an option, please try again"
        if self.current_room == 'treasure' and entry == 'a':
            self.current_room = 'treasure'
            return "Not an option, please try again"
        if self.current_room == 'treasure' and entry == 'd':
            self.current_room = 'treasure'
            return "Not an option, please try again"
        if self.current_room == 'treasure' and entry == 's':
            self.current_room = 'narrow'
            return f"You've returned to the {self.current_room}"
# Overlook ------------------------------------------------
        if self.current_room == 'overlook' and entry == 'w':
            self.current_room = 'overlook'
            return "Not an option, please try again"
        if self.current_room == 'overlook' and entry == 'a':
            self.current_room = 'overlook'
            return "Not an option, please try again"
        if self.current_room == 'overlook' and entry == 'd':
            self.current_room = 'overlook'
            return "Not an option, please try again"
        if self.current_room == 'overlook' and entry == 's':
            self.current_room = 'foyer'
            return f"You've returned to the {self.current_room}"

    def get_current_room(self):
        return self.current_room





