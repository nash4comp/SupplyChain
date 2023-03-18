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

            if user_input == 0:  # read the Excel file and create order object
                file_to_read = input("Please enter the excel file name to read: ")
                self.get_order_processor().convert_dict_from_excel_file(file_to_read)
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
                # print(self.get_order_processor().get_orders().get(1))
                # print(self.get_order_processor().get_holiday_of_an_item(1))
                # print(self.get_order_processor().get_orders().get(1)[0])
                # print(self.get_order_processor().get_orders().get(1)[0].get_item_type())
                print(self.get_order_processor().get_corresponding_factory(1))
                # print(self.get_order_processor().get_orders().get(2))
                # print(self.get_order_processor().get_orders().get(2)[0])
            else:
                print("Could not process the input. Please enter a number from 1 - 3.")
        print("Thank you for visiting the store.")

    def export_daily_transaction_report(self):
        # create a txt file contains valid orders
        text_file_name = self.text_file_name_generator()
        with open(text_file_name, 'w') as f:
            f.write('Create a new text file!')

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


