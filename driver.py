"""
# TODO: Add title and description

# Name1: Nash Baek (nash4comp@gmail.com)
# Student number1: A01243888

# Name2: Taylor Ji (taylor.ji719@gmail.com)
# Student number2: A01304056

UML diagram: https://app.diagrams.net/#G18MWO3bp974lfK4Ceehz2vUfH8YmqEEfE
"""

from store_front import StoreFront
import inventory
import gift_factory


def main():
	inv = inventory.Inventory()
	test_store_front = StoreFront()
	factory = gift_factory.GiftFactory()
	test_store_front.display_menu(inv, factory)


if __name__ == '__main__':
	main()
