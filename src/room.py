# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room(Item):
    def __init__(self, name, description):
        # super().__init__(item_name=None, item_desc=None)
        self.current_room = playerName.get_current_room()
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    def potential_items(self, playerName, current_room=None, item):
        self.current_room = current_room
        if self.current_room == 'outside':
            return item

    # def get_room_items(self):
    #     return self.item_name
