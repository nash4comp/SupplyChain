"""
# TODO: Add title and description

# Name1: Nash Baek (nash4comp@gmail.com)
# Student number1: A01243888

# Name2: Taylor Ji (taylor.ji719@gmail.com)
# Student number2: A01304056

UML diagram: https://app.diagrams.net/#G18MWO3bp974lfK4Ceehz2vUfH8YmqEEfE
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


class Theme(Enum):
    Christmas = 1
    Halloween = 2
    Easter = 3


class SpiderType(Enum):
    Tarantula = 1
    WolfSpider = 2


class Color(Enum):
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


class PumpkinCaramelFlavor(Enum):
    Sea_Salt = 1
    Regular = 2


class CandyCanesStrips(Enum):
    Red = 1
    Green = 2


class GiftFactory:
    def create_item(self, **kwargs):
        item_type = kwargs["item_type"]
        del kwargs["item_type"]
        if kwargs["theme"] == Theme.Christmas.name:
            if item_type == "Toys":
                return SantasWorkshop(**kwargs)
            elif item_type == "StuffedAnimal":
                return Reindeer(**kwargs)
            elif item_type == "Candy":
                return CandyCanes(**kwargs)
        elif kwargs["theme"] == Theme.Halloween.name:
            if item_type == "Toys":
                return RCSpider(**kwargs)
            elif item_type == "StuffedAnimal":
                return DancingSkeleton(**kwargs)
            elif item_type == "Candy":
                return PumpkinCaramelToffee(**kwargs)
        elif kwargs["theme"] == Theme.Easter.name:
            if item_type == "Toys":
                return RobotBunny(**kwargs)
            elif item_type == "StuffedAnimal":
                return EasterBunny(**kwargs)
            elif item_type == "Candy":
                return CreamEggs(**kwargs)


class Product(ABC):
    def __init__(self, quantity=0, name='No name', description='', pid='', theme=None):
        self._quantity = quantity
        self._name = name
        self._description = description
        self._pid = pid
        self._theme = theme

    def __str__(self):
        return "Product"

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self._quantity = quantity

    def set_name(self, name):
        self._name = name

    def set_description(self, description):
        self._description = description

    def set_pid(self, pid):
        self._pid = pid

    def set_theme(self, theme):
        if theme == Theme.Christmas:
            self._theme = Theme.Christmas
        elif theme == Theme.Halloween:
            self._theme = Theme.Halloween
        elif theme == Theme.Easter:
            self._theme = Theme.Easter
        else:
            self._theme = None

    def get_quantity(self):
        return self._quantity

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_pid(self):
        return self._pid

    def get_theme(self):
        return self._theme

    @abc.abstractmethod
    def get_product_type(self):
        pass


class Toy(Product):
    @staticmethod
    def validate_attribute(attribute_dict):
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

    def __init__(self, quantity=0, name='No name', description='', pid='', theme=None, is_battery_operated=False,
                 min_age=0):
        super().__init__(quantity, name, description, pid, theme)
        self._is_battery_operated = is_battery_operated
        self._min_age = min_age

    def set_is_battery_operated(self, is_battery_operated):
        self._is_battery_operated = is_battery_operated

    def set_min_age(self, min_age):
        if min_age < 0:
            raise ValueError("Min age cannot be negative")
        self._min_age = min_age

    def get_is_battery_operated(self):
        return self._is_battery_operated

    def get_min_age(self):
        return self._min_age

    def get_product_type(self):
        return "Toy"

    def __str__(self):
        return "Toy"


class SantasWorkshop(Toy):

    @staticmethod
    def santa_detail_validator(att_dict):
        valid_attributes_count = 6
        if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
            print("extra column")
            return None
        valid_santa_attributes = {"dimension": "", "num_of_rooms": 0}
        for key_att_dict in att_dict.keys():
            if key_att_dict == "dimensions":
                valid_santa_attributes["dimension"] = att_dict[key_att_dict]
            if key_att_dict == "num_rooms" and type(att_dict[key_att_dict]) != str:
                int_room_num = int(att_dict[key_att_dict])
                valid_santa_attributes["num_of_rooms"] = int_room_num
        if valid_santa_attributes["dimension"] == "" \
                or valid_santa_attributes["num_of_rooms"] == 0:
            return None
        else:
            return valid_santa_attributes

    def __init__(self, quantity=0, name='No name', description='', pid='', theme=None, is_battery_operated=False,
                 min_age='', dimension="", num_of_rooms=0):
        super().__init__(quantity, name, description, pid, theme, is_battery_operated, min_age)
        self._dimension = dimension
        # self._width = width
        # self._height = height
        self._num_of_rooms = num_of_rooms

    # def set_width(self, width):
    #     if width < 0:
    #         self._width = 0
    #     self._width = width
    #
    # def set_height(self, height):
    #     if height < 0:
    #         self._height = 0
    #     self._height = height

    def set_num_of_rooms(self, num_of_rooms):
        if num_of_rooms < 0:
            self._num_of_rooms = 0
        self._num_of_rooms = num_of_rooms

    def get_product_type(self):
        return "SantasWorkshop"

    # def get_width(self):
    #     return self._width
    #
    # def get_height(self):
    #     return self._height

    def get_num_of_rooms(self):
        return self._num_of_rooms

    def __str__(self):
        return "SantasWorkshop"


class RCSpider(Toy):

    @staticmethod
    def rc_spider_detail_validator(att_dict):
        # desc, quan, has_batteries, min_age
        # speed, jump_height, has_glow, spider_type
        valid_attributes_count = 8
        valid_attribute_count = 0
        if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
            print("extra column")
            return None
        valid_spider_attributes = {"speed": 0, "jump_height": 0, "has_glow": "", "spider_type": ""}
        for key_att_dict in att_dict.keys():
            if key_att_dict == "speed":
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
                or valid_spider_attributes["has_glow"] == ""\
                or valid_spider_attributes["spider_type"] == "":
            return None
        else:
            return valid_spider_attributes

    def __init__(self, quantity=0, name='No name', description='', pid='', theme=None, is_battery_operated=False,
                 min_age=0, speed=0.0, jump_height=0.0, is_glowing=False, spider_type=None):
        super().__init__(quantity, name, description, pid, theme, is_battery_operated, min_age)
        self._speed = speed
        self._jump_height = jump_height
        self._is_glowing = is_glowing
        self._spider_type = spider_type

    def set_speed(self, speed):
        if speed < 0:
            self._speed = 0
        self._speed = speed

    def set_jump_height(self, jump_height):
        if jump_height < 0:
            self._jump_height = 0
        self._jump_height = jump_height

    def set_is_glowing(self, is_glowing):
        self._is_glowing = is_glowing

    def set_spider_type(self, spider_type):
        if spider_type == SpiderType.Tarantula:
            self._spider_type = SpiderType.Tarantula
        elif spider_type == SpiderType.WolfSpider:
            self._spider_type = SpiderType.WolfSpider
        else:
            self._spider_type = None

    def get_product_type(self):
        return "RCSpider"

    def get_speed(self):
        return self._speed

    def get_jump_height(self):
        return self._jump_height

    def get_is_glowing(self):
        return self._is_glowing

    def get_spider_type(self):
        return self._spider_type

    def __str__(self):
        return "RCSpider"


class RobotBunny(Toy):

    @staticmethod
    def robot_bunny_detail_validator(att_dict):
        # desc, quan, has_batteries, min_age
        # num_sound, colour,
        valid_attributes_count = 6
        valid_attribute_count = 0
        if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
            print("extra column")
            return None
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

    def __init__(self, quantity=0, name='No name', description='', pid='', theme=None, is_battery_operated=False,
                 min_age=0, num_of_sound_effects=0, color=None):
        super().__init__(quantity, name, description, pid, theme, is_battery_operated, min_age)
        self._num_of_sound_effects = num_of_sound_effects
        self._color = color

    def set_num_of_sound_effects(self, num_of_sound_effects):
        if num_of_sound_effects < 0:
            self._num_of_sound_effects = 0
        self._num_of_sound_effects = num_of_sound_effects

    def set_color(self, color):
        if color == Color.Orange:
            self._color = Color.Orange
        elif color == Color.Pink:
            self._color = Color.Pink
        elif color == Color.Blue:
            self._color = Color.Blue
        else:
            self._color = None

    def get_product_type(self):
        return "RobotBunny"

    def get_num_of_sound_effects(self):
        return self._num_of_sound_effects

    def get_color(self):
        return self._color

    def __str__(self):
        return "RobotBunny"


class StuffedAnimal(Product):
    @staticmethod
    def validate_attribute(attribute_dict):
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
        if valid_attribute_count != len(valid_attributes_stuffed_animal):
            print("Invalid order")
        else:
            return valid_attributes_stuffed_animal

    def __init__(self, quantity=0, name='No name', description='', pid='', theme=None, stuffing=None, size=None,
                 fabric=None):
        super().__init__(quantity, name, description, pid, theme)
        self._stuffing = stuffing
        self._size = size
        self._fabric = fabric

    def set_stuffing(self, stuffing):
        if stuffing == Stuffing.Polyester_Fibrefill:
            self._stuffing = Stuffing.Polyester_Fibrefill
        elif stuffing == Stuffing.Wool:
            self._stuffing = Stuffing.Wool
        else:
            self._stuffing = None

    def set_size(self, size):
        if size == Size.S:
            self._size = Size.S
        elif size == Size.M:
            self._size = Size.M
        elif size == Size.L:
            self._size = Size.L
        else:
            self._size = None

    def set_fabric(self, fabric):
        if fabric == Fabric.Linen:
            self._fabric = Fabric.Linen
        elif fabric == Fabric.Cotton:
            self._fabric = Fabric.Cotton
        elif fabric == Fabric.Acrylic:
            self._fabric = Fabric.Acrylic
        else:
            self._fabric = None

    def get_product_type(self):
        return "StuffedAnimal"

    def __str__(self):
        return "StuffedAnimal"


class DancingSkeleton(StuffedAnimal):
    @staticmethod
    def dancing_skeleton_detail_validator(att_dict):
        # quantity": 0, "description": "", "stuffing": "", "size": ""
        valid_attributes_count = 6
        if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
            print("extra column")
            return None
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

    def __init__(self, quantity=0, name='No name', description='', pid='', theme=None, stuffing=None, size=None,
                 fabric=None, is_glowing=False):
        super().__init__(quantity, name, description, pid, theme, stuffing, size, fabric)
        self._is_glowing = is_glowing

    def set_is_glowing(self, is_glowing):
        self._is_glowing = is_glowing

    def get_product_type(self):
        return "DancingSkeleton"

    def get_is_glowing(self):
        return self._is_glowing

    def __str__(self):
        return "DancingSkeleton"


class Reindeer(StuffedAnimal):

    @staticmethod
    def rein_deer_detail_validator(att_dict):
        valid_attributes_count = 6
        if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
            print("extra column")
            return None
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

    def __init__(self, quantity=0, name='No name', description='', pid='', theme=None, stuffing=None, size=None,
                 fabric=None, has_glow=False):
        super().__init__(quantity, name, description, pid, theme, stuffing, size, fabric)
        self._has_glow = has_glow

    def set_has_glow(self, has_glow):
        self._has_glow = has_glow

    def get_product_type(self):
        return "Reindeer"

    def get_has_glow(self):
        return self._has_glow

    def __str__(self):
        return "Reindeer"


class EasterBunny(StuffedAnimal):
    @staticmethod
    def east_bunny_detail_validator(att_dict):
        # quantity": 0, "description": "", "stuffing": "", "size": ""
        # Orange = 1
        # Blue = 2
        # Pink = 3
        # White = 4
        # Grey = 5
        valid_attributes_count = 6
        if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
            print("extra column")
            return None
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
    def __init__(self, quantity=0, name='No name', description='', pid='', theme=None, stuffing=None, size=None,
                 fabric=None, color=None):
        super().__init__(quantity, name, description, pid, theme, stuffing, size, fabric)
        # self._num_of_sound_effects = num_of_sound_effects  #
        self._color = color

    def set_num_of_sound_effects(self, num_of_sound_effects):
        if num_of_sound_effects < 0:
            self._num_of_sound_effects = 0
        self._num_of_sound_effects = num_of_sound_effects

    def set_color(self, color):
        if color == Color.White:
            self._color = Color.White
        elif color == Color.Grey:
            self._color = Color.Grey
        elif color == Color.Pink:
            self._color = Color.Pink
        elif color == Color.Blue:
            self._color = Color.Blue
        else:
            self._color = None

    def get_product_type(self):
        return "EasterBunny"

    def get_num_of_sound_effects(self):
        return self._num_of_sound_effects

    def get_color(self):
        return self._color

    def __str__(self):
        return "EasterBunny"


class Candy(Product):

    @staticmethod
    def validate_attribute(attribute_dict):
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
        if valid_attribute_count != len(valid_attributes_candy):
            print("Invalid order")
        else:
            return valid_attributes_candy

    def __init__(self, quantity=0, name='No name', description='', pid='', theme=None, contains_nuts=False,
                 is_lactose_free=False):
        super().__init__(quantity, name, description, pid, theme)
        self._contains_nuts = contains_nuts
        self._is_lactose_free = is_lactose_free

    def set_contains_nuts(self, contains_nuts):
        self._contains_nuts = contains_nuts

    def set_is_lactose_free(self, is_lactose_free):
        self._is_lactose_free = is_lactose_free

    def get_product_type(self):
        return "Candy"

    def get_contains_nuts(self):
        return self._contains_nuts

    def get_is_lactose_free(self):
        return self._is_lactose_free

    def __str__(self):
        return "Candy"


class PumpkinCaramelToffee(Candy):
    @staticmethod
    def pumpkin_toffee_detail_validator(att_dict):
        # quantity": 0, "description": "", "has_nuts": "", "has_lactose": ""
        valid_attributes_count = 5
        if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
            print("extra column")
            return None
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

    def __init__(self, quantity=0, name='No name', description='', pid='', theme=None, contains_nuts=False,
                 is_lactose_free=False, flavor=None):
        super().__init__(quantity, name, description, pid, theme, contains_nuts, is_lactose_free)
        self._flavor = flavor

    def set_flavor(self, flavor):
        if flavor == PumpkinCaramelFlavor.Sea_Salt:
            self._flavor = PumpkinCaramelFlavor.Sea_Salt
        elif flavor == PumpkinCaramelFlavor.Regular:
            self._flavor = PumpkinCaramelFlavor.Regular
        else:
            self._flavor = None

    def get_product_type(self):
        return "PumpkinCaramelToffee"

    def get_flavor(self):
        return self._flavor

    def __str__(self):
        return "PumpkinCaramelToffee"


class CandyCanes(Candy):

    @staticmethod
    def candy_cane_detail_validator(att_dict):
        # quantity": 0, "description": "", "has_nuts": "", "has_lactose": "", "colour":"",
        # Red = 1
        # Green = 2
        valid_attributes_count = 5
        if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
            print("extra column")
            return None
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

    def __init__(self, quantity=0, name='No name', description='', pid='', theme=None, contains_nuts=False,
                 is_lactose_free=False, strips=None):
        super().__init__(quantity, name, description, pid, theme, contains_nuts, is_lactose_free)
        self._strips = strips

    def set_strips(self, strips):
        if strips == CandyCanesStrips.Red:
            self._strips = CandyCanesStrips.Red
        elif strips == CandyCanesStrips.Green:
            self._strips = CandyCanesStrips.Green
        else:
            self._strips = None

    def get_product_type(self):
        return "CandyCanes"

    def get_strips(self):
        return self._strips

    def __str__(self):
        return "CandyCanes"


class CreamEggs(Candy):

    @staticmethod
    def cream_egg_detail_validator(att_dict):
        # quantity": 0, "description": "", "has_nuts": "", "has_lactose": "", "colour":""
        # pack_size
        valid_attributes_count = 5
        if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
            print("extra column")
            return None
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
    def __init__(self, quantity=0, name='No name', description='', pid='', theme=None, contains_nuts=False,
                 is_lactose_free=False, pack_size=0):
        super().__init__(quantity, name, description, pid, theme, contains_nuts, is_lactose_free)
        self._pack_size = pack_size

    def set_pack_size(self, pack_size):
        if pack_size < 0:
            self._pack_size = 0
        self._pack_size = pack_size

    def get_product_type(self):
        return "CreamEggs"

    def get_pack_size(self):
        return self._pack_size

    def __str__(self):
        return "CreamEggs"
