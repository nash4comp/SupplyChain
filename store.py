import datetime
from order_processor import OrderProcessor


class Store:
    def __init__(self):
        self._order_processor = OrderProcessor()
        self._orders_without_validation = {}
        self._records = {}  # this record has only valid orders

    def menu_process_web_orders(self, inv, factory):
        file_to_read = int(input("If you want to read orders.xlsx enter 1 "))
        if file_to_read == 1:
            excel_file = "orders.xlsx"
            self.get_order_processor().convert_dict_from_excel_file(excel_file)
            self.get_order_processor().create_orders()  # just create orders without any validation
            self.update_orders_without_validation(self.get_order_processor().get_orders())
            self.validate_order()
        for each_order in self.get_order_processor().get_orders().values():
            inv.check_item_quantity(each_order[0].get_all_info_dict_for_factory_creation(), factory)

    def validate_order(self):
        for order in self.get_order_processor().get_orders().values():
            order_object = order[0]
            holiday = order[1]
            order_object.validate_details(holiday)

    def export_daily_transaction_report(self):
        # create a txt file contains valid orders
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
        return self._order_processor

    def text_file_name_generator(self):
        now = datetime.datetime.now()
        date_str = now.strftime('%d%m%y')
        time_str = now.strftime('%H%M')
        file_name = f"DTR_{date_str}_{time_str}.txt"
        return file_name

    def update_orders_without_validation(self, dict_to_update):
        self._orders_without_validation = dict_to_update


