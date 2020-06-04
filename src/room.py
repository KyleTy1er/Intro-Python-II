# Implement a class to hold room information. This should have name and
# description attributes.



# class Rooms:

#     def __init__(self, rooms, descriptions):
#         self.descriptions = descriptions
#         self.rooms = self.init_rooms(rooms)
#         print (self.descriptions)
#     def init_rooms(self, rooms):
#         # instances = []
#         # for i, d in enumerate(departments):
#         #     instances.append(Department(i + 1, d))
#         # return instances
#         return [Room(i + 1, d) for i, d in enumerate(rooms)]
#
#     # def __str__(self):
#     #     return f" Room name: {(self.name)}, Description: '{(self.description)}'"
#
#     def __str__(self):
#         # this will print out the name of the Store
#         # as well as any departments that the Store has
#         output = f"{self.rooms}\n"
#         for d in self.rooms:
#             output += "  desc: " + str(d.get_description()) + ", name: " + str(d.get_name()) + "\n"
#         return output


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def __str__(self):
        return f"{self.name}: {self.description}"

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name
