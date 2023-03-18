import pandas as pd
from order import Order
import gift_factory
from gift_factory import ChristmasGiftFactory
from gift_factory import HalloweenGiftFactory
from gift_factory import EasterGiftFactory


class OrderProcessor:
    def __init__(self):
        self._orders_dict = {}
        self._excel_to_dict = {}
        self._order_ids = set()
        self._factory_map_dict = {"Christmas": ChristmasGiftFactory(), "Halloween": HalloweenGiftFactory(),
                                  "Easter": EasterGiftFactory()}

    def convert_dict_from_excel_file(self, excel_file):
        """
        Converts an Excel file to dictionary. Replace nan with empty String.
        :param excel_file: String, the name of Excel file to convert
        """
        excel_data_df = pd.read_excel(excel_file, sheet_name='Sheet1')
        excel_data_df.fillna('', inplace=True)
        dict_version = excel_data_df.to_dict('index')
        self.update_excel_to_dict(dict_version)

    def update_excel_to_dict(self, dict_to_update):
        """
        Setter for updating excel_to_dict
        :param dict_to_update: dictionary that updates excel_to_dict
        """
        self._excel_to_dict = dict_to_update

    def get_excel_to_dict(self):
        """
        Getter for excel_to_dict.
        :return: dictionary, excel_to_dict
        """
        return self._excel_to_dict

    def get_orders(self):
        """
        Getter for created order dictionary.
        :return: dictionary, order_dict
        """
        return self._orders_dict

    def get_order_ids(self):
        return self._order_ids

    def add_order(self, order, holiday):
        """
        Add order and holiday to order_dictionary
        :param order: Created Order
        :param holiday: holiday type
        """
        self.get_orders()[order.get_order_num()] = [order, holiday]

    def create_orders(self):
        """
        Creates order based on each order from excel_to_dict.
        Add the created order to order_dict. Key is order number and value is Order and holiday.
        """
        required_properties = {"order_number": "", "item": "", "name": "", "product_id": ""}
        description = {}
        created_order = None
        holiday = ""
        for key in self.get_excel_to_dict().keys():
            order_to_process = self.get_excel_to_dict()[key]  # get the nth dictionary
            for key in order_to_process.keys():
                value_from_key = order_to_process[key]
                if value_from_key != "":
                    if key != "holiday":
                        if key in required_properties.keys():
                            if key == "product_id":
                                required_properties["product_id"] = value_from_key
                            if key == "item":
                                required_properties["item"] = value_from_key
                            if key == "name":
                                required_properties["name"] = value_from_key
                            if key == "order_number":
                                required_properties["order_number"] = value_from_key
                        else:
                            description[key] = value_from_key
                    else:
                        holiday = value_from_key
                created_order = Order(item_type=required_properties.get("item"),
                                      order_number=required_properties.get("order_number"),
                                      name=required_properties.get("name"),
                                      pid=required_properties.get("product_id"),
                                      description=description)
            if self.validate_order(created_order):
                self.add_order(created_order, holiday)
                self.get_order_ids().add(created_order.get_id())
                holiday = ""
                description = {}  # empty the dictionary

    def get_holiday_of_an_item(self, order):
        return self.get_orders()[order][1]

    def get_corresponding_factory(self, order):
        holiday = self.get_holiday_of_an_item(order)
        item_type = self.get_orders()[order][0].get_item_type()
        for holidays in self._factory_map_dict.keys():
            if holiday == holidays:
                print(holiday)
                print(item_type)
                print(self._factory_map_dict[holidays])
                self._factory_map_dict[holidays].create_item(item=item_type, quantity=10)

    def validate_order(self, order):
        # duplicated id
        # invalid description (not proper attribute), after factory mapping

        if order.get_id() in self.get_order_ids():
            return False
        else:
            return True
