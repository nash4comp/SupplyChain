import pandas as pd
from order import Order
from item import Item

excel_data_df = pd.read_excel('orders.xlsx', sheet_name='Sheet1')
excel_data_df.fillna('', inplace=True)  # replace nan with empty string
dict_version = excel_data_df.to_dict('index')  # convert dictionary row by row
print(dict_version.items())
first_itme = dict_version[0]
pid = ""
item_type = None
pname = ""
oder_num = 0
test_order = None
description = {}
holiday = ""
properties = ["product_id", "item", "name", "order_number"]
for key in first_itme.keys():
    value_from_dict = first_itme[key]
    if value_from_dict != "":
        if key != "holiday":
            if key in properties:
                if key == "product_id":
                    pid = value_from_dict
                if key == "item":
                    item_type = value_from_dict
                if key == "name":
                    pname = value_from_dict
                if key == "order_number":
                    quantity = value_from_dict
            else:
                description[key] = value_from_dict
            test_order = Order(pid=pid, item_type=item_type, name=pname, order_number=oder_num, description=description)

        else:
            holiday = value_from_dict

        print(f"{key} : {first_itme[key]}")


print(test_order.get_description())


# test_process = Order()
