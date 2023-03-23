"""
The Supply Chain Management System

This program is a simulation of a supply chain management system. It is a
command-line program that allows the user to create a gift factory and
create orders for the factory to fulfill. The program will then process
the orders and print out the results.

# Name1: Nash Baek (nash4comp@gmail.com)
# Student number1: A01243888

# Name2: Taylor Ji (taylor.ji719@gmail.com)
# Student number2: A01304056

UML diagram: https://app.diagrams.net/#G18MWO3bp974lfK4Ceehz2vUfH8YmqEEfE
Sequence diagram: https://app.diagrams.net/#G1gf1FB-nTLsNcJypwlBpQREfXNScSEKYN
"""


class Inventory:
    def __init__(self):
        self._inventory_toy = []
        self._inventory_stuffed_animal = []
        self._inventory_candy = []

    def check_inventory(self, quantity):
        if quantity >= 10:
            return "In Stock"
        elif 10 > quantity >= 3:
            return "Low"
        elif 3 > quantity > 0:
            return "Very Low"
        else:
            return "Out of Stock"

    def add_item(self, spec, factory):
        item_type = spec["item_type"]
        holiday = spec["holiday"]
        if item_type == "Toy":
            if holiday == "Christmas":
                santas_workshop = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                                      name=spec["name"],
                                                      description=spec["description"], product_id=spec["product_id"],
                                                      holiday=spec["holiday"],
                                                      has_batteries=spec["has_batteries"],
                                                      min_age=spec["min_age"], dimension=spec["dimension"],
                                                      num_rooms=spec["num_rooms"])
                self._inventory_toy.append(santas_workshop)
            elif holiday == "Halloween":
                rc_spider = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                                name=spec["name"],
                                                description=spec["description"], product_id=spec["product_id"],
                                                holiday=spec["holiday"], has_batteries=spec["has_batteries"],
                                                min_age=spec["min_age"], speed=spec["speed"],
                                                jump_height=spec["jump_height"],
                                                has_glow=spec["has_glow"], spider_type=spec["spider_type"])
                self._inventory_toy.append(rc_spider)
            elif holiday == "Easter":
                robot_bunny = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                                  name=spec["name"],
                                                  description=spec["description"], product_id=spec["product_id"],
                                                  holiday=spec["holiday"], has_batteries=spec["has_batteries"],
                                                  min_age=spec["min_age"],
                                                  num_sound=spec["num_sound"],
                                                  colour=spec["colour"])
                self._inventory_toy.append(robot_bunny)
        elif item_type == "StuffedAnimal":
            if holiday == "Christmas":
                dancing_skeleton = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                                       name=spec["name"],
                                                       description=spec["description"], product_id=spec["product_id"],
                                                       holiday=spec["holiday"], stuffing=spec["stuffing"],
                                                       size=spec["size"], fabric=spec["fabric"],
                                                       has_glow=spec["has_glow"])
                self._inventory_stuffed_animal.append(dancing_skeleton)
            elif holiday == "Halloween":
                reindeer = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                               name=spec["name"],
                                               description=spec["description"], product_id=spec["product_id"],
                                               holiday=spec["holiday"], stuffing=spec["stuffing"],
                                               size=spec["size"], fabric=spec["fabric"],
                                               has_glow=spec["has_glow"])
                self._inventory_stuffed_animal.append(reindeer)
            elif holiday == "Easter":
                easter_bunny = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                                   name=spec["name"],
                                                   description=spec["description"], product_id=spec["product_id"],
                                                   holiday=spec["holiday"], stuffing=spec["stuffing"],
                                                   size=spec["size"], fabric=spec["fabric"],
                                                   colour=spec["colour"])
                self._inventory_stuffed_animal.append(easter_bunny)
        elif item_type == "Candy":
            if holiday == "Christmas":
                candy_canes = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                                  name=spec["name"],
                                                  description=spec["description"], product_id=spec["product_id"],
                                                  holiday=spec["holiday"], has_nuts=spec["has_nuts"],
                                                  has_lactose=spec["has_lactose"], colour=spec["colour"])
                self._inventory_candy.append(candy_canes)
            elif holiday == "Halloween":
                pumpkin_caramel_toffee = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                                             name=spec["name"],
                                                             description=spec["description"],
                                                             product_id=spec["product_id"],
                                                             holiday=spec["holiday"],
                                                             has_nuts=spec["has_nuts"],
                                                             has_lactose=spec["has_lactose"],
                                                             variety=spec["variety"])
                self._inventory_candy.append(pumpkin_caramel_toffee)
            elif holiday == "Easter":
                cream_eggs = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                                 name=spec["name"],
                                                 description=spec["description"], product_id=spec["product_id"],
                                                 holiday=spec["holiday"], has_nuts=spec["has_nuts"],
                                                 has_lactose=spec["has_lactose"], pack_size=spec["pack_size"])
                self._inventory_candy.append(cream_eggs)

    # def inventory_test(self, items):
    #     self._inventory_toy.append(items[0])
    #     self._inventory_stuffed_animal.append(items[1])
    #     self._inventory_candy.append(items[2])
    #
    #     self._inventory_toy.append(items[3])
    #     self._inventory_stuffed_animal.append(items[4])
    #     self._inventory_candy.append(items[5])
    #
    #     self._inventory_toy.append(items[6])
    #     self._inventory_stuffed_animal.append(items[7])
    #     self._inventory_candy.append(items[8])
    #
    #     self._inventory_toy.append(items[0])
    #
    # def inventory_test2(self, factory):
    #     spec = {"quantity": 20, "name": "Nash's Santas Workshop", "description": "", "product_id": "",
    #             "holiday": "Christmas",
    #             "item_type": "Toy", "has_batteries": False, "min_age": 10, "dimension": "", "num_rooms": 0}
    #     spec2 = {"quantity": 5, "name": "Taylor's DancingSkeleton", "description": "", "product_id": "",
    #              "holiday": "Halloween", "item_type": "StuffedAnimal", "has_batteries": False, "min_age": 8,
    #              "dimension": "", "num_rooms": 1, "stuffing": "Polyester", "size": "Medium", "fabric": "Cotton",
    #              "has_glow": False, "num_sound": 0, "colour": ""}
    #     spec3 = {"quantity": 3, "name": "Jeff's Candy Canes", "description": "", "product_id": "",
    #              "holiday": "Christmas", "item_type": "Candy", "has_batteries": False, "min_age": 8,
    #              "dimension": "", "num_rooms": 1, "stuffing": "Polyester", "size": "Medium", "fabric": "Cotton",
    #              "has_glow": False, "num_sound": 0, "variety": "Sea Salt", "has_lactose": True,
    #              "has_nuts": False, "colour": "Red"}
    #     spec4 = {
    #         "quantity": 20,
    #         "name": "Nash's Halloween RC Spider",
    #         "description": "",
    #         "product_id": "",
    #         "holiday": "Halloween",
    #         "item_type": "Toy",
    #         "has_batteries": False,
    #         "min_age": 8,
    #         "dimension": "",
    #         "num_rooms": 1,
    #         "stuffing": "Polyester",
    #         "size": "Medium",
    #         "fabric": "Cotton",
    #         "has_glow": False,
    #         "num_sound": 0,
    #         "variety": "Sea Salt",
    #         "has_lactose": True,
    #         "has_nuts": False,
    #         "colour": "Red",
    #         "jump_height": 10,
    #         "pack_size": 1,
    #         "speed": 10,
    #         "spider_type": "Tarantula"
    #     }
    #
    #     spec5 = {
    #         "quantity": 20,
    #         "name": "Nash's Robot Bunny",
    #         "description": "",
    #         "product_id": "",
    #         "holiday": "Easter",
    #         "item_type": "Toy",
    #         "has_batteries": False,
    #         "min_age": 8,
    #         "dimension": "",
    #         "num_rooms": 1,
    #         "stuffing": "Polyester",
    #         "size": "Medium",
    #         "fabric": "Cotton",
    #         "has_glow": True,
    #         "num_sound": 0,
    #         "variety": "Sea Salt",
    #         "has_lactose": True,
    #         "has_nuts": False,
    #         "colour": "Red",
    #         "jump_height": 10,
    #         "pack_size": 1,
    #         "speed": 10,
    #         "spider_type": "Tarantula"
    #     }
    #
    #     spec6 = {
    #         "quantity": 20,
    #         "name": "Taylor's Reindeer",
    #         "description": "",
    #         "product_id": "",
    #         "holiday": "Christmas",
    #         "item_type": "StuffedAnimal",
    #         "has_batteries": False,
    #         "min_age": 8,
    #         "dimension": "",
    #         "num_rooms": 1,
    #         "stuffing": "Polyester",
    #         "size": "Medium",
    #         "fabric": "Cotton",
    #         "has_glow": True,
    #         "num_sound": 0,
    #         "variety": "Sea Salt",
    #         "has_lactose": True,
    #         "has_nuts": False,
    #         "colour": "Red",
    #         "jump_height": 10,
    #         "pack_size": 1,
    #         "speed": 10,
    #         "spider_type": "Tarantula"
    #     }
    #
    #     spec7 = {
    #         "quantity": 20,
    #         "name": "Taylor's Easter Bunny",
    #         "description": "",
    #         "product_id": "",
    #         "holiday": "Easter",
    #         "item_type": "StuffedAnimal",
    #         "has_batteries": False,
    #         "min_age": 8,
    #         "dimension": "",
    #         "num_rooms": 1,
    #         "stuffing": "Polyester",
    #         "size": "Medium",
    #         "fabric": "Cotton",
    #         "has_glow": True,
    #         "num_sound": 0,
    #         "variety": "Sea Salt",
    #         "has_lactose": True,
    #         "has_nuts": False,
    #         "colour": "Red",
    #         "jump_height": 10,
    #         "pack_size": 1,
    #         "speed": 10,
    #         "spider_type": "Tarantula"
    #     }
    #
    #     spec8 = {
    #         "quantity": 20,
    #         "name": "Jeff's Pumpkin Caramel Toffee",
    #         "description": "",
    #         "product_id": "",
    #         "holiday": "Halloween",
    #         "item_type": "Candy",
    #         "has_batteries": False,
    #         "min_age": 8,
    #         "dimension": "",
    #         "num_rooms": 1,
    #         "stuffing": "Polyester",
    #         "size": "Medium",
    #         "fabric": "Cotton",
    #         "has_glow": True,
    #         "num_sound": 0,
    #         "variety": "Sea Salt",
    #         "has_lactose": True,
    #         "has_nuts": False,
    #         "colour": "Red",
    #         "jump_height": 10,
    #         "pack_size": 1,
    #         "speed": 10,
    #         "spider_type": "Tarantula"
    #     }
    #
    #     spec9 = {
    #         "quantity": 20,
    #         "name": "Jeff's Cream Eggs",
    #         "description": "",
    #         "product_id": "",
    #         "holiday": "Easter",
    #         "item_type": "Candy",
    #         "has_batteries": False,
    #         "min_age": 8,
    #         "dimension": "",
    #         "num_rooms": 1,
    #         "stuffing": "Polyester",
    #         "size": "Medium",
    #         "fabric": "Cotton",
    #         "has_glow": True,
    #         "num_sound": 0,
    #         "variety": "Sea Salt",
    #         "has_lactose": True,
    #         "has_nuts": False,
    #         "colour": "Red",
    #         "jump_height": 10,
    #         "pack_size": 1,
    #         "speed": 10,
    #         "spider_type": "Tarantula"
    #     }
    #
    #     self.add_item(spec, factory)  # Santa's Workshop
    #     self.add_item(spec2, factory)  # Dancing Skeleton
    #     self.add_item(spec3, factory)  # Candy Canes
    #     self.add_item(spec4, factory)  # RC Spider
    #     self.add_item(spec5, factory)  # Robot Bunny
    #     self.add_item(spec6, factory)  # Reindeer
    #     self.add_item(spec7, factory)  # Easter Bunny
    #     self.add_item(spec8, factory)  # Pumpkin Caramel Toffee
    #     self.add_item(spec9, factory)  # Cream Eggs

    def display_inventory(self):
        print("Inventory List")
        print("<Toy>")
        for item in self._inventory_toy:
            # print(item.get_product_type() + ", " + item.get_name() + ", " + str(item.get_quantity()) +
            #       ", " + self.check_inventory(item.get_quantity()))
            print("[" + self.check_inventory(item.get_quantity()) + "] " + str(item))
        print("\n<Stuffed Animals>")
        for item in self._inventory_stuffed_animal:
            # print(item.get_product_type() + ", " + item.get_name() + ", " + str(item.get_quantity()) +
            #       ", " + self.check_inventory(item.get_quantity()))
            print("[" + self.check_inventory(item.get_quantity()) + "] " + str(item))
        print("\n<Candy>")
        for item in self._inventory_candy:
            # print(item.get_product_type() + ", " + item.get_name() + ", " + str(item.get_quantity()) +
            #       ", " + self.check_inventory(item.get_quantity()))
            print("[" + self.check_inventory(item.get_quantity()) + "] " + str(item))
        print("\n")
