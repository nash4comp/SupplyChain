def display_menu():
	user_input = None
	while user_input != 3:
		print("Welcome to the store")
		print("1. Process web orders")
		print("2. Check inventory")
		print("3. Exit")
		string_input = input("Please enter a number from 1 - 3\n> ")

		if string_input == '':
			continue
		user_input = int(string_input)
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
