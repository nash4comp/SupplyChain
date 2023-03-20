from enum import Enum
import gift_factory


class Order:
    def __init__(self, item_type, order_number, name, pid, **kwargs):
        self._item_type = item_type
        self._orderNum = int(order_number)
        self._name = name
        self._pid = pid
        self._detail = kwargs  # decode the kwargs

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

    def get_item_type(self):
        return self._item_type

    def validate_details(self, holiday):
        item_type = self.get_item_type()
        if holiday == "Christmas":
            if item_type == "Toy":
                result = gift_factory.Toy.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    santa_detail = gift_factory.SantasWorkshop.santa_detail_validator(self.get_attributes())
                    if santa_detail is not None:
                        santa_workshop = gift_factory.SantasWorkshop(quantity=result["quantity"], name=self.get_name(),
                                                                     description=result["description"],
                                                                     pid=self.get_id(), theme=holiday,
                                                                     is_battery_operated=result["has_batteries"],
                                                                     min_age=result["min_age"],
                                                                     dimension=santa_detail["dimension"],
                                                                     num_of_rooms=santa_detail["num_of_rooms"])
                        print("validated_santa_house")
                        return santa_workshop






    def __str__(self):
        return f"order number: {self.get_order_num()}, " \
               f"item type: {self._item_type}, " \
               f"name: {self._name}, " \
               f"id: {self.get_id()}, " \
               f"attribute : {self.get_attributes()}"


class Item(Enum):
    TOY = "Toy",
    STUFFED_ANIMAL = "StuffedAnimal",
    CANDY = "Candy"


class Holiday(Enum):
    XMAS = "Christmas",
    EASTER = "Easter",
    HALLOWEEN = "Halloween"
