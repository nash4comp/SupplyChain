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

import datetime
from order_processor import OrderProcessor


class Store:
    """
    This class is backend for store_front.
    Handles order_processing, inventory monitor, and daily transaction report.
    """
    def __init__(self):
        """
        Initialize Store.
        Records has valid orders.
        """
        self._order_processor = OrderProcessor()
        self._orders_without_validation = {}
        self._records = {}  # this record has only valid orders

    def menu_process_web_orders(self, inv, factory):
        """
        Process web order by reading an Excel file and creating Order objects.
        Based on created Order objects, validate them, if validate then check inventory
        :param inv: Inventory
        :param factory: GiftFactory
        """
        file_to_read = input("Please enter the Excel file name: ")
        self.get_order_processor().convert_dict_from_excel_file(file_to_read)
        self.get_order_processor().create_orders()  # just create orders without any validation
        self.update_orders_without_validation(self.get_order_processor().get_orders())
        self.validate_order()
        print(self.get_order_processor().get_orders().values())
        print(len(self.get_order_processor().get_orders().values()))
        print(self.get_order_processor().get_valid_orders_list())
        print(len(self.get_order_processor().get_valid_orders_list()))
        for each_order_dict in self.get_order_processor().get_valid_orders_list():
            key = each_order_dict.values()
            print(key)
            print(type(key))
            # inv.check_item_quantity(each_order[0].get_all_info_dict_for_factory_creation(), factory)

        # for each_order in self.get_order_processor().get_orders().values():
        #     inv.check_item_quantity(each_order[0].get_all_info_dict_for_factory_creation(), factory)

    def validate_order(self):
        """
        Validate each order inside valid orders inside OrderProcessing.
        """
        for order in self.get_order_processor().get_orders().values():
            order_object = order[0]
            holiday = order[1]
            order_object.validate_details(holiday)

    def export_daily_transaction_report(self):
        """
        Write Daily Transaction Report (DRT) that contains valid orders
        """
        text_file_name = self.text_file_name_generator()
        now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        with open(text_file_name, 'w', encoding='utf-8') as f:
            f.write("Holiday Store - Daily Transaction Report(DTR)\n")
            f.write(now)
            f.write("\n")
            key = 1
            for order in self.get_order_processor().get_valid_orders_list():
                f.write(f"{order[key]}\n")
                key += 1

    def get_order_processor(self):
        """
        Getter for _order_processor
        :return: OrderProcessor
        """
        return self._order_processor

    def text_file_name_generator(self):
        """
        Format text_file_name
        :return: formatted string
        """
        now = datetime.datetime.now()
        date_str = now.strftime('%d%m%y')
        time_str = now.strftime('%H%M')
        file_name = f"DTR_{date_str}_{time_str}.txt"
        return file_name

    def update_orders_without_validation(self, dict_to_update):
        """
        Setter for orders_without_validation dictionary.
        :param dict_to_update: dictionary
        """
        self._orders_without_validation = dict_to_update
