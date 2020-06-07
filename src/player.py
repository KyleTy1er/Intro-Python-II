# Write a class to hold player information, e.g. what room they are in
# currently.
import sys

class Player():

    def __init__(self, playerName, current_room='outside'):
        self.playerName = playerName
        self.current_room = current_room
        self.inventory = []


    def __str__(self):
        return f" {self.playerName}, your current location is the: '{self.current_room}'"

    def get_item(self):
        if self.current_room == 'outside':
            self.item = 'Cup'
            if self.item not in self.inventory:
                self.inventory.append(self.item)
                return self.inventory
            if self.item in self.inventory:
                print("This room has already been looted!")
        if self.current_room == 'narrow':
            self.item = 'Broken Teleporter'
            if self.item not in self.inventory:
                self.inventory.append(self.item)
                return self.inventory
        if self.current_room == 'foyer':
            self.item = 'Key'
            if self.item not in self.inventory:
                self.inventory.append(self.item)
                return self.inventory
        if self.current_room == 'treasure':
            self.item = 'Hand of Ragnaros'
            if self.item not in self.inventory:
                self.inventory.append(self.item)
                return self.inventory
        if self.current_room == 'overlook':
            self.item = 'Cauliflower'
            if self.item not in self.inventory:
                self.inventory.append(self.item)
                return self.inventory


    def check_inventory(self):
        return self.inventory


    def check_items(self):
      if self.current_room == 'outside':
          self.item = 'Cup'
          if self.item not in self.inventory:
              print("---------------------------------------------------")
              print("ITEM: You notice something highly creative...a cup.")
              print("---------------------------------------------------")
              self.item = 'Cup'
              return self.item
          else:
              print("This room has already been looted!")


      if self.current_room == 'foyer':
          self.item = 'Key'
          if self.item not in self.inventory:
              print("----------------------------------------------")
              print ("ITEM: HEY THERES A KEY OVER THERE :O")
              print("----------------------------------------------")
              self.item = 'Key'
              return self.item
          else:
              print("This room has already been looted!")


      if self.current_room == 'narrow':
          self.item = 'Broken Teleporter'
          if self.item not in self.inventory:
              print("----------------------------------------------")
              print ("ITEM: idk what that is... better pick it up.")
              print("----------------------------------------------")
              self.item = 'Broken Teleporter'
          else:
            print("This room has already been looted!")


      if self.current_room == 'overlook':
          self.item = 'Cauliflower'
          if self.item not in self.inventory:
             print("----------------------------------------------")
             print("ITEM: something delicious is like... right over there")
             print("----------------------------------------------")
             self.item = 'Cauliflower'
          else:
              print("This room has already been looted")


      if self.current_room == 'treasure':
          self.item = 'Hand of Ragnaros'
          if self.item not in self.inventory:
              print("----------------------------------------------")
              print("ITEM: if you dont recognize this item then ur better off honestly.")
              print("----------------------------------------------")
              self.item = 'Hand of Ragnaros'
          else:
              print("This room has already been looted")

    def change_rooms(self, entry, current_room='outside'):
        self.entry = entry
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





