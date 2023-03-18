"""
# TODO: Add title and description

# Name1: Nash Baek (nash4comp@gmail.com)
# Student number1: A01243888

# Name2: Taylor Ji (taylor.ji719@gmail.com)
# Student number2: A01304056

UML diagram: https://app.diagrams.net/#G18MWO3bp974lfK4Ceehz2vUfH8YmqEEfE
"""

from abc import ABC


class GiftFactory(ABC):
    def __init__(self):
        pass

    @staticmethod
    def classify_item(theme, item, num):
        if theme == 'Christmas':
            cf = ChristmasGiftFactory()
            cf.create_item(item, num)
        elif theme == 'Halloween':
            hf = HalloweenGiftFactory()
            hf.create_item(item, num)
        elif theme == 'Easter':
            ef = EasterGiftFactory()
            ef.create_item(item, num)


class ChristmasGiftFactory(GiftFactory):

    def __init__(self):
        super().__init__()

    def create_item(self, item, quantity):
        if item == 'Toy':
            product_name = 'SantasWorkshop'
            self.create_toy(product_name, quantity)
        elif item == 'Stuffed_animal':
            product_name = 'Reindeer'
            self.create_stuffed_animal(product_name, quantity)
        elif item == 'Candy':
            product_name = 'CandyCane'
            self.create_candy(product_name, quantity)

    def test(self):
        return "test Chirstmas toy"

    def create_toy(self, product_name, num):
        print(str(num) + " " + product_name + " created.")

    def create_stuffed_animal(self, product_name, num):
        print(str(num) + " " + product_name + " created.")

    def create_candy(self, product_name, num):
        print(str(num) + " " + product_name + " created.")


class HalloweenGiftFactory(GiftFactory):

    def __init__(self):
        super().__init__()

    def create_item(self, item, num):
        if item == 'Toys':
            product_name = 'RCSniper'
            self.create_toy(product_name, num)
        elif item == 'Stuffed_animal':
            product_name = 'DancingSkeleton'
            self.create_stuffed_animal(product_name, num)
        elif item == 'Candy':
            product_name = 'PumpkinCaramelToffee'
            self.create_candy(product_name, num)

    def create_toy(self, product_name, num):
        print(str(num) + " " + product_name + " created.")

    def create_stuffed_animal(self, product_name, num):
        print(str(num) + " " + product_name + " created.")

    def create_candy(self, product_name, num):
        print(str(num) + " " + product_name + " created.")


class EasterGiftFactory(GiftFactory):

    def __init__(self):
        super().__init__()

    def create_item(self, item, num):
        if item == 'Toys':
            product_name = 'RobotBunny'
            self.create_toy(product_name, num)
        elif item == 'Stuffed_animal':
            product_name = 'EasterBunny'
            self.create_stuffed_animal(product_name, num)
        elif item == 'Candy':
            product_name = 'CreamEggs'
            self.create_candy(product_name, num)

    def create_toy(self, product_name, num):
        print(str(num) + " " + product_name + " created.")

    def create_stuffed_animal(self, product_name, num):
        print(str(num) + " " + product_name + " created.")

    def create_candy(self, product_name, num):
        print(str(num) + " " + product_name + " created.")


class Product(ABC):
    def __init__(self, name, description, pid, theme):
        self._name = name
        self._description = description
        self._pid = pid
        self._theme = theme

    def __str__(self):
        return "Product"


class Toy(Product):
    def __init__(self, name, description, pid, theme, is_battery_operated, min_age):
        super().__init__(name, description, pid, theme)
        self._is_battery_operated = is_battery_operated
        self._min_age = min_age

    def __str__(self):
        return "Toy"


class SantasWorkshop(Toy):
    def __init__(self, name, description, pid, theme, is_battery_operated, min_age, width, height, num_of_rooms):
        super().__init__(name, description, pid, theme, is_battery_operated, min_age)
        self._width = width
        self._height = height
        self._num_of_rooms = num_of_rooms

    def __str__(self):
        return "SantasWorkshop"


class RCSpider(Toy):
    def __init__(self, name, description, pid, theme, is_battery_operated, min_age, speed, jump_height, is_glowing,
                 spider_type):
        super().__init__(name, description, pid, theme, is_battery_operated, min_age)
        self._speed = speed
        self._jump_height = jump_height
        self._is_glowing = is_glowing
        self._spider_type = spider_type

    def __str__(self):
        return "RCSpider"


class RobotBunny(Toy):
    def __init__(self, name, description, pid, theme, is_battery_operated, min_age, num_of_sound_effects, color):
        super().__init__(name, description, pid, theme, is_battery_operated, min_age)
        self._num_of_sound_effects = num_of_sound_effects
        self._color = color

    def __str__(self):
        return "RobotBunny"


class StuffedAnimal(Product):
    def __init__(self, name, description, pid, theme, stuffing, size, fabric):
        super().__init__(name, description, pid, theme)
        self._stuffing = stuffing
        self._size = size
        self._fabric = fabric

    def __str__(self):
        return "StuffedAnimal"


class DancingSkeleton(StuffedAnimal):
    def __init__(self, name, description, pid, theme, stuffing, size, fabric, is_glowing):
        super().__init__(name, description, pid, theme, stuffing, size, fabric)
        self._is_glowing = is_glowing

    def __str__(self):
        return "DancingSkeleton"


class Reindeer(StuffedAnimal):
    def __init__(self, name, description, pid, theme, stuffing, size, fabric, has_glow):
        super().__init__(name, description, pid, theme, stuffing, size, fabric)
        self._has_glow = has_glow

    def __str__(self):
        return "Reindeer"


class EasterBunny(StuffedAnimal):
    def __init__(self, name, description, pid, theme, stuffing, size, fabric, num_of_sound_effects, color):
        super().__init__(name, description, pid, theme, stuffing, size, fabric)
        self._num_of_sound_effects = num_of_sound_effects
        self._color = color

    def __str__(self):
        return "EasterBunny"


class Candy(Product):
    def __init__(self, name, description, pid, theme, contains_nuts, is_lactose_free):
        super().__init__(name, description, pid, theme)
        self._contains_nuts = contains_nuts
        self._is_lactose_free = is_lactose_free

    def __str__(self):
        return "Candy"


class PumpkinCaramelToffee(Candy):
    def __init__(self, name, description, pid, theme, contains_nuts, is_lactose_free, flavor):
        super().__init__(name, description, pid, theme, contains_nuts, is_lactose_free)
        self._flavor = flavor

    def __str__(self):
        return "PumpkinCaramelToffee"


class CandyCanes(Candy):
    def __init__(self, name, description, pid, theme, contains_nuts, is_lactose_free, color):
        super().__init__(name, description, pid, theme, contains_nuts, is_lactose_free)
        self._color = color

    def __str__(self):
        return "CandyCanes"


class CreamEggs(Candy):
    def __init__(self, name, description, pid, theme, contains_nuts, is_lactose_free, pack_size):
        super().__init__(name, description, pid, theme, contains_nuts, is_lactose_free)
        self._pack_size = pack_size

    def __str__(self):
        return "CreamEggs"
