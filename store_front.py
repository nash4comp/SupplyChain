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

from store import Store


class StoreFront:
	def __init__(self):
		self._store = Store()

	def display_menu(self, inv, factory):
		valid_user_inputs = ["1", "2", "3"]
		user_input = None
		while user_input != 3:
			print("Welcome to the store front")
			print("1. Process web orders")
			print("2. Check inventory")
			print("3. Exit")
			string_input = input("Please enter a number from 1 - 3\n> ")
			if string_input == '':
				continue
			if string_input not in valid_user_inputs:
				print("Please enter a number between 1 to 3")
				continue
			user_input = int(string_input)
			if user_input == 1:
				self._store.menu_process_web_orders(inv, factory)
			elif user_input == 2:
				inv.display_each_item_inventory()
			elif user_input == 3:
				self._store.export_daily_transaction_report()
			else:
				print("Could not process the input. Please enter a number from 1 - 3.")
		print("Thank you for visiting the store.")
