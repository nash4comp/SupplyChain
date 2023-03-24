class Inventory:
    """
    Inventory class that contains all the items in the store.
    """
    def __init__(self):
        """
        Initialize Inventory.
        """
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
        pid = item.get_product_id()
        if pid in item_key_dict.keys():
            for pid in self._inventory_toy.keys():
                toy_obj = self._inventory_toy[pid]
                if pid == item.get_product_id():
                    if toy_obj.get_quantity() < item.get_quantity():
                        toy_obj.add_quantity(100)
                    toy_obj.subtract_quantity(item.get_quantity())
        else:
            item.initial_process(item.get_quantity())
            item_key_dict[item.get_product_id()] = item

    def check_item_quantity(self, spec, factory):
        """
        Check the item's quantity and if the item's quantity in the inventory is
        less than the item to process's quantity
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

    @staticmethod
    def check_inventory(quantity):
        """
        Check the quantity of the item and return the corresponding string
        :param quantity: the quantity of the item
        :return: the corresponding string
        """
        if quantity >= 10:
            return "In Stock"
        elif 10 > quantity >= 3:
            return "Low"
        elif 3 > quantity > 0:
            return "Very Low"
        else:
            return "Out of Stock"

    def display_toys(self):
        """
        Display each toys inside the inventory_toy
        """
        for item in self._inventory_toy.keys():
            print(f"[{self.check_inventory(self._inventory_toy[item].get_quantity())}] {self._inventory_toy[item]}")

    def display_stuffed_animals(self):
        """
        Display each toys inside the inventory_stuffed_animals
        """
        for item in self._inventory_stuffed_animal.keys():
            print(f"[{self.check_inventory(self._inventory_stuffed_animal[item].get_quantity())}] "
                  f"{self._inventory_stuffed_animal[item]}")

    def display_candy(self):
        """
        Display each toys inside the inventory_candy
        """
        for item in self._inventory_candy.keys():
            print(f"[{self.check_inventory(self._inventory_candy[item].get_quantity())}] {self._inventory_candy[item]}")

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
