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

import abc
from abc import ABC
from enum import Enum


class Products(Enum):
    class Toy(Enum):
        SantasWorkshop = 1
        RCSpider = 2
        RobotBunny = 3

    class StuffedAnimal(Enum):
        DancingSkeleton = 1
        Reindeer = 2
        EasterBunny = 3

    class Candy(Enum):
        PumpkinCaramelToffee = 1
        CandyCanes = 2
        CreamEggs = 3


class Holiday(Enum):
    Christmas = 1
    Halloween = 2
    Easter = 3


class SpiderType(Enum):
    Tarantula = 1
    WolfSpider = 2


class Colour(Enum):
    Orange = 1
    Blue = 2
    Pink = 3
    White = 4
    Grey = 5


class Stuffing(Enum):
    Polyester_Fibrefill = 1
    Wool = 2


class Size(Enum):
    S = 1
    M = 2
    L = 3


class Fabric(Enum):
    Linen = 1
    Cotton = 2
    Acrylic = 3


class PumpkinCaramelVariety(Enum):
    Sea_Salt = 1
    Regular = 2


class CandyCanesStrips(Enum):
    Red = 1
    Green = 2


class GiftFactory:
    @staticmethod
    def create_item(**kwargs):
        item_type = kwargs["item_type"]
        del kwargs["item_type"]
        if kwargs["holiday"] == Holiday.Christmas.name:
            if item_type == "Toy":
                return SantasWorkshop(**kwargs)
            elif item_type == "StuffedAnimal":
                return Reindeer(**kwargs)
            elif item_type == "Candy":
                return CandyCanes(**kwargs)
        elif kwargs["holiday"] == Holiday.Halloween.name:
            if item_type == "Toy":
                return RCSpider(**kwargs)
            elif item_type == "StuffedAnimal":
                return DancingSkeleton(**kwargs)
            elif item_type == "Candy":
                return PumpkinCaramelToffee(**kwargs)
        elif kwargs["holiday"] == Holiday.Easter.name:
            if item_type == "Toy":
                return RobotBunny(**kwargs)
            elif item_type == "StuffedAnimal":
                return EasterBunny(**kwargs)
            elif item_type == "Candy":
                return CreamEggs(**kwargs)


class Product(ABC):
    def __init__(self, item_type=None, quantity=0, name='No name', description='', product_id='', holiday=None):
        self._item_type = item_type
        self._quantity = quantity
        self._name = name
        self._description = description
        self._product_id = product_id
        self._holiday = holiday

    def __str__(self):
        return "Product"

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = quantity

    # def set_name(self, name):
    # 	self._name = name
    def initial_process(self, initial_order_count):
        initial_count = 100
        processed_count = initial_count - initial_order_count
        self.set_quantity(processed_count)

    def add_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = self.get_quantity() + quantity

    def subtract_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = self.get_quantity() - quantity

    def set_name(self, name):
        self._name = name

    # def set_description(self, description):
    # 	self._description = description

    # def set_product_id(self, product_id):
    # 	self._product_id = product_id

    # def set_holiday(self, holiday):
    # 	if holiday == Holiday.Christmas:
    # 		self._holiday = Holiday.Christmas
    # 	elif holiday == Holiday.Halloween:
    # 		self._holiday = Holiday.Halloween
    # 	elif holiday == Holiday.Easter:
    # 		self._holiday = Holiday.Easter
    # 	else:
    # 		self._holiday = None

    def get_quantity(self):
        return self._quantity

    def get_name(self):
        return self._name

    # def get_description(self):
    # 	return self._description

    def get_product_id(self):
        return self._product_id

    # def get_holiday(self):
    # 	return self._holiday

    @abc.abstractmethod
    def get_item_type(self):
        pass


class Toy(Product):
    @staticmethod
    def validate_attribute(attribute_dict):
        """
        Validate toy's common attributes.
        :param attribute_dict: dictionary that has all the information required to create an item.
        """
        valid_attributes_toy = {"quantity": 0, "description": "", "has_batteries": False, "min_age": 0}
        valid_attribute_count = 0
        for attribute in valid_attributes_toy.keys():
            if attribute in attribute_dict.keys():
                if attribute == "quantity" and type(attribute_dict[attribute]) == int:
                    valid_attributes_toy["quantity"] = attribute_dict[attribute]
                    valid_attribute_count += 1
                if attribute == "description" and attribute_dict[attribute] is not None:
                    valid_attributes_toy["description"] = attribute_dict[attribute]
                    valid_attribute_count += 1
                if attribute == "has_batteries":
                    if attribute_dict["has_batteries"] == "N":
                        valid_attributes_toy["has_batteries"] = False
                        valid_attribute_count += 1
                    elif attribute_dict["has_batteries"] == "Y":
                        valid_attributes_toy["has_batteries"] = True
                        valid_attribute_count += 1
                    else:
                        print("Invalid battery input")
                    # valid_attributes_toy["has_batteries"] = attribute_dict[attribute]
                if attribute == "min_age" and type(attribute_dict[attribute]) == float:
                    int_age = int(attribute_dict[attribute])
                    valid_attributes_toy["min_age"] = int_age
                    valid_attribute_count += 1
        if valid_attribute_count != len(valid_attributes_toy):
            print("Invalid order")
        else:
            return valid_attributes_toy

    def __init__(self, item_type='TOY', quantity=0, name='No name', description='', product_id='', holiday=None,
                 has_batteries=False,
                 min_age=0):
        super().__init__(item_type, quantity, name, description, product_id, holiday)
        self._item_type = item_type
        self._has_batteries = has_batteries
        self._min_age = min_age

    # def set_has_batteries(self, has_batteries):
    # 	self._has_batteries = has_batteries

    # def set_min_age(self, min_age):
    # 	if min_age < 0:
    # 		raise ValueError("Min age cannot be negative")
    # 	self._min_age = min_age

    # def get_has_batteries(self):
    # 	return self._has_batteries

    # def get_min_age(self):
    # 	return self._min_age

    # def get_item_type(self):
    # 	return "Toy"

    def get_item_type(self):
        return self._item_type

    def __str__(self):
        return "Toy"


class SantasWorkshop(Toy):

    @staticmethod
    def santa_detail_validator(att_dict):
        """
        Validate Santa's attributes.
        :param att_dict: dictionary that has all the information required to create Santa Workshop.
        """
        # valid_attributes_count = 6
        # if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
        #     # print("extra column santa")
        #     return None
        valid_santa_attributes = {"dimension": "", "num_rooms": 0}
        for key_att_dict in att_dict.keys():
            if key_att_dict == "dimensions":
                valid_santa_attributes["dimension"] = att_dict[key_att_dict]
            if key_att_dict == "num_rooms" and type(att_dict[key_att_dict]) != str:
                int_room_num = int(att_dict[key_att_dict])
                valid_santa_attributes["num_rooms"] = int_room_num
        if valid_santa_attributes["dimension"] == "" \
                or valid_santa_attributes["num_rooms"] == 0:
            return None
        else:
            return valid_santa_attributes

    def __init__(self, item_type='TOY', quantity=0, name='No name', description='', product_id='', holiday=None,
                 has_batteries=False,
                 min_age='', dimension="", num_rooms=0):
        super().__init__(item_type, quantity, name, description, product_id, holiday, has_batteries, min_age)
        self._dimension = dimension
        # self._width = width
        # self._height = height
        self._num_rooms = num_rooms

    # def set_width(self, width):
    #     if width < 0:
    #         self._width = 0
    #     self._width = width
    #
    # def set_height(self, height):
    #     if height < 0:
    #         self._height = 0
    #     self._height = height

    # def set_num_rooms(self, num_rooms):
    # 	if num_rooms < 0:
    # 		self._num_rooms = 0
    # 	self._num_rooms = num_rooms

    def get_item_type(self):
        return self._item_type

    # def get_width(self):
    #     return self._width
    #
    # def get_height(self):
    #     return self._height

    # def get_num_rooms(self):
    # 	return self._num_rooms

    # def get_dimension(self):
    # 	return self._dimension

    def __str__(self):
        ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
              str(self.get_quantity()) + ", Name: " + self.get_name()
        return ret


class RCSpider(Toy):

    @staticmethod
    def rc_spider_detail_validator(att_dict):
        """
        Validate RC Spider's attributes.
        :param att_dict: dictionary that has all the information required to create RC Spider.
        """

        valid_attribute_count = 0
        # if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
        #     # print("extra column rc spider")
        #     return None
        valid_spider_attributes = {"speed": 0, "jump_height": 0, "has_glow": "", "spider_type": ""}
        for key_att_dict in att_dict.keys():
            if key_att_dict == "speed" and att_dict[key_att_dict] != str:
                int_speed = int(att_dict[key_att_dict])
                valid_spider_attributes["speed"] = int_speed
                valid_attribute_count += 1
            if key_att_dict == "jump_height" and type(att_dict[key_att_dict]) != str:
                int_jump = int(att_dict[key_att_dict])
                valid_spider_attributes["jump_height"] = int_jump
                valid_attribute_count += 1
            if key_att_dict == "has_glow":
                if att_dict["has_glow"] == "N":
                    valid_spider_attributes["has_glow"] = False
                    valid_attribute_count += 1
                elif att_dict["has_glow"] == "Y":
                    valid_spider_attributes["has_glow"] = True
                    valid_attribute_count += 1
                else:
                    print("Invalid glow input")
            if key_att_dict == "spider_type":
                if att_dict["spider_type"] == "Tarantula":
                    valid_spider_attributes["spider_type"] = "Tarantula"
                    valid_attribute_count += 1
                elif att_dict["spider_type"] == "Wolf Spider":
                    valid_spider_attributes["spider_type"] = "Wolf Spider"
                    valid_attribute_count += 1
                else:
                    print("Invalid spider type input")
        if valid_spider_attributes["speed"] == 0 \
                or valid_spider_attributes["jump_height"] == 0 \
                or valid_spider_attributes["has_glow"] == "" \
                or valid_spider_attributes["spider_type"] == "":
            return None
        else:
            return valid_spider_attributes

    def __init__(self, item_type='TOY', quantity=0, name='No name', description='', product_id='', holiday=None,
                 has_batteries=False,
                 min_age=0, speed=0, jump_height=0, has_glow=False, spider_type=None):
        super().__init__(item_type, quantity, name, description, product_id, holiday, has_batteries, min_age)
        self._speed = speed
        self._jump_height = jump_height
        self._has_glow = has_glow
        self._spider_type = spider_type

    # def set_speed(self, speed):
    # 	if speed < 0:
    # 		self._speed = 0
    # 	self._speed = speed

    # def set_jump_height(self, jump_height):
    # 	if jump_height < 0:
    # 		self._jump_height = 0
    # 	self._jump_height = jump_height

    # def set_has_glow(self, has_glow):
    # 	self._has_glow = has_glow

    # def set_spider_type(self, spider_type):
    # 	if spider_type == SpiderType.Tarantula:
    # 		self._spider_type = SpiderType.Tarantula
    # 	elif spider_type == SpiderType.WolfSpider:
    # 		self._spider_type = SpiderType.WolfSpider
    # 	else:
    # 		self._spider_type = None

    def get_item_type(self):
        return self._item_type

    # def get_speed(self):
    # 	return self._speed
    #
    # def get_jump_height(self):
    # 	return self._jump_height
    #
    # def get_has_glow(self):
    # 	return self._has_glow
    #
    # def get_spider_type(self):
    # 	return self._spider_type

    def __str__(self):
        ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
              str(self.get_quantity()) + ", Name: " + self.get_name()
        return ret


class RobotBunny(Toy):

    @staticmethod
    def robot_bunny_detail_validator(att_dict):
        """
        Validate Robot bunny's attributes.
        :param att_dict: dictionary that has all the information required to create Robot bunny.
        """
        # valid_attributes_count = 6
        valid_attribute_count = 0
        # if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
        #     # print("extra column robot bunny")
        #     return None
        valid_robot_bunny_details = {"num_sound": 0, "colour": ""}
        for key_att_dict in att_dict.keys():
            value_from_dict = att_dict[key_att_dict]
            if key_att_dict == "num_sound" and type(att_dict[key_att_dict]) != str:
                int_num_sound = int(att_dict[key_att_dict])
                valid_robot_bunny_details["num_sound"] = int_num_sound
                valid_attribute_count += 1
            if key_att_dict == "colour":
                # Orange, Blue, Pink
                if key_att_dict == "colour":
                    if value_from_dict == "Orange":
                        valid_robot_bunny_details["colour"] = "Orange"
                    if value_from_dict == "Blue":
                        valid_robot_bunny_details["colour"] = "Blue"
                    if value_from_dict == "Pink":
                        valid_robot_bunny_details["colour"] = "Pink"
                valid_attribute_count += 1
        if valid_robot_bunny_details["num_sound"] == 0 \
                or valid_robot_bunny_details["colour"] == "":
            return None
        else:
            return valid_robot_bunny_details

    def __init__(self, item_type='TOY', quantity=0, name='No name', description='', product_id='', holiday=None,
                 has_batteries=False,
                 min_age=0, num_sound=0, colour=None):
        super().__init__(item_type, quantity, name, description, product_id, holiday, has_batteries, min_age)
        self._num_of_sound_effects = num_sound
        self._color = colour

    # def set_num_of_sound_effects(self, num_sound):
    # 	if num_sound < 0:
    # 		self._num_of_sound_effects = 0
    # 	self._num_of_sound_effects = num_sound

    # def set_color(self, colour):
    # 	if colour == Colour.Orange:
    # 		self._color = Colour.Orange
    # 	elif colour == Colour.Pink:
    # 		self._color = Colour.Pink
    # 	elif colour == Colour.Blue:
    # 		self._color = Colour.Blue
    # 	else:
    # 		self._color = None

    def get_item_type(self):
        return self._item_type

    # def get_num_of_sound_effects(self):
    # 	return self._num_of_sound_effects

    # def get_color(self):
    # 	return self._color

    def __str__(self):
        ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
              str(self.get_quantity()) + ", Name: " + self.get_name()
        return ret


class StuffedAnimal(Product):
    @staticmethod
    def validate_attribute(attribute_dict):
        """
        Validate Robot bunny's attributes.
        :param attribute_dict: dictionary that has all the information required to create Stuffed Animal.
        """
        valid_attributes_stuffed_animal = {"quantity": 0, "description": "", "stuffing": "", "size": ""}
        valid_attribute_count = 0
        for attribute in valid_attributes_stuffed_animal.keys():
            if attribute in attribute_dict.keys():
                if attribute == "quantity" and type(attribute_dict[attribute]) == int:
                    valid_attributes_stuffed_animal["quantity"] = attribute_dict[attribute]
                    valid_attribute_count += 1
                if attribute == "description" and attribute_dict[attribute] is not None:
                    valid_attributes_stuffed_animal["description"] = attribute_dict[attribute]
                    valid_attribute_count += 1
                if attribute == "stuffing":
                    if attribute_dict["stuffing"] == "Polyester Fibrefill":
                        valid_attributes_stuffed_animal["stuffing"] = "Polyester Fibrefill"
                        valid_attribute_count += 1
                    elif attribute_dict["stuffing"] == "Wool":
                        valid_attributes_stuffed_animal["stuffing"] = "Wool"
                        valid_attribute_count += 1
                    else:
                        print("Invalid stuffing input")
                if attribute == "size":
                    if attribute_dict["size"] == "S":
                        valid_attributes_stuffed_animal["size"] = "S"
                        valid_attribute_count += 1
                    elif attribute_dict["size"] == "M":
                        valid_attributes_stuffed_animal["size"] = "M"
                        valid_attribute_count += 1
                    elif attribute_dict["size"] == "L":
                        valid_attributes_stuffed_animal["size"] = "L"
                        valid_attribute_count += 1
                    else:
                        print("Invalid size input")
        # if valid_attribute_count != len(valid_attributes_stuffed_animal):
        #     print("Invalid order stuffed animal")
        # else:
        return valid_attributes_stuffed_animal

    def __init__(self, item_type='StuffedAnimal', quantity=0, name='No name', description='', product_id='',
                 holiday=None, stuffing=None, size=None,
                 fabric=None):
        super().__init__(item_type, quantity, name, description, product_id, holiday)
        self._stuffing = stuffing
        self._size = size
        self._fabric = fabric

    # def set_stuffing(self, stuffing):
    # 	if stuffing == Stuffing.Polyester_Fibrefill:
    # 		self._stuffing = Stuffing.Polyester_Fibrefill
    # 	elif stuffing == Stuffing.Wool:
    # 		self._stuffing = Stuffing.Wool
    # 	else:
    # 		self._stuffing = None
    #
    # def set_size(self, size):
    # 	if size == Size.S:
    # 		self._size = Size.S
    # 	elif size == Size.M:
    # 		self._size = Size.M
    # 	elif size == Size.L:
    # 		self._size = Size.L
    # 	else:
    # 		self._size = None
    #
    # def set_fabric(self, fabric):
    # 	if fabric == Fabric.Linen:
    # 		self._fabric = Fabric.Linen
    # 	elif fabric == Fabric.Cotton:
    # 		self._fabric = Fabric.Cotton
    # 	elif fabric == Fabric.Acrylic:
    # 		self._fabric = Fabric.Acrylic
    # 	else:
    # 		self._fabric = None
    #
    # def get_item_type(self):
    # 	return "StuffedAnimal"

    def get_item_type(self):
        return self._item_type

    def __str__(self):
        ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
              str(self.get_quantity()) + ", Name: " + self.get_name()
        return ret


class DancingSkeleton(StuffedAnimal):
    @staticmethod
    def dancing_skeleton_detail_validator(att_dict):
        """
        Validate Dancing Skeleton's attributes.
        :param attribute_dict: dictionary that has all the information required to create Dancing Skeleton.
        """
        # valid_attributes_count = 6
        # if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
        #     # print("extra column dancing monkey")
        #     return None
        valid_dancing_skeleton_attributes = {"fabric": "", "has_glow": ""}
        for key_att_dict in att_dict.keys():
            value_from_dict = att_dict[key_att_dict]
            if key_att_dict == "fabric":
                if value_from_dict == "Linen":
                    valid_dancing_skeleton_attributes["fabric"] = "Linen"
                if value_from_dict == "Cotton":
                    valid_dancing_skeleton_attributes["fabric"] = "Cotton"
                if value_from_dict == "Acrylic":
                    valid_dancing_skeleton_attributes["fabric"] = "Acrylic"
            if key_att_dict == "has_glow":
                if value_from_dict == "N":
                    valid_dancing_skeleton_attributes["has_glow"] = False
                elif value_from_dict == "Y":
                    valid_dancing_skeleton_attributes["has_glow"] = True
                else:
                    print("Invalid fabric")
        if valid_dancing_skeleton_attributes["fabric"] == "" \
                or valid_dancing_skeleton_attributes["has_glow"] == "":
            return None
        else:
            return valid_dancing_skeleton_attributes

    def __init__(self, item_type='StuffedAnimal', quantity=0, name='No name', description='', product_id='',
                 holiday=None, stuffing=None, size=None,
                 fabric=None, has_glow=False):
        super().__init__(item_type, quantity, name, description, product_id, holiday, stuffing, size, fabric)
        self._has_glow = has_glow

    # def set_has_glow(self, has_glow):
    # 	self._has_glow = has_glow
    #
    # def get_item_type(self):
    # 	return "DancingSkeleton"
    #
    # def get_has_glow(self):
    # 	return self._has_glow

    def __str__(self):
        ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
              str(self.get_quantity()) + ", Name: " + self.get_name()
        return ret


class Reindeer(StuffedAnimal):

    @staticmethod
    def rein_deer_detail_validator(att_dict):
        """
        Validate Reindeer's attributes.
        :param att_dict: dictionary that has all the information required to create  Reindeer.
        """
        # valid_attributes_count = 6
        # if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
        #     # print("extra column reindeer")
        #     return None
        valid_reindeer_attributes = {"fabric": "", "has_glow": ""}
        for key_att_dict in att_dict.keys():
            value_from_dict = att_dict[key_att_dict]
            if key_att_dict == "fabric":
                if value_from_dict == "Linen":
                    valid_reindeer_attributes["fabric"] = "Linen"
                if value_from_dict == "Cotton":
                    valid_reindeer_attributes["fabric"] = "Cotton"
                if value_from_dict == "Acrylic":
                    valid_reindeer_attributes["fabric"] = "Acrylic"
            if key_att_dict == "has_glow":
                if value_from_dict == "N":
                    valid_reindeer_attributes["has_glow"] = False
                elif value_from_dict == "Y":
                    valid_reindeer_attributes["has_glow"] = True
                else:
                    print("Invalid glow")
        if valid_reindeer_attributes["fabric"] == "" \
                or valid_reindeer_attributes["has_glow"] == "":
            return None
        else:
            return valid_reindeer_attributes

    def __init__(self, item_type='StuffedAnimal', quantity=0, name='No name', description='', product_id='',
                 holiday=None, stuffing=None, size=None,
                 fabric=None, has_glow=False):
        super().__init__(item_type, quantity, name, description, product_id, holiday, stuffing, size, fabric)
        self._has_glow = has_glow

    # def set_has_glow(self, has_glow):
    # 	self._has_glow = has_glow
    #
    # def get_item_type(self):
    # 	return "Reindeer"
    #
    # def get_has_glow(self):
    # 	return self._has_glow

    def __str__(self):
        ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
              str(self.get_quantity()) + ", Name: " + self.get_name()
        return ret


class EasterBunny(StuffedAnimal):
    @staticmethod
    def east_bunny_detail_validator(att_dict):
        """
        Validate Easter Bunny's attributes.
        :param att_dict: dictionary that has all the information required to create Easter Bunny.
        """
        # valid_attributes_count = 6
        # if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
        #     # print("extra column easter bunny")
        #     return None
        valid_reindeer_attributes = {"fabric": "", "colour": ""}
        for key_att_dict in att_dict.keys():
            value_from_dict = att_dict[key_att_dict]
            if key_att_dict == "fabric":
                if value_from_dict == "Linen":
                    valid_reindeer_attributes["fabric"] = "Linen"
                if value_from_dict == "Cotton":
                    valid_reindeer_attributes["fabric"] = "Cotton"
                if value_from_dict == "Acrylic":
                    valid_reindeer_attributes["fabric"] = "Acrylic"
            if key_att_dict == "colour":
                if value_from_dict == "Orange":
                    valid_reindeer_attributes["colour"] = "Orange"
                if value_from_dict == "Blue":
                    valid_reindeer_attributes["colour"] = "Blue"
                if value_from_dict == "Pink":
                    valid_reindeer_attributes["colour"] = "Pink"
                if value_from_dict == "White":
                    valid_reindeer_attributes["colour"] = "White"
                if value_from_dict == "Grey":
                    valid_reindeer_attributes["colour"] = "Grey"
        if valid_reindeer_attributes["fabric"] == "" \
                or valid_reindeer_attributes["colour"] == "":
            return None
        else:
            return valid_reindeer_attributes

    # num of sound effect??
    def __init__(self, item_type='StuffedAnimal', quantity=0, name='No name', description='', product_id='',
                 holiday=None, stuffing=None, size=None,
                 fabric=None, colour=None):
        super().__init__(item_type, quantity, name, description, product_id, holiday, stuffing, size, fabric)
        # self._num_of_sound_effects = num_sound  #
        self._color = colour

    # def set_num_of_sound_effects(self, num_sound):
    # 	if num_sound < 0:
    # 		self._num_of_sound_effects = 0
    # 	self._num_of_sound_effects = num_sound

    # def set_color(self, colour):
    # 	if colour == Colour.White:
    # 		self._color = Colour.White
    # 	elif colour == Colour.Grey:
    # 		self._color = Colour.Grey
    # 	elif colour == Colour.Pink:
    # 		self._color = Colour.Pink
    # 	elif colour == Colour.Blue:
    # 		self._color = Colour.Blue
    # 	else:
    # 		self._color = None

    # def get_item_type(self):
    # 	return "EasterBunny"

    # def get_num_of_sound_effects(self):
    # 	return self._num_of_sound_effects

    # def get_color(self):
    # 	return self._color

    def __str__(self):
        ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
              str(self.get_quantity()) + ", Name: " + self.get_name()
        return ret


class Candy(Product):

    @staticmethod
    def validate_attribute(attribute_dict):
        """
        Validate Candy's common attributes.
        :param attribute_dict: dictionary that has all the information required to create Candy.
        """
        valid_attributes_candy = {"quantity": 0, "description": "", "has_nuts": "", "has_lactose": ""}
        valid_attribute_count = 0
        for attribute in valid_attributes_candy.keys():
            if attribute in attribute_dict.keys():
                if attribute == "quantity" and type(attribute_dict[attribute]) == int:
                    valid_attributes_candy["quantity"] = attribute_dict[attribute]
                    valid_attribute_count += 1
                if attribute == "description" and attribute_dict[attribute] is not None:
                    valid_attributes_candy["description"] = attribute_dict[attribute]
                    valid_attribute_count += 1
                if attribute == "has_nuts":
                    if attribute_dict["has_nuts"] == "N":
                        valid_attributes_candy["has_nuts"] = False
                        valid_attribute_count += 1
                    elif attribute_dict["has_nuts"] == "Y":
                        valid_attributes_candy["has_nuts"] = True
                        valid_attribute_count += 1
                    else:
                        print("Invalid has_nuts input")
                if attribute == "has_lactose":
                    if attribute_dict["has_lactose"] == "N":
                        valid_attributes_candy["has_lactose"] = False
                        valid_attribute_count += 1
                    elif attribute_dict["has_lactose"] == "Y":
                        valid_attributes_candy["has_lactose"] = True
                        valid_attribute_count += 1
                    else:
                        print("Invalid has_lactose input")
        # if valid_attribute_count != len(valid_attributes_candy):
        #     print("Invalid order")
        return valid_attributes_candy

    def __init__(self, item_type='Candy', quantity=0, name='No name', description='', product_id='', holiday=None,
                 has_nuts=False,
                 has_lactose=False):
        super().__init__(item_type, quantity, name, description, product_id, holiday)
        self._contains_nuts = has_nuts
        self._is_lactose_free = has_lactose

    # def set_contains_nuts(self, has_nuts):
    # 	self._contains_nuts = has_nuts
    #
    # def set_is_lactose_free(self, has_lactose):
    # 	self._is_lactose_free = has_lactose
    #
    # def get_item_type(self):
    # 	return "Candy"
    #
    # def get_contains_nuts(self):
    # 	return self._contains_nuts
    #
    # def get_is_lactose_free(self):
    # 	return self._is_lactose_free

    def get_item_type(self):
        return self._item_type

    def __str__(self):
        ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
              str(self.get_quantity()) + ", Name: " + self.get_name()
        return ret


class PumpkinCaramelToffee(Candy):
    @staticmethod
    def pumpkin_toffee_detail_validator(att_dict):
        """
        Validate Pumpkin Caramel Toffee's attributes.
        :param att_dict: dictionary that has all the information required to create  Pumpkin Caramel Toffee.
        """
        # valid_attributes_count = 5
        # if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
        #     # print("extra column")
        #     return None
        valid_halloween_candy_attributes = {"variety": ""}
        for key_att_dict in att_dict.keys():
            value_from_dict = att_dict[key_att_dict]
            if key_att_dict == "variety":
                if value_from_dict == "Sea Salt":
                    valid_halloween_candy_attributes["variety"] = value_from_dict
                if value_from_dict == "Regular":
                    valid_halloween_candy_attributes["variety"] = value_from_dict
        if valid_halloween_candy_attributes["variety"] == "":
            return None
        else:
            return valid_halloween_candy_attributes

    def __init__(self, item_type='Candy', quantity=0, name='No name', description='', product_id='', holiday=None,
                 has_nuts=False,
                 has_lactose=False, variety=''):
        super().__init__(item_type, quantity, name, description, product_id, holiday, has_nuts, has_lactose)
        self._variety = variety

    # def set_variety(self, variety):
    # 	if variety == PumpkinCaramelVariety.Sea_Salt:
    # 		self._variety = PumpkinCaramelVariety.Sea_Salt
    # 	elif variety == PumpkinCaramelVariety.Regular:
    # 		self._variety = PumpkinCaramelVariety.Regular
    # 	else:
    # 		self._variety = None
    #
    # def get_item_type(self):
    # 	return "PumpkinCaramelToffee"
    #
    # def get_variety(self):
    # 	return self._variety

    def __str__(self):
        ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
              str(self.get_quantity()) + ", Name: " + self.get_name()
        return ret


class CandyCanes(Candy):

    @staticmethod
    def candy_cane_detail_validator(att_dict):
        """
        Validate Pumpkin Candy Cane's attributes.
        :param att_dict: dictionary that has all the information required to create Candy Cane.
        """
        # valid_attributes_count = 5
        # if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
        #     # print("extra column")
        #     return None
        valid_candy_cane_attributes = {"colour": ""}
        for key_att_dict in att_dict.keys():
            value_from_dict = att_dict[key_att_dict]
            if key_att_dict == "colour":
                if value_from_dict == "Red":
                    valid_candy_cane_attributes["colour"] = value_from_dict
                if value_from_dict == "Green":
                    valid_candy_cane_attributes["colour"] = value_from_dict
        if valid_candy_cane_attributes["colour"] == "":
            return None
        else:
            return valid_candy_cane_attributes

    def __init__(self, item_type='Candy', quantity=0, name='No name', description='', product_id='', holiday=None,
                 has_nuts=False,
                 has_lactose=False, colour=None):
        super().__init__(item_type, quantity, name, description, product_id, holiday, has_nuts, has_lactose)
        self._strips = colour

    # def set_strips(self, colour):
    # 	if colour == CandyCanesStrips.Red:
    # 		self._strips = CandyCanesStrips.Red
    # 	elif colour == CandyCanesStrips.Green:
    # 		self._strips = CandyCanesStrips.Green
    # 	else:
    # 		self._strips = None
    #
    # def get_item_type(self):
    # 	return "CandyCanes"
    #
    # def get_strips(self):
    # 	return self._strips

    def __str__(self):
        ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
              str(self.get_quantity()) + ", Name: " + self.get_name()
        return ret


class CreamEggs(Candy):

    @staticmethod
    def cream_egg_detail_validator(att_dict):
        """
        Validate Pumpkin Cream Egg's attributes.
        :param att_dict: dictionary that has all the information required to create Cream Egg.
        """
        # valid_attributes_count = 5
        # if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
        #     # print("extra column")
        #     return None
        valid_cream_egg_attributes = {"pack_size": ""}
        for key_att_dict in att_dict.keys():
            value_from_dict = att_dict[key_att_dict]
            if key_att_dict == "pack_size" and type(value_from_dict) != str:
                int_pack_size = int(value_from_dict)
                valid_cream_egg_attributes["pack_size"] = int_pack_size
        if valid_cream_egg_attributes["pack_size"] == "":
            return None
        else:
            return valid_cream_egg_attributes

    def __init__(self, item_type='Candy', quantity=0, name='No name', description='', product_id='', holiday=None,
                 has_nuts=False,
                 has_lactose=False, pack_size=0):
        super().__init__(item_type, quantity, name, description, product_id, holiday, has_nuts, has_lactose)
        self._pack_size = pack_size

    # def set_pack_size(self, pack_size):
    # 	if pack_size < 0:
    # 		self._pack_size = 0
    # 	self._pack_size = pack_size
    #
    # def get_item_type(self):
    # 	return "CreamEggs"
    #
    # def get_pack_size(self):
    # 	return self._pack_size

    def __str__(self):
        ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
              str(self.get_quantity()) + ", Name: " + self.get_name()
        return ret
