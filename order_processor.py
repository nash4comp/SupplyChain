import os

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

import pandas as pd
from order import Order
from gift_factory import GiftFactory


class OrderProcessor:
    """
    OrderProcessor class that processes orders from Excel file.
    """
    def __init__(self):
        """
        Constructor for OrderProcessor class.
        """
        self._orders_dict = {}
        self._excel_to_dict = {}
        self._factory_map = GiftFactory()
        self._valid_orders = []
        self._valid_order_nums = []

    def convert_dict_from_excel_file(self, excel_file):
        """
        Converts an Excel file to dictionary. Replace nan with empty String.
        :param excel_file: String, the name of Excel file to convert
        """
        if os.path.isfile(excel_file):
            excel_data_df = pd.read_excel(excel_file, sheet_name='Sheet1')
            excel_data_df.fillna('', inplace=True)
            dict_version = excel_data_df.to_dict('index')
            self.update_excel_to_dict(dict_version)
        else:
            print(f"The file {excel_file} does not exist in the current directory.")

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
        valid_item_types = {"Toy", "StuffedAnimal", "Candy"}
        valid_theme = {"Christmas", "Halloween", "Easter"}
        attributes = {}
        created_order = None
        holiday = ""
        for key in self.get_excel_to_dict().keys():
            order_to_process = self.get_excel_to_dict()[key]  # get the nth dictionary
            for key_inside in order_to_process.keys():
                value_from_key = order_to_process[key_inside]
                if value_from_key != "":
                    if key_inside != "holiday":
                        if key_inside in required_properties.keys():
                            if key_inside == "product_id":
                                if key_inside is not None:
                                    required_properties["product_id"] = value_from_key
                            if key_inside == "item":
                                if value_from_key in valid_item_types:
                                    required_properties["item"] = value_from_key
                            if key_inside == "name":
                                if value_from_key is not None:
                                    required_properties["name"] = value_from_key
                            if key_inside == "order_number":
                                if key_inside is not None:
                                    required_properties["order_number"] = value_from_key
                        else:
                            attributes[key_inside] = value_from_key
                    else:
                        if value_from_key in valid_theme:
                            holiday = value_from_key
                created_order = Order(item_type=required_properties.get("item"),
                                      order_number=required_properties.get("order_number"),
                                      name=required_properties.get("name"),
                                      product_id=required_properties.get("product_id"),
                                      attribute=attributes)
            if created_order.get_order_num() not in self._valid_order_nums:
                self.add_order(created_order, holiday)
                valid_order = created_order.validate_details(holiday)
                if valid_order is not None:
                    self.get_valid_orders_list().append({created_order.get_order_num(): valid_order})
                    self.get_valid_order_num().append(created_order.get_order_num())
            holiday = ""
            attributes = {}

    def get_holiday_of_an_item(self, order):
        """
        Getter for holiday of an order
        :param order: Order
        :return: String, holiday
        """
        return self.get_orders()[order][1]

    def get_valid_order_num(self):
        """
        Getter for valid_order_num list.
        :return: list, list of valid order numbers
        """
        return self._valid_order_nums

    def get_valid_orders_list(self):
        """
        Getter for valid order list.
        :return: list of dictionary that contains each valid order
        """
        return self._valid_orders
