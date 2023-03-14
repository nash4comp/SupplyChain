"""
# TODO: Add title and description

# Name1: Nash Baek (nash4comp@gmail.com)
# Student number1: A01243888

# Name2: Taylor Ji (taylor.ji719@gmail.com)
# Student number2: A01304056

UML diagram: https://app.diagrams.net/#G18MWO3bp974lfK4Ceehz2vUfH8YmqEEfE
"""

import gift_factory

def display_menu():
	user_input = None
	while user_input != 3:
		print("Welcome to the store")
		print("0. Create Test")
		print("1. Process web orders")
		print("2. Check inventory")
		print("3. Exit")
		string_input = input("Please enter a number from 1 - 3\n> ")

		if string_input == '':
			continue
		user_input = int(string_input)

		if user_input == 0:
			gf = gift_factory.GiftFactory()
			gf.classify_item('Christmas', 'Toys', 100)
			gf.classify_item('Christmas', 'Stuffed_animal', 99)
			gf.classify_item('Christmas', 'Candy', 98)
			gf.classify_item('Halloween', 'Toys', 97)
			gf.classify_item('Halloween', 'Stuffed_animal', 96)
			gf.classify_item('Halloween', 'Candy', 95)
			gf.classify_item('Easter', 'Toys', 94)
			gf.classify_item('Easter', 'Stuffed_animal', 93)
			gf.classify_item('Easter', 'Candy', 92)

		if user_input == 1:
			# self.process_web_orders()
			pass
		elif user_input == 2:
			# self.check_inventory()
			pass
		elif user_input == 3:
			pass
		else:
			print("Could not process the input. Please enter a number from 1 - 3.")
	print("Thank you for visiting the store.")


class StoreFront:
	def __init__(self):
		pass
