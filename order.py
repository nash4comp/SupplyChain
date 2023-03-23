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

from enum import Enum
import gift_factory


# factory_mapping = {
#     "Christmas" : ChristmasFactory,
#     EASTER : EasterFactory
# }

class Order:
    def __init__(self, item_type, order_number, name, product_id, **kwargs):
        self._item_type = item_type
        self._orderNum = int(order_number)
        self._name = name
        self._pid = product_id
        self._detail = kwargs  # decode the kwargs
        self._factory = None
        self._all_information = {"quantity": "", "name": "", "item_type": "", #3
                                 "description": "", "product_id": "", "holiday": "",  # 3
                                 "has_batteries": False,  # 1
                                 "min_age": 0, "dimension": "", "num_rooms": 0, "stuffing": "", "size": "",  # 5
                                 "has_nuts": False, "has_lactose": False, "speed": 0,  # 3
                                 "jump_height": 0,  # 1
                                 "spider_type": "", "fabric": "", "has_glow": False, "num_sound": 0,  # 4
                                 "colour": "", "pack_size": "", "variety": ""}  # 3

    def get_id(self):
        """
        Getter for id
        :return: String, id
        """
        return self._pid

    def get_name(self):
        """
        Getter for id
        :return: String, id
        """
        return self._name

    def get_order_num(self):
        """
        Getter for id
        :return: String, id
        """
        return self._orderNum

    def get_attributes(self):
        return self._detail['attribute']

    def get_quantity(self):
        return self.get_attributes()["quantity"]

    def get_item_type(self):
        return self._item_type

    def get_all_info_dict_for_factory_creation(self):
        return self._all_information

    def validate_details(self, holiday):
        item_type = self.get_item_type()
        # self._factory = factory_mapping[holiday]
        if holiday == "Christmas":
            # self._factory = ChristmasFactorytory
            if item_type == "Toy":
                result = gift_factory.Toy.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    santa_detail = gift_factory.SantasWorkshop.santa_detail_validator(self.get_attributes())
                    if santa_detail is not None:
                        # this order is valid
                        self._all_information["quantity"] = result["quantity"]
                        self._all_information["item_type"] = self.get_item_type()
                        self._all_information["name"] = self.get_name()
                        self._all_information["description"] = result["description"]
                        self._all_information["product_id"] = self.get_id()
                        self._all_information["has_batteries"] = result["has_batteries"]
                        self._all_information["min_age"] = result["min_age"]
                        self._all_information["dimension"] = santa_detail["dimension"]
                        self._all_information["num_rooms"] = santa_detail["num_rooms"]
                        self._all_information["holiday"] = holiday




                        santa_workshop = gift_factory.SantasWorkshop(quantity=result["quantity"], name=self.get_name(),
                                                                     description=result["description"],
                                                                     product_id=self.get_id(), holiday=holiday,
                                                                     has_batteries=result["has_batteries"],
                                                                     min_age=result["min_age"],
                                                                     dimension=santa_detail["dimension"],
                                                                     num_rooms=santa_detail["num_rooms"])
                        print("inside validation function: santa house---------------------------")
                        # print(santa_workshop.get_name())
                        # print(santa_workshop.get_description())
                        # print(santa_workshop.get_is_battery_operated())
                        print("validated_santa_house")
                        return self
                    else:
                        return None
            elif item_type == "StuffedAnimal":
                result = gift_factory.StuffedAnimal.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    rein_deer_detail = gift_factory.Reindeer.rein_deer_detail_validator(self.get_attributes())
                    if rein_deer_detail is not None:
                        self._all_information["quantity"] = result["quantity"]
                        self._all_information["name"] = self.get_name()
                        self._all_information["description"] = result["description"]
                        self._all_information["item_type"] = self.get_item_type()
                        self._all_information["product_id"] = self.get_id()
                        self._all_information["holiday"] = holiday
                        self._all_information["stuffing"] = result["stuffing"]
                        self._all_information["size"] = result["size"]



                        rein_deer_workshop = gift_factory.Reindeer(quantity=result["quantity"], name=self.get_name(),
                                                                   description=result["description"],
                                                                   product_id=self.get_id(), holiday=holiday,
                                                                   stuffing=result["stuffing"],
                                                                   size=result["size"])
                        print("inside validation function: rein deer--------------------------------------------")
                        # print(rein_deer_workshop.get_name())
                        # print(rein_deer_workshop.get_description())
                        # print(rein_deer_workshop.get_has_glow())
                        print("validated_rein_deer")
                        return self
                    else:
                        return None
            elif item_type == "Candy":
                result = gift_factory.Candy.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    candy_detail = gift_factory.CandyCanes.candy_cane_detail_validator(self.get_attributes())
                    if candy_detail is not None:
                        self._all_information["quantity"] = result["quantity"]
                        self._all_information["name"] = self.get_name()
                        self._all_information["description"] = result["description"]
                        self._all_information["product_id"] = self.get_id()
                        self._all_information["item_type"] = self.get_item_type()
                        self._all_information["holiday"] = holiday
                        self._all_information["has_nuts"] = result["has_nuts"]
                        self._all_information["has_lactose"] = result["has_lactose"]


                        candy_cane = gift_factory.CandyCanes(quantity=result["quantity"], name=self.get_name(),
                                                             description=result["description"],
                                                             product_id=self.get_id(), holiday=holiday,
                                                             has_nuts=result["has_nuts"],
                                                             has_lactose=result["has_lactose"])
                        print("inside validation function: candy cane--------------------------------------------")
                        # print(candy_cane.get_name())
                        # print(candy_cane.get_description())
                        # print(candy_cane.get_contains_nuts())
                        print("validated_candy_cane")
                        return self
                    else:
                        return None
            else:
                print("Invalid product type")
        elif holiday == "Halloween":
            if item_type == "Toy":
                result = gift_factory.Toy.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    spider_detail = gift_factory.RCSpider.rc_spider_detail_validator(self.get_attributes())
                    if spider_detail is not None:
                        print(spider_detail["speed"])
                        print(spider_detail["spider_type"])
                        self._all_information["quantity"] = result["quantity"]
                        self._all_information["name"] = self.get_name()
                        self._all_information["description"] = result["description"]
                        self._all_information["product_id"] = self.get_id()
                        self._all_information["item_type"] = self.get_item_type()
                        self._all_information["holiday"] = holiday
                        self._all_information["has_batteries"] = result["has_batteries"]
                        self._all_information["min_age"] = result["min_age"]
                        self._all_information["speed"] = spider_detail["speed"]
                        self._all_information["jump_height"] = spider_detail["jump_height"]
                        self._all_information["spider_type"] = spider_detail["spider_type"]





                        spider = gift_factory.RCSpider(quantity=result["quantity"], name=self.get_name(),
                                                       description=result["description"],
                                                       product_id=self.get_id(), holiday=holiday,
                                                       has_batteries=result["has_batteries"],
                                                       min_age=result["min_age"],
                                                       speed=spider_detail["speed"],
                                                       jump_height=spider_detail["jump_height"],
                                                       spider_type=spider_detail["spider_type"])
                        print("inside validation function: RC spider---------------------------")
                        # print(santa_workshop.get_name())
                        # print(santa_workshop.get_description())
                        # print(santa_workshop.get_is_battery_operated())
                        print("validated_RC spider")
                        return self
                    else:
                        return None
            elif item_type == "StuffedAnimal":
                result = gift_factory.StuffedAnimal.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    dancing_skeleton_detail = gift_factory.DancingSkeleton.dancing_skeleton_detail_validator(
                        self.get_attributes())
                    if dancing_skeleton_detail is not None:
                        self._all_information["quantity"] = result["quantity"]
                        self._all_information["name"] = self.get_name()
                        self._all_information["description"] = result["description"]
                        self._all_information["product_id"] = self.get_id()
                        self._all_information["item_type"] = self.get_item_type()
                        self._all_information["holiday"] = holiday
                        self._all_information["stuffing"] = result["stuffing"]
                        self._all_information["size"] = result["size"]
                        self._all_information["fabric"] = dancing_skeleton_detail["fabric"]
                        self._all_information["has_glow"] = dancing_skeleton_detail["has_glow"]



                        dancing_skeleton = gift_factory.DancingSkeleton(
                            quantity=result["quantity"], name=self.get_name(), description=result["description"],
                            product_id=self.get_id(), holiday=holiday, stuffing=result["stuffing"], size=result["size"],
                            fabric=dancing_skeleton_detail["fabric"], has_glow=dancing_skeleton_detail["has_glow"]
                        )
                        print(
                            "inside validation function: dancing skeleton--------------------------------------------")
                        # print(rein_deer_workshop.get_name())
                        # print(dancing_skeleton.get_description())
                        # print(rein_deer_workshop.get_has_glow())
                        print("validated_dancing skeleton")
                        return self
                    else:
                        return None
            elif item_type == "Candy":
                result = gift_factory.Candy.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    pumpkin_candy_detail = gift_factory.PumpkinCaramelToffee.pumpkin_toffee_detail_validator(
                        self.get_attributes())
                    if pumpkin_candy_detail is not None:
                        self._all_information["quantity"] = result["quantity"]
                        self._all_information["name"] = self.get_name()
                        self._all_information["description"] = result["description"]
                        self._all_information["product_id"] = self.get_id()
                        self._all_information["item_type"] = self.get_item_type()
                        self._all_information["holiday"] = holiday
                        self._all_information["has_nuts"] = result["has_nuts"]
                        self._all_information["has_lactose"] = result["has_lactose"]
                        self._all_information["variety"] = pumpkin_candy_detail["variety"]


                        pumpkin_candy = gift_factory.PumpkinCaramelToffee(quantity=result["quantity"],
                                                                          name=self.get_name(),
                                                                          description=result["description"],
                                                                          product_id=self.get_id(), holiday=holiday,
                                                                          has_nuts=result["has_nuts"],
                                                                          has_lactose=result["has_lactose"],
                                                                          variety=pumpkin_candy_detail["variety"])
                        print("inside validation function: pumpkin_candy--------------------------------------------")
                        # print(candy_cane.get_name())
                        # print(candy_cane.get_description())
                        # print(candy_cane.get_contains_nuts())
                        print("validated_pumpkin_candy")
                        return self
                    else:
                        return None
            else:
                print("Invalid product type")
        elif holiday == "Easter":
            if item_type == "Toy":
                result = gift_factory.Toy.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    robot_bunny_detail = gift_factory.RobotBunny.robot_bunny_detail_validator(self.get_attributes())
                    if robot_bunny_detail is not None:
                        self._all_information["quantity"] = result["quantity"]
                        self._all_information["name"] = self.get_name()
                        self._all_information["description"] = result["description"]
                        self._all_information["product_id"] = self.get_id()
                        self._all_information["item_type"] = self.get_item_type()
                        self._all_information["holiday"] = holiday
                        self._all_information["has_batteries"] = result["has_batteries"]
                        self._all_information["min_age"] = result["min_age"]
                        self._all_information["num_sound"] = robot_bunny_detail["num_sound"]
                        self._all_information["colour"] = robot_bunny_detail["colour"]


                        robot_bunny = gift_factory.RobotBunny(quantity=result["quantity"], name=self.get_name(),
                                                              description=result["description"],
                                                              product_id=self.get_id(), holiday=holiday,
                                                              has_batteries=result["has_batteries"],
                                                              min_age=result["min_age"],
                                                              num_sound=robot_bunny_detail["num_sound"],
                                                              colour=robot_bunny_detail["colour"])
                        print("inside validation function: robot_bunny---------------------------")
                        print("validated_robot_bunny")
                        return self
                    else:
                        return None
            elif item_type == "StuffedAnimal":
                result = gift_factory.StuffedAnimal.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    east_bunny_detail = gift_factory.EasterBunny.east_bunny_detail_validator(self.get_attributes())
                    if east_bunny_detail is not None:
                        self._all_information["quantity"] = result["quantity"]
                        self._all_information["name"] = self.get_name()
                        self._all_information["description"] = result["description"]
                        self._all_information["product_id"] = self.get_id()
                        self._all_information["item_type"] = self.get_item_type()
                        self._all_information["holiday"] = holiday
                        self._all_information["stuffing"] = result["stuffing"]
                        self._all_information["size"] = result["size"]
                        self._all_information["fabric"] = east_bunny_detail["fabric"]
                        self._all_information["colour"] = east_bunny_detail["colour"]


                        east_bunny = gift_factory.EasterBunny(quantity=result["quantity"], name=self.get_name(),
                                                              description=result["description"],
                                                              product_id=self.get_id(), holiday=holiday,
                                                              stuffing=result["stuffing"],
                                                              size=result["size"],
                                                              fabric=east_bunny_detail["fabric"],
                                                              colour=east_bunny_detail["colour"])
                        print("inside validation function: east_bunny--------------------------------------------")
                        print("validated_east bunny")
                        return self
                    else:
                        return None
            elif item_type == "Candy":
                result = gift_factory.Candy.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    cream_egg_detail = gift_factory.CreamEggs.cream_egg_detail_validator(self.get_attributes())
                    if cream_egg_detail is not None:
                        self._all_information["quantity"] = result["quantity"]
                        self._all_information["name"] = self.get_name()
                        self._all_information["description"] = result["description"]
                        self._all_information["product_id"] = self.get_id()
                        self._all_information["item_type"] = self.get_item_type()
                        self._all_information["holiday"] = holiday
                        self._all_information["has_nuts"] = result["has_nuts"]
                        self._all_information["has_lactose"] = result["has_lactose"]
                        self._all_information["pack_size"] = cream_egg_detail["pack_size"]

                        cream_egg = gift_factory.CreamEggs(quantity=result["quantity"], name=self.get_name(),
                                                           description=result["description"],
                                                           product_id=self.get_id(), holiday=holiday,
                                                           has_nuts=result["has_nuts"],
                                                           has_lactose=result["has_lactose"],
                                                           pack_size=cream_egg_detail["pack_size"])
                        print("inside validation function: cream egg--------------------------------------------")
                        # print(candy_cane.get_name())
                        # print(candy_cane.get_description())
                        # print(candy_cane.get_contains_nuts())
                        print("validated_cream egg")
                        return self
                    else:
                        return None
            else:
                print("Invalid product type")
        else:
            print("Invalid holiday")

    def __str__(self):
        return f"order number: {self.get_order_num()}, " \
               f"item type: {self._item_type}, " \
               f"name: {self._name}, " \
               f"id: {self.get_id()}, " \
               f"quantity : {self.get_quantity()}"


class Item(Enum):
    TOY = "Toy",
    STUFFED_ANIMAL = "StuffedAnimal",
    CANDY = "Candy"


class Holiday(Enum):
    XMAS = "Christmas",
    EASTER = "Easter",
    HALLOWEEN = "Halloween"
