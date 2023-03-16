# read excel file
import pandas as pd
from order import Order


class OrderProcessor:
    def __init__(self):
        self._orders_dict = {}
        self._excel_to_dict = {}

    def convert_dict_from_excel_file(self, excel_file):
        excel_data_df = pd.read_excel(excel_file, sheet_name='Sheet1')
        excel_data_df.fillna('', inplace=True)  # replace nan with empty string
        dict_version = excel_data_df.to_dict('index')
        self.update_excel_to_dict(dict_version)

    def update_excel_to_dict(self, dict):
        self._excel_to_dict = dict

    def get_excel_to_dict(self):
        return self._excel_to_dict

    def get_orders(self):
        return self._orders_dict

    def add_order(self, order, holiday):
        self.get_orders()[order.get_order_num()] = {order, holiday}

    def create_oders(self):
        required_properties = {"order_number": "", "item": "", "name": "", "product_id": ""}
        description = {}
        created_order = None
        holiday = ""
        for key in self.get_excel_to_dict().keys():
            order_to_process = self.get_excel_to_dict()[key]  # get the nth dictionary
            # print(order_to_process)
            for key in order_to_process.keys():
                value_from_key = order_to_process[key]
                # print(value_from_key)
                if value_from_key != "":
                    if key != "holiday":
                        if key in required_properties.keys():
                            if key == "product_id":
                                required_properties["product_id"] = value_from_key
                                # print(required_properties["product_id"])
                            if key == "item":
                                required_properties["item"] = value_from_key
                                # print(required_properties["item"])
                            if key == "name":
                                required_properties["name"] = value_from_key
                                # print(required_properties["name"])
                            if key == "order_number":
                                required_properties["order_number"] = value_from_key
                                # print(required_properties["order_number"])
                        else:
                            description[key] = value_from_key
                    else:
                        holiday = value_from_key
                created_order = Order(item_type=required_properties.get("item"),
                                      order_number=required_properties.get("order_number"),
                                      name=required_properties.get("name"),
                                      pid=required_properties.get("product_id"),
                                      description=description)
            self.add_order(created_order, holiday)
            holiday = ""


test = OrderProcessor()
test.convert_dict_from_excel_file('orders.xlsx')
test.create_oders()
print(test.get_orders().items())

