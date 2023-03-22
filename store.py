import datetime
from oder_processor import OrderProcessor


class Store:
    def __init__(self):
        self._order_processor = OrderProcessor()
        self._orders_without_validation = {}
        self._records = {}  # this record has only valid orders

    def display_menu(self):
        user_input = None
        while user_input != 3:
            print("Welcome to the store")
            print("0. Receive orders and maintain inventory")
            print("1. Create items that need to be re-stocked")
            print("2. Generate Daily Transaction Report")
            print("3. Exit")
            print("4. test")
            string_input = input("Please enter a number from 1 - 3\n> ")

            if string_input == '':
                continue
            user_input = int(string_input)

            if user_input == 0:  # read the Excel file and create order object and validate order
                file_to_read = int(input("If you want to read orders.xlsx enter 1 "))
                if file_to_read == 1:
                    excel_file = "orders.xlsx"
                    self.get_order_processor().convert_dict_from_excel_file(excel_file)
                    self.get_order_processor().create_orders()  # just create orders without any validation
                    self.update_orders_without_validation(self.get_order_processor().get_orders())
                print(self.get_order_processor().get_orders())

            if user_input == 1:  #
                # self.process_web_orders()
                pass
            elif user_input == 2:  # create a txt file for valid orders
                # self.check_inventory()
                pass
            elif user_input == 3:
                self.export_daily_transaction_report()
            elif user_input == 4:
                # print(self.get_order_processor().get_orders().items())
                for order in self.get_order_processor().get_orders().values():
                    # print(order)
                    order_object = order[0]
                    holiday = order[1]
                    # print(order_object)
                    # print(holiday)
                    # item_type = order_object.get_item_type()
                    # print(order_object)
                    # print(item_type)
                    # print(holiday)
                    # print(order_object.get_attributes())
                    order_object.validate_details(holiday)
                # print(self.get_order_processor().get_valid_orders_list())
                self.get_order_processor().print_valid_order_product_name()

            else:
                print("Could not process the input. Please enter a number from 1 - 3.")
        print("Thank you for visiting the store.")

    def menu_process_web_orders(self):
        file_to_read = int(input("If you want to read orders.xlsx enter 1 "))
        if file_to_read == 1:
            excel_file = "orders.xlsx"
            self.get_order_processor().convert_dict_from_excel_file(excel_file)
            self.get_order_processor().create_orders()  # just create orders without any validation
            self.update_orders_without_validation(self.get_order_processor().get_orders())
        print(self.get_order_processor().get_orders())

    def export_daily_transaction_report(self):
        # create a txt file contains valid orders
        text_file_name = self.text_file_name_generator()
        now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        with open(text_file_name, 'w') as f:
            f.write("Holiday Store - Daily Transaction Report(DTR)\n")
            f.write(now)
            f.write("\n")
            key = 1
            for order in self.get_order_processor().get_valid_orders_list():
                # print(order)
                f.write(f"{order[key]}\n")
                key += 1
            self.get_order_processor().print_valid_order_product_name()
            # for valid_order in self.get_order_processor().get_valid_orders_list():
            #     f.write(valid_order.daily_transaction_report_form())
            # f.write('Create a new text file!')

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


test = Store()
test.display_menu()
