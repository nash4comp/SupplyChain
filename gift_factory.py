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
import inventory


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


class GiftFactory(ABC):
    def __init__(self):
        pass

    @staticmethod
    def classify_item(theme, item, quantity):
        if theme == Theme.Christmas:
            cf = ChristmasGiftFactory()
            cf.create_item(item, quantity)
        elif theme == Theme.Halloween:
            hf = HalloweenGiftFactory()
            hf.create_item(item, quantity)
        elif theme == Theme.Easter:
            ef = EasterGiftFactory()
            ef.create_item(item, quantity)


class ChristmasGiftFactory(GiftFactory):

    def __init__(self):
        super().__init__()

    def create_item(self, item, quantity):
        if item == "Toy":
            product_name = Products.Toy.SantasWorkshop
            self.create_toy(product_name, quantity)
        elif item == "StuffedAnimal":
            product_name = Products.StuffedAnimal.Reindeer
            self.create_stuffed_animal(product_name, quantity)
        elif item == "Candy":
            product_name = Products.Candy.CandyCanes
            self.create_candy(product_name, quantity)

    def create_toy(self, product_name, quantity):
        inventory.Inventory().add_item("Toy", product_name, quantity, Theme.Christmas)
        print(str(quantity) + " " + product_name + " created.")

    def create_stuffed_animal(self, product_name, quantity):
        print(str(quantity) + " " + product_name + " created.")

    def create_candy(self, product_name, quantity):
        print(str(quantity) + " " + product_name + " created.")


class HalloweenGiftFactory(GiftFactory):

    def __init__(self):
        super().__init__()

    def create_item(self, item, quantity):
        if item == "Toy":
            product_name = Products.Toy.RCSpider
            self.create_toy(product_name, quantity)
        elif item == "StuffedAnimal":
            product_name = Products.StuffedAnimal.DancingSkeleton
            self.create_stuffed_animal(product_name, quantity)
        elif item == "Candy":
            product_name = Products.Candy.PumpkinCaramelToffee
            self.create_candy(product_name, quantity)

    def create_toy(self, product_name, quantity):
        print(str(quantity) + " " + product_name + " created.")

    def create_stuffed_animal(self, product_name, quantity):
        print(str(quantity) + " " + product_name + " created.")

    def create_candy(self, product_name, quantity):
        print(str(quantity) + " " + product_name + " created.")


class EasterGiftFactory(GiftFactory):

    def __init__(self):
        super().__init__()

    def create_item(self, item, quantity):
        if item == "Toy":
            product_name = Products.Toy.RobotBunny
            self.create_toy(product_name, quantity)
        elif item == "StuffedAnimal":
            product_name = Products.StuffedAnimal.EasterBunny
            self.create_stuffed_animal(product_name, quantity)
        elif item == "Candy":
            product_name = Products.Candy.CreamEggs
            self.create_candy(product_name, quantity)

    def create_toy(self, product_name, quantity):
        print(str(quantity) + " " + product_name + " created.")

    def create_stuffed_animal(self, product_name, quantity):
        print(str(quantity) + " " + product_name + " created.")

    def create_candy(self, product_name, quantity):
        print(str(quantity) + " " + product_name + " created.")


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
                    valid_attributes_toy["has_batteries"] = attribute_dict[attribute]
                    valid_attribute_count += 1
                if attribute == "min_age" and type(attribute_dict[attribute]) == float:
                    valid_attributes_toy["min_age"] = attribute_dict[attribute]
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
        valid_santa_attributes = {"dimension": "", "num_of_rooms": 0}
        for key_att_dict in att_dict.keys():
            if key_att_dict == "dimensions":
                valid_santa_attributes["dimension"] = att_dict[key_att_dict]
            if key_att_dict == "num_rooms":
                valid_santa_attributes["num_of_rooms"] = att_dict[key_att_dict]
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

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_num_of_rooms(self):
        return self._num_of_rooms

    def __str__(self):
        return "SantasWorkshop"


class RCSpider(Toy):
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
    def __init__(self, quantity=0, name='No name', description='', pid='', theme=None, stuffing=None, size=None,
                 fabric=None, num_of_sound_effects=0, color=None):
        super().__init__(quantity, name, description, pid, theme, stuffing, size, fabric)
        self._num_of_sound_effects = num_of_sound_effects
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
