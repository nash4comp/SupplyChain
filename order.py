from enum import Enum


class Order:
    def __init__(self, item_type, order_number, name, pid, **kwargs):
        self._item_type = item_type
        self._orderNum = order_number
        self._name = name
        self._pid = pid
        self._detail = kwargs  # decode the kwargs

    def get_id(self):
        """
        Getter for id
        :return: String, id
        """
        return self._pid

    def get_order_num(self):
        """
        Getter for id
        :return: String, id
        """
        return self._orderNum

    def get_description(self):
        return self._detail.items()

    def get_item_type(self):
        return self._item_type

    def __str__(self):
        return f"order number: {self.get_order_num()}, "\
               f"item type: {self._item_type}, " \
               f"name: {self._name}, " \
               f"id: {self.get_id()}, " \
               f"description : {self.get_description()}"


class Item(Enum):
    TOY = "Toy",
    STUFFED_ANIMAL = "StuffedAnimal",
    CANDY = "Candy"


class Holiday(Enum):
    XMAS = "Christmas",
    EASTER = "Easter",
    HALLOWEEN = "Halloween"
