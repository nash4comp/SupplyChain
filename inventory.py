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
        theme = spec["theme"]
        if item_type == "Toy":
            if theme == "Christmas":
                santas_workshop = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"], name=spec["name"],
                                                      description=spec["description"], pid=spec["pid"],
                                                      theme=spec["theme"],
                                                      is_battery_operated=spec["is_battery_operated"],
                                                      min_age=spec["min_age"], dimension=spec["dimension"],
                                                      num_of_rooms=spec["num_of_rooms"])
                self._inventory_toy.append(santas_workshop)
            elif theme == "Halloween":
                rc_spider = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"], name=spec["name"],
                                                description=spec["description"], pid=spec["pid"],
                                                theme=spec["theme"], is_battery_operated=spec["is_battery_operated"],
                                                min_age=spec["min_age"], speed=spec["speed"],
                                                jump_height=spec["jump_height"],
                                                has_glow=spec["has_glow"], spider_type=spec["spider_type"])
                self._inventory_toy.append(rc_spider)
            elif theme == "Easter":
                robot_bunny = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"], name=spec["name"],
                                                  description=spec["description"], pid=spec["pid"],
                                                  theme=spec["theme"], is_battery_operated=spec["is_battery_operated"],
                                                  min_age=spec["min_age"],
                                                  num_of_sound_effects=spec["num_of_sound_effects"],
                                                  color=spec["color"])
                self._inventory_toy.append(robot_bunny)
        elif item_type == "StuffedAnimal":
            if theme == "Christmas":
                dancing_skeleton = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"], name=spec["name"],
                                                       description=spec["description"], pid=spec["pid"],
                                                       theme=spec["theme"], stuffing=spec["stuffing"],
                                                       size=spec["size"], fabric=spec["fabric"],
                                                       has_glow=spec["has_glow"])
                self._inventory_stuffed_animal.append(dancing_skeleton)
            elif theme == "Halloween":
                reindeer = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"], name=spec["name"],
                                               description=spec["description"], pid=spec["pid"],
                                               theme=spec["theme"], stuffing=spec["stuffing"],
                                               size=spec["size"], fabric=spec["fabric"],
                                               has_glow=spec["has_glow"])
                self._inventory_stuffed_animal.append(reindeer)
            elif theme == "Easter":
                easter_bunny = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"], name=spec["name"],
                                                   description=spec["description"], pid=spec["pid"],
                                                   theme=spec["theme"], stuffing=spec["stuffing"],
                                                   size=spec["size"], fabric=spec["fabric"],
                                                   color=spec["color"])
                self._inventory_stuffed_animal.append(easter_bunny)
        elif item_type == "Candy":
            if theme == "Christmas":
                candy_canes = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"], name=spec["name"],
                                                  description=spec["description"], pid=spec["pid"],
                                                  theme=spec["theme"], contains_nuts=spec["contains_nuts"],
                                                  is_lactose_free=spec["is_lactose_free"], strips=spec["strips"])
                self._inventory_candy.append(candy_canes)
            elif theme == "Halloween":
                pumpkin_caramel_toffee = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"], name=spec["name"],
                                                             description=spec["description"], pid=spec["pid"],
                                                             theme=spec["theme"],
                                                             contains_nuts=spec["contains_nuts"],
                                                             is_lactose_free=spec["is_lactose_free"],
                                                             variety=spec["variety"])
                self._inventory_candy.append(pumpkin_caramel_toffee)
            elif theme == "Easter":
                cream_eggs = factory.create_item(item_type=spec["item_type"], quantity=spec["quantity"], name=spec["name"],
                                                 description=spec["description"], pid=spec["pid"],
                                                 theme=spec["theme"], contains_nuts=spec["contains_nuts"],
                                                 is_lactose_free=spec["is_lactose_free"], pack_size=spec["pack_size"])
                self._inventory_candy.append(cream_eggs)

    def inventory_test(self, items):
        self._inventory_toy.append(items[0])
        self._inventory_stuffed_animal.append(items[1])
        self._inventory_candy.append(items[2])

        self._inventory_toy.append(items[3])
        self._inventory_stuffed_animal.append(items[4])
        self._inventory_candy.append(items[5])

        self._inventory_toy.append(items[6])
        self._inventory_stuffed_animal.append(items[7])
        self._inventory_candy.append(items[8])

        self._inventory_toy.append(items[0])

    def inventory_test2(self, factory):
        spec = {"quantity": 20, "name": "Nash's Santas Workshop", "description": "", "pid": "", "theme": "Christmas",
                "item_type": "Toy", "is_battery_operated": False, "min_age": 10, "dimension": "", "num_of_rooms": 0}
        spec2 = {"quantity": 5, "name": "Taylor's DancingSkeleton", "description": "", "pid": "",
                 "theme": "Halloween", "item_type": "StuffedAnimal", "is_battery_operated": False, "min_age": 8,
                 "dimension": "", "num_of_rooms": 1, "stuffing": "Polyester", "size": "Medium", "fabric": "Cotton",
                 "has_glow": False, "num_of_sound_effects": 0, "color": ""}
        spec3 = {"quantity": 3, "name": "Jeff's Candy Canes", "description": "", "pid": "",
                 "theme": "Christmas", "item_type": "Candy", "is_battery_operated": False, "min_age": 8,
                 "dimension": "", "num_of_rooms": 1, "stuffing": "Polyester", "size": "Medium", "fabric": "Cotton",
                 "has_glow": False, "num_of_sound_effects": 0, "color": "", "variety": "Sea Salt", "is_lactose_free": True,
                 "contains_nuts": False, "strips": "Red"}
        spec4 = {
            "quantity": 20,
            "name": "Nash's Halloween RC Spider",
            "description": "",
            "pid": "",
            "theme": "Halloween",
            "item_type": "Toy",
            "is_battery_operated": False,
            "min_age": 8,
            "dimension": "",
            "num_of_rooms": 1,
            "stuffing": "Polyester",
            "size": "Medium",
            "fabric": "Cotton",
            "has_glow": False,
            "num_of_sound_effects": 0,
            "color": "",
            "variety": "Sea Salt",
            "is_lactose_free": True,
            "contains_nuts": False,
            "strips": "Red",
            "jump_height": 10,
            "pack_size": 1,
            "speed": 10,
            "spider_type": "Tarantula"
        }

        spec5 = {
            "quantity": 20,
            "name": "Nash's Robot Bunny",
            "description": "",
            "pid": "",
            "theme": "Easter",
            "item_type": "Toy",
            "is_battery_operated": False,
            "min_age": 8,
            "dimension": "",
            "num_of_rooms": 1,
            "stuffing": "Polyester",
            "size": "Medium",
            "fabric": "Cotton",
            "has_glow": True,
            "num_of_sound_effects": 0,
            "color": "",
            "variety": "Sea Salt",
            "is_lactose_free": True,
            "contains_nuts": False,
            "strips": "Red",
            "jump_height": 10,
            "pack_size": 1,
            "speed": 10,
            "spider_type": "Tarantula"
        }

        spec6 = {
            "quantity": 20,
            "name": "Taylor's Reindeer",
            "description": "",
            "pid": "",
            "theme": "Christmas",
            "item_type": "StuffedAnimal",
            "is_battery_operated": False,
            "min_age": 8,
            "dimension": "",
            "num_of_rooms": 1,
            "stuffing": "Polyester",
            "size": "Medium",
            "fabric": "Cotton",
            "has_glow": True,
            "num_of_sound_effects": 0,
            "color": "",
            "variety": "Sea Salt",
            "is_lactose_free": True,
            "contains_nuts": False,
            "strips": "Red",
            "jump_height": 10,
            "pack_size": 1,
            "speed": 10,
            "spider_type": "Tarantula"
        }

        spec7 = {
	        "quantity": 20,
	        "name": "Taylor's Easter Bunny",
	        "description": "",
	        "pid": "",
	        "theme": "Easter",
	        "item_type": "StuffedAnimal",
	        "is_battery_operated": False,
	        "min_age": 8,
	        "dimension": "",
	        "num_of_rooms": 1,
	        "stuffing": "Polyester",
	        "size": "Medium",
	        "fabric": "Cotton",
	        "has_glow": True,
	        "num_of_sound_effects": 0,
	        "color": "",
	        "variety": "Sea Salt",
	        "is_lactose_free": True,
	        "contains_nuts": False,
	        "strips": "Red",
	        "jump_height": 10,
	        "pack_size": 1,
	        "speed": 10,
	        "spider_type": "Tarantula"
        }

        spec8 = {
	        "quantity": 20,
	        "name": "Jeff's Pumpkin Caramel Toffee",
	        "description": "",
	        "pid": "",
	        "theme": "Halloween",
	        "item_type": "Candy",
	        "is_battery_operated": False,
	        "min_age": 8,
	        "dimension": "",
	        "num_of_rooms": 1,
	        "stuffing": "Polyester",
	        "size": "Medium",
	        "fabric": "Cotton",
	        "has_glow": True,
	        "num_of_sound_effects": 0,
	        "color": "",
	        "variety": "Sea Salt",
	        "is_lactose_free": True,
	        "contains_nuts": False,
	        "strips": "Red",
	        "jump_height": 10,
	        "pack_size": 1,
	        "speed": 10,
	        "spider_type": "Tarantula"
        }

        spec9 = {
	        "quantity": 20,
	        "name": "Jeff's Cream Eggs",
	        "description": "",
	        "pid": "",
	        "theme": "Easter",
	        "item_type": "Candy",
	        "is_battery_operated": False,
	        "min_age": 8,
	        "dimension": "",
	        "num_of_rooms": 1,
	        "stuffing": "Polyester",
	        "size": "Medium",
	        "fabric": "Cotton",
	        "has_glow": True,
	        "num_of_sound_effects": 0,
	        "color": "",
	        "variety": "Sea Salt",
	        "is_lactose_free": True,
	        "contains_nuts": False,
	        "strips": "Red",
	        "jump_height": 10,
	        "pack_size": 1,
	        "speed": 10,
	        "spider_type": "Tarantula"
        }

        self.add_item(spec, factory) # Santa's Workshop
        self.add_item(spec2, factory) # Dancing Skeleton
        self.add_item(spec3, factory) # Candy Canes
        self.add_item(spec4, factory) # RC Spider
        self.add_item(spec5, factory) # Robot Bunny
        self.add_item(spec6, factory) # Reindeer
        self.add_item(spec7, factory) # Easter Bunny
        self.add_item(spec8, factory) # Pumpkin Caramel Toffee
        self.add_item(spec9, factory) # Cream Eggs




    def display_inventory(self):
        print("Inventory List")
        print("<Toy>")
        for item in self._inventory_toy:
            print(item.get_product_type() + ", " + item.get_name() + ", " + str(item.get_quantity()) +
                  ", " + self.check_inventory(item.get_quantity()))
        print("\n<Stuffed Animals>")
        for item in self._inventory_stuffed_animal:
            print(item.get_product_type() + ", " + item.get_name() + ", " + str(item.get_quantity()) +
                  ", " + self.check_inventory(item.get_quantity()))
        print("\n<Candy>")
        for item in self._inventory_candy:
            print(item.get_product_type() + ", " + item.get_name() + ", " + str(item.get_quantity()) +
                  ", " + self.check_inventory(item.get_quantity()))
        print("\n")
