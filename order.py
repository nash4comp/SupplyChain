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
                        print("inside validation function: santa house---------------------------")
                        # print(santa_workshop.get_name())
                        # print(santa_workshop.get_description())
                        # print(santa_workshop.get_is_battery_operated())
                        print("validated_santa_house")
                        return santa_workshop
                    else:
                        return None
            elif item_type == "StuffedAnimal":
                result = gift_factory.StuffedAnimal.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    rein_deer_detail = gift_factory.Reindeer.rein_deer_detail_validator(self.get_attributes())
                    if rein_deer_detail is not None:
                        rein_deer_workshop = gift_factory.Reindeer(quantity=result["quantity"], name=self.get_name(),
                                                                   description=result["description"],
                                                                   pid=self.get_id(), theme=holiday,
                                                                   stuffing=result["stuffing"],
                                                                   size=result["size"])
                        print("inside validation function: rein deer--------------------------------------------")
                        # print(rein_deer_workshop.get_name())
                        # print(rein_deer_workshop.get_description())
                        # print(rein_deer_workshop.get_has_glow())
                        print("validated_rein_deer")
                        return rein_deer_workshop
                    else:
                        return None
            elif item_type == "Candy":
                result = gift_factory.Candy.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    candy_detail = gift_factory.CandyCanes.candy_cane_detail_validator(self.get_attributes())
                    if candy_detail is not None:
                        candy_cane = gift_factory.CandyCanes(quantity=result["quantity"], name=self.get_name(),
                                                             description=result["description"],
                                                             pid=self.get_id(), theme=holiday,
                                                             contains_nuts=result["has_nuts"],
                                                             is_lactose_free=result["has_lactose"])
                        print("inside validation function: candy cane--------------------------------------------")
                        # print(candy_cane.get_name())
                        # print(candy_cane.get_description())
                        # print(candy_cane.get_contains_nuts())
                        print("validated_candy_cane")
                        return candy_cane
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
                        spider = gift_factory.RCSpider(quantity=result["quantity"], name=self.get_name(),
                                                       description=result["description"],
                                                       pid=self.get_id(), theme=holiday,
                                                       is_battery_operated=result["has_batteries"],
                                                       min_age=result["min_age"],
                                                       speed=spider_detail["speed"],
                                                       jump_height=spider_detail["jump_height"],
                                                       spider_type=spider_detail["spider_type"])
                        print("inside validation function: RC spider---------------------------")
                        # print(santa_workshop.get_name())
                        # print(santa_workshop.get_description())
                        # print(santa_workshop.get_is_battery_operated())
                        print("validated_RC spider")
                        return spider
                    else:
                        return None
            elif item_type == "StuffedAnimal":
                result = gift_factory.StuffedAnimal.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    dancing_skeleton_detail = gift_factory.DancingSkeleton.dancing_skeleton_detail_validator(
                        self.get_attributes())
                    if dancing_skeleton_detail is not None:
                        dancing_skeleton = gift_factory.DancingSkeleton(
                            quantity=result["quantity"], name=self.get_name(), description=result["description"],
                            pid=self.get_id(), theme=holiday, stuffing=result["stuffing"], size=result["size"],
                            fabric=dancing_skeleton_detail["fabric"], is_glowing=dancing_skeleton_detail["has_glow"]
                        )
                        print(
                            "inside validation function: dancing skeleton--------------------------------------------")
                        # print(rein_deer_workshop.get_name())
                        # print(dancing_skeleton.get_description())
                        # print(rein_deer_workshop.get_has_glow())
                        print("validated_dancing skeleton")
                        return dancing_skeleton
                    else:
                        return None
            elif item_type == "Candy":
                result = gift_factory.Candy.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    pumpkin_candy_detail = gift_factory.PumpkinCaramelToffee.pumpkin_toffee_detail_validator(
                        self.get_attributes())
                    if pumpkin_candy_detail is not None:
                        pumpkin_candy = gift_factory.PumpkinCaramelToffee(quantity=result["quantity"],
                                                                          name=self.get_name(),
                                                                          description=result["description"],
                                                                          pid=self.get_id(), theme=holiday,
                                                                          contains_nuts=result["has_nuts"],
                                                                          is_lactose_free=result["has_lactose"],
                                                                          flavor=pumpkin_candy_detail["variety"])
                        print("inside validation function: pumpkin_candy--------------------------------------------")
                        # print(candy_cane.get_name())
                        # print(candy_cane.get_description())
                        # print(candy_cane.get_contains_nuts())
                        print("validated_pumpkin_candy")
                        return pumpkin_candy
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
                        robot_bunny = gift_factory.RobotBunny(quantity=result["quantity"], name=self.get_name(),
                                                              description=result["description"],
                                                              pid=self.get_id(), theme=holiday,
                                                              is_battery_operated=result["has_batteries"],
                                                              min_age=result["min_age"],
                                                              num_of_sound_effects=robot_bunny_detail["num_sound"],
                                                              color=robot_bunny_detail["colour"])
                        print("inside validation function: robot_bunny---------------------------")
                        # print(santa_workshop.get_name())
                        # print(santa_workshop.get_description())
                        # print(santa_workshop.get_is_battery_operated())
                        print("validated_robot_bunny")
                        return robot_bunny
                    else:
                        return None
            elif item_type == "StuffedAnimal":
                result = gift_factory.StuffedAnimal.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    east_bunny_detail = gift_factory.EasterBunny.east_bunny_detail_validator(self.get_attributes())
                    if east_bunny_detail is not None:
                        east_bunny = gift_factory.EasterBunny(quantity=result["quantity"], name=self.get_name(),
                                                              description=result["description"],
                                                              pid=self.get_id(), theme=holiday,
                                                              stuffing=result["stuffing"],
                                                              size=result["size"],
                                                              fabric=east_bunny_detail["fabric"],
                                                              color=east_bunny_detail["colour"])
                        print("inside validation function: east_bunny--------------------------------------------")
                        # print(rein_deer_workshop.get_name())
                        # print(rein_deer_workshop.get_description())
                        # print(rein_deer_workshop.get_has_glow())
                        print("validated_east bunny")
                        return east_bunny
                    else:
                        return None
            elif item_type == "Candy":
                result = gift_factory.Candy.validate_attribute(self.get_attributes())
                if type(result) == dict:
                    cream_egg_detail = gift_factory.CreamEggs.cream_egg_detail_validator(self.get_attributes())
                    if cream_egg_detail is not None:
                        cream_egg = gift_factory.CreamEggs(quantity=result["quantity"], name=self.get_name(),
                                                            description=result["description"],
                                                            pid=self.get_id(), theme=holiday,
                                                            contains_nuts=result["has_nuts"],
                                                            is_lactose_free=result["has_lactose"],
                                                            pack_size=cream_egg_detail["pack_size"])
                        print("inside validation function: cream egg--------------------------------------------")
                        # print(candy_cane.get_name())
                        # print(candy_cane.get_description())
                        # print(candy_cane.get_contains_nuts())
                        print("validated_cream egg")
                        return cream_egg
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
               f"attribute : {self.get_attributes()}"


class Item(Enum):
    TOY = "Toy",
    STUFFED_ANIMAL = "StuffedAnimal",
    CANDY = "Candy"


class Holiday(Enum):
    XMAS = "Christmas",
    EASTER = "Easter",
    HALLOWEEN = "Halloween"
