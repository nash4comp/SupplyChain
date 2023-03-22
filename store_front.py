"""
# TODO: Add title and description

# Name1: Nash Baek (nash4comp@gmail.com)
# Student number1: A01243888

# Name2: Taylor Ji (taylor.ji719@gmail.com)
# Student number2: A01304056

UML diagram: https://app.diagrams.net/#G18MWO3bp974lfK4Ceehz2vUfH8YmqEEfE
"""

from store import Store


# def display_menu(inv, factory):
# 	santas_workshop = factory.create_item(theme="Christmas", item_type="Toys")
# 	reindeer = factory.create_item(theme="Christmas", item_type="StuffedAnimal")
# 	candy_canes = factory.create_item(theme="Christmas", item_type="Candy")
#
# 	rc_spider = factory.create_item(theme="Halloween", item_type="Toys")
# 	dancing_skeleton = factory.create_item(theme="Halloween", item_type="StuffedAnimal")
# 	pumpkin_caramel_toffee = factory.create_item(theme="Halloween", item_type="Candy")
#
# 	robot_bunny = factory.create_item(theme="Easter", item_type="Toys")
# 	easter_bunny = factory.create_item(theme="Easter", item_type="StuffedAnimal")
# 	cream_eggs = factory.create_item(theme="Easter", item_type="Candy")
#
# 	items = [santas_workshop, reindeer, candy_canes, rc_spider, dancing_skeleton, pumpkin_caramel_toffee, robot_bunny,
# 	         easter_bunny, cream_eggs]
#
# 	user_input = None
# 	while user_input != 3:
# 		print("Welcome to the store")
# 		print("0. Create Test")
# 		print("1. Process web orders")
# 		print("2. Check inventory")
# 		print("3. Exit")
# 		print("4. Inventory append test with default values")
# 		print("5. Inventory append test with hard coded values")
# 		string_input = input("Please enter a number from 1 - 3\n> ")
#
# 		if string_input == '':
# 			continue
# 		user_input = int(string_input)
#
# 		if user_input == 0:
# 			pass
#
# 		if user_input == 1:
# 			# self.process_web_orders()
# 			pass
# 		elif user_input == 2:
# 			inv.display_inventory()
# 		elif user_input == 3:
# 			pass
# 		elif user_input == 4:
# 			inv.inventory_test(items)
# 		elif user_input == 5:
# 			inv.inventory_test2(factory)
# 		else:
# 			print("Could not process the input. Please enter a number from 1 - 3.")
# 	print("Thank you for visiting the store.")


class StoreFront:
	def __init__(self):
		self._store = Store()

	def display_menu(self, inv, factory):
		santas_workshop = factory.create_item(theme="Christmas", item_type="Toy")
		reindeer = factory.create_item(theme="Christmas", item_type="StuffedAnimal")
		candy_canes = factory.create_item(theme="Christmas", item_type="Candy")

		rc_spider = factory.create_item(theme="Halloween", item_type="Toy")
		dancing_skeleton = factory.create_item(theme="Halloween", item_type="StuffedAnimal")
		pumpkin_caramel_toffee = factory.create_item(theme="Halloween", item_type="Candy")

		robot_bunny = factory.create_item(theme="Easter", item_type="Toy")
		easter_bunny = factory.create_item(theme="Easter", item_type="StuffedAnimal")
		cream_eggs = factory.create_item(theme="Easter", item_type="Candy")

		items = [santas_workshop, reindeer, candy_canes, rc_spider, dancing_skeleton, pumpkin_caramel_toffee,
		         robot_bunny, easter_bunny, cream_eggs]

		user_input = None
		while user_input != 3:
			print("Welcome to the store front!!!!!!!!!!!")
			print("0. Create Test")
			print("1. Process web orders")
			print("2. Check inventory")
			print("3. Exit")
			print("4. Inventory append test with default values")
			print("5. Inventory append test with hard coded values")
			print("6. Inventory append test with hard coded values")
			string_input = input("Please enter a number from 1 - 3\n> ")

			if string_input == '':
				continue
			user_input = int(string_input)

			if user_input == 0:
				pass

			if user_input == 1:
				self._store.menu_process_web_orders(factory)
			elif user_input == 2:
				inv.display_inventory()
			elif user_input == 3:
				pass
			elif user_input == 4:
				inv.inventory_test(items)
			elif user_input == 5:
				inv.inventory_test2(factory)
			else:
				print("Could not process the input. Please enter a number from 1 - 3.")
		print("Thank you for visiting the store.")
