class Inventory:
    def __init__(self):
        self._inventory_toy = {}
        self._inventory_stuffed_animal = {}
        self._inventory_candy = {}

    def check_item_quantity_helper(self, item, item_key_dict):
        """
        Helps check_item_quantity function to validate the order and its dictionary that has all the required
        information to create the item, especially the quantity
        :param item: Product, item to validate
        :param item_key_dict: dictionary, dictionary that has all the required information to create the item
        """
        pid = item.get_pid()
        if pid in item_key_dict.keys():
            for pid in self._inventory_toy.keys():
                toy_obj = self._inventory_toy[pid]
                if pid == item.get_pid():
                    if toy_obj.get_quantity() < item.get_quantity():
                        toy_obj.add_quantity(100)
                    toy_obj.subtract_quantity(item.get_quantity())
        else:
            item.initial_process(item.get_quantity())
            item_key_dict[item.get_pid()] = item

    def check_item_quantity(self, spec, factory):
        """
        Check the item's quantity and if the item's quantity in the inventory is less than the item to process's quantity
        then add 100 items, then subtract item quantity to process.
        :param spec: dictionary
        :param factory: Factory
        """
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
                self.check_item_quantity_helper(santas_workshop, self.get_item_inventory_dict(item_type))
            elif holiday == "Halloween":
                rc_spider = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                                name=spec["name"],
                                                description=spec["description"], product_id=spec["product_id"],
                                                holiday=spec["holiday"], has_batteries=spec["has_batteries"],
                                                min_age=spec["min_age"], speed=spec["speed"],
                                                jump_height=spec["jump_height"],
                                                has_glow=spec["has_glow"], spider_type=spec["spider_type"])
                self.check_item_quantity_helper(rc_spider, self.get_item_inventory_dict(item_type))
            elif holiday == "Easter":
                robot_bunny = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                                  name=spec["name"],
                                                  description=spec["description"], product_id=spec["product_id"],
                                                  holiday=spec["holiday"], has_batteries=spec["has_batteries"],
                                                  min_age=spec["min_age"],
                                                  num_sound=spec["num_sound"],
                                                  colour=spec["colour"])
                self.check_item_quantity_helper(robot_bunny, self.get_item_inventory_dict(item_type))
        elif item_type == "StuffedAnimal":
            if holiday == "Christmas":
                dancing_skeleton = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                                       name=spec["name"],
                                                       description=spec["description"], product_id=spec["product_id"],
                                                       holiday=spec["holiday"], stuffing=spec["stuffing"],
                                                       size=spec["size"], fabric=spec["fabric"],
                                                       has_glow=spec["has_glow"])
                self.check_item_quantity_helper(dancing_skeleton, self.get_item_inventory_dict(item_type))
            elif holiday == "Halloween":
                reindeer = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                               name=spec["name"],
                                               description=spec["description"], product_id=spec["product_id"],
                                               holiday=spec["holiday"], stuffing=spec["stuffing"],
                                               size=spec["size"], fabric=spec["fabric"],
                                               has_glow=spec["has_glow"])
                self.check_item_quantity_helper(reindeer, self.get_item_inventory_dict(item_type))
            elif holiday == "Easter":
                easter_bunny = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                                   name=spec["name"],
                                                   description=spec["description"], product_id=spec["product_id"],
                                                   holiday=spec["holiday"], stuffing=spec["stuffing"],
                                                   size=spec["size"], fabric=spec["fabric"],
                                                   colour=spec["colour"])
                self.check_item_quantity_helper(easter_bunny, self.get_item_inventory_dict(item_type))
        elif item_type == "Candy":
            if holiday == "Christmas":
                candy_canes = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                                  name=spec["name"],
                                                  description=spec["description"], product_id=spec["product_id"],
                                                  holiday=spec["holiday"], has_nuts=spec["has_nuts"],
                                                  has_lactose=spec["has_lactose"], colour=spec["colour"])
                self.check_item_quantity_helper(candy_canes, self.get_item_inventory_dict(item_type))
            elif holiday == "Halloween":
                pumpkin_caramel_toffee = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                                             name=spec["name"],
                                                             description=spec["description"],
                                                             product_id=spec["product_id"],
                                                             holiday=spec["holiday"],
                                                             has_nuts=spec["has_nuts"],
                                                             has_lactose=spec["has_lactose"],
                                                             variety=spec["variety"])
                self.check_item_quantity_helper(pumpkin_caramel_toffee, self.get_item_inventory_dict(item_type))
            elif holiday == "Easter":
                cream_eggs = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
                                                 name=spec["name"],
                                                 description=spec["description"], product_id=spec["product_id"],
                                                 holiday=spec["holiday"], has_nuts=spec["has_nuts"],
                                                 has_lactose=spec["has_lactose"], pack_size=spec["pack_size"])
                self.check_item_quantity_helper(cream_eggs, self.get_item_inventory_dict(item_type))

    def get_item_inventory_dict(self, item_type):
        """
        Get corresponding dictionary to the item_type
        :param item_type: String
        :return: inventory_toy for toy, inventory_stuffed_animal for stuffedAnimal, inventory_toy for candy
        """
        if item_type == "Toy":
            return self._inventory_toy
        elif item_type == "StuffedAnimal":
            return self._inventory_stuffed_animal
        elif item_type == "Candy":
            return self._inventory_candy
        else:
            print("Item type error")

    def check_inventory(self, quantity):
        if quantity >= 10:
            return "In Stock"
        elif 10 > quantity >= 3:
            return "Low"
        elif 3 > quantity > 0:
            return "Very Low"
        else:
            return "Out of Stock"

    # def add_item(self, spec, factory):
    #     item_type = spec["item_type"]
    #     holiday = spec["holiday"]
    #     if item_type == "Toy":
    #         if holiday == "Christmas":
    #             santas_workshop = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
    #                                                   name=spec["name"],
    #                                                   description=spec["description"], product_id=spec["product_id"],
    #                                                   holiday=spec["holiday"],
    #                                                   has_batteries=spec["has_batteries"],
    #                                                   min_age=spec["min_age"], dimension=spec["dimension"],
    #                                                   num_rooms=spec["num_rooms"])
    #             self._inventory_toy.append(santas_workshop)
    #         elif holiday == "Halloween":
    #             rc_spider = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
    #                                             name=spec["name"],
    #                                             description=spec["description"], product_id=spec["product_id"],
    #                                             holiday=spec["holiday"], has_batteries=spec["has_batteries"],
    #                                             min_age=spec["min_age"], speed=spec["speed"],
    #                                             jump_height=spec["jump_height"],
    #                                             has_glow=spec["has_glow"], spider_type=spec["spider_type"])
    #             self._inventory_toy.append(rc_spider)
    #         elif holiday == "Easter":
    #             robot_bunny = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
    #                                               name=spec["name"],
    #                                               description=spec["description"], product_id=spec["product_id"],
    #                                               holiday=spec["holiday"], has_batteries=spec["has_batteries"],
    #                                               min_age=spec["min_age"],
    #                                               num_sound=spec["num_sound"],
    #                                               colour=spec["colour"])
    #             self._inventory_toy.append(robot_bunny)
    #     elif item_type == "StuffedAnimal":
    #         if holiday == "Christmas":
    #             dancing_skeleton = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
    #                                                    name=spec["name"],
    #                                                    description=spec["description"], product_id=spec["product_id"],
    #                                                    holiday=spec["holiday"], stuffing=spec["stuffing"],
    #                                                    size=spec["size"], fabric=spec["fabric"],
    #                                                    has_glow=spec["has_glow"])
    #             self._inventory_stuffed_animal.append(dancing_skeleton)
    #         elif holiday == "Halloween":
    #             reindeer = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
    #                                            name=spec["name"],
    #                                            description=spec["description"], product_id=spec["product_id"],
    #                                            holiday=spec["holiday"], stuffing=spec["stuffing"],
    #                                            size=spec["size"], fabric=spec["fabric"],
    #                                            has_glow=spec["has_glow"])
    #             self._inventory_stuffed_animal.append(reindeer)
    #         elif holiday == "Easter":
    #             easter_bunny = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
    #                                                name=spec["name"],
    #                                                description=spec["description"], product_id=spec["product_id"],
    #                                                holiday=spec["holiday"], stuffing=spec["stuffing"],
    #                                                size=spec["size"], fabric=spec["fabric"],
    #                                                colour=spec["colour"])
    #             self._inventory_stuffed_animal.append(easter_bunny)
    #     elif item_type == "Candy":
    #         if holiday == "Christmas":
    #             candy_canes = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
    #                                               name=spec["name"],
    #                                               description=spec["description"], product_id=spec["product_id"],
    #                                               holiday=spec["holiday"], has_nuts=spec["has_nuts"],
    #                                               has_lactose=spec["has_lactose"], colour=spec["colour"])
    #             self._inventory_candy.append(candy_canes)
    #         elif holiday == "Halloween":
    #             pumpkin_caramel_toffee = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
    #                                                          name=spec["name"],
    #                                                          description=spec["description"],
    #                                                          product_id=spec["product_id"],
    #                                                          holiday=spec["holiday"],
    #                                                          has_nuts=spec["has_nuts"],
    #                                                          has_lactose=spec["has_lactose"],
    #                                                          variety=spec["variety"])
    #             self._inventory_candy.append(pumpkin_caramel_toffee)
    #         elif holiday == "Easter":
    #             cream_eggs = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"],
    #                                              name=spec["name"],
    #                                              description=spec["description"], product_id=spec["product_id"],
    #                                              holiday=spec["holiday"], has_nuts=spec["has_nuts"],
    #                                              has_lactose=spec["has_lactose"], pack_size=spec["pack_size"])
    #             self._inventory_candy.append(cream_eggs)

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
    #              "has_glow": False, "num_sound": 0, "colour": "", "variety": "Sea Salt", "has_lactose": True,
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
    #         "colour": "",
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
    #         "colour": "",
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
    #         "colour": "",
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
    #         "colour": "",
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
    #         "colour": "",
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
    #         "colour": "",
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

    def display_toys(self):
        """
        Display each toys inside the inventory_toy
        """
        for item in self._inventory_toy.keys():
            print(f"{self._inventory_toy[item].get_product_type()}, {self._inventory_toy[item].get_name()}"
                  f", {self._inventory_toy[item].get_quantity()}"
                  f", {self.check_inventory(self._inventory_toy[item].get_quantity())}")

    def display_stuffed_animals(self):
        """
        Display each toys inside the inventory_stuffed_animals
        """
        for item in self._inventory_stuffed_animal.keys():
            print(f"{self._inventory_stuffed_animal[item].get_product_type()}, "
                  f"{self._inventory_stuffed_animal[item].get_name()}"
                  f", {self._inventory_stuffed_animal[item].get_quantity()}"
                  f", {self.check_inventory(self._inventory_stuffed_animal[item].get_quantity())}")

    def display_candy(self):
        """
        Display each toys inside the inventory_candy
        """
        for item in self._inventory_candy.keys():
            print(f"{self._inventory_candy[item].get_product_type()}, {self._inventory_candy[item].get_name()}"
                  f", {self._inventory_candy[item].get_quantity()}"
                  f", {self.check_inventory(self._inventory_candy[item].get_quantity())}")

    def display_each_item_inventory(self):
        """
        Display all the inventory items with its status
        """
        print("Inventory Status")
        print("<Toy>")
        self.display_toys()
        print("\n")
        print("<Stuffed Animal>")
        self.display_stuffed_animals()
        print("\n")
        print("<Candy>")
        self.display_candy()
        print("\n")
        # for item in self._inventory_toy.keys():
        #     if item == "Toy":
        #         print(f"{self._inventory_toy[item].get_product_type()}, {self._inventory_toy[item].get_name()}"
        #             f", {self._inventory_toy[item].get_quantity()}"
        #             f", {self.check_inventory(self._inventory_toy[item].get_quantity())}")
        #     print("\n<Stuffed Animals>")
        #     if item == "StuffedAnimal":
        #         print(f"{self._inventory_toy[item].get_product_type()}, {self._inventory_toy[item].get_name()}"
        #               f", {self._inventory_toy[item].get_quantity()}"
        #               f", {self.check_inventory(self._inventory_toy[item].get_quantity())}")
        #     print("\n<Candy>")
        #     if item == "Candy":
        #         if item == "Candy":
        #             print(f"{self._inventory_toy[item].get_product_type()}, {self._inventory_toy[item].get_name()}"
        #                   f", {self._inventory_toy[item].get_quantity()}"
        #                   f", {self.check_inventory(self._inventory_toy[item].get_quantity())}")
        # print("\n")
