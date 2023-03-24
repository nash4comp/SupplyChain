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

import gift_factory


class Order:
    """
    This class takes care of order. Order has all_information dictionary containing all the information to create an
    item.
    """
    def __init__(self, item_type, order_number, name, product_id, **kwargs):
        """
        Initialize Order
        :param item_type: String, item_type
        :param order_number: int, order number, it is unique
        :param name: String, name of the order,
        :param product_id: String, product_id is unique
        :param kwargs: details of the order
        """
        self._item_type = item_type
        self._orderNum = int(order_number)
        self._name = name
        self._pid = product_id
        self._detail = kwargs
        self._factory = None
        self._all_information = {"quantity": "", "name": "", "item_type": "",
                                 "description": "", "product_id": "", "holiday": "",
                                 "has_batteries": False,
                                 "min_age": 0, "dimension": "", "num_rooms": 0, "stuffing": "", "size": "",
                                 "has_nuts": False, "has_lactose": False, "speed": 0,
                                 "jump_height": 0,
                                 "spider_type": "", "fabric": "", "has_glow": False, "num_sound": 0,
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
        """
        Getter for details dictionary.
        :return: dictionary of details
        """
        return self._detail['attribute']

    def get_quantity(self):
        """
        Getter for quantity.
        :return: int, quantity of the order
        """
        return self.get_attributes()["quantity"]

    def get_item_type(self):
        """
        Getter for item_type
        :return: String, item_type
        """
        return self._item_type

    def get_all_info_dict_for_factory_creation(self):
        """
        Getter for all_infor_dict.
        :return: dictionary, self._all_information
        """
        return self._all_information

    def validate_details(self, holiday):
        """
        Validate all the details required to create an item.
        :param holiday: String, holiday of the item
        :return: dictionary if valid None, if invalid.
        """
        item_type = self.get_item_type()
        if holiday == "Christmas":
            if item_type == "Toy":
                result = gift_factory.Toy.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    santa_detail = gift_factory.SantasWorkshop.santa_detail_validator(self.get_attributes())
                    if santa_detail is not None:
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
                        return self
                    else:
                        return None
            else:
                print("Invalid product type")
        else:
            print("Invalid holiday")

    def __str__(self):
        """
        ToString method.
        :return: short description of the order
        """
        return f"order number: {self.get_order_num()}, " \
               f"item type: {self._item_type}, " \
               f"name: {self._name}, " \
               f"id: {self.get_id()}, " \
               f"quantity : {self.get_quantity()}"
