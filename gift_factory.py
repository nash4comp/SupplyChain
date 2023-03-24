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

import abc
from abc import ABC
from enum import Enum


class Products(Enum):
	"""
	This class is an enum that contains all the products that the store sells.
	"""

	class Toy(Enum):
		"""
		This class is an enum that contains all the toy products that the store sells.
		"""
		SantasWorkshop = 1
		RCSpider = 2
		RobotBunny = 3

	class StuffedAnimal(Enum):
		"""
		This class is an enum that contains all the stuffed animal products that the store sells.
		"""
		DancingSkeleton = 1
		Reindeer = 2
		EasterBunny = 3

	class Candy(Enum):
		"""
		This class is an enum that contains all the candy products that the store sells.
		"""
		PumpkinCaramelToffee = 1
		CandyCanes = 2
		CreamEggs = 3


class Holiday(Enum):
	"""
	This class is an enum that contains all the holidays that the store sells products for.
	"""
	Christmas = 1
	Halloween = 2
	Easter = 3


class SpiderType(Enum):
	"""
	This class is an enum that contains all the spider types that the store sells.
	"""
	Tarantula = 1
	WolfSpider = 2


class Colour(Enum):
	"""
	This class is an enum that contains all the colours that the store sells.
	"""
	Orange = 1
	Blue = 2
	Pink = 3
	White = 4
	Grey = 5


class Stuffing(Enum):
	"""
	This class is an enum that contains all the stuffing types that the store sells.
	"""
	Polyester_Fibrefill = 1
	Wool = 2


class Size(Enum):
	"""
	This class is an enum that contains all the sizes that the store sells.
	"""
	S = 1
	M = 2
	L = 3


class Fabric(Enum):
	"""
	This class is an enum that contains all the fabric types that the store sells.
	"""
	Linen = 1
	Cotton = 2
	Acrylic = 3


class PumpkinCaramelVariety(Enum):
	"""
	This class is an enum that contains all the pumpkin caramel toffee varieties that the store sells.
	"""
	Sea_Salt = 1
	Regular = 2


class CandyCanesStrips(Enum):
	"""
	This class is an enum that contains all the candy cane strip types that the store sells.
	"""
	Red = 1
	Green = 2


class GiftFactory:
	"""
	This class is a factory that creates products for the store front.
	"""

	@staticmethod
	def create_item(**kwargs):
		"""
		This method creates a product based on the item type and holiday.
		:param kwargs: item details
		:return: class object
		"""
		item_type = kwargs["item_type"]
		del kwargs["item_type"]
		if kwargs["holiday"] == Holiday.Christmas.name:
			if item_type == "Toy":
				return SantasWorkshop(**kwargs)
			elif item_type == "StuffedAnimal":
				return Reindeer(**kwargs)
			elif item_type == "Candy":
				return CandyCanes(**kwargs)
		elif kwargs["holiday"] == Holiday.Halloween.name:
			if item_type == "Toy":
				return RCSpider(**kwargs)
			elif item_type == "StuffedAnimal":
				return DancingSkeleton(**kwargs)
			elif item_type == "Candy":
				return PumpkinCaramelToffee(**kwargs)
		elif kwargs["holiday"] == Holiday.Easter.name:
			if item_type == "Toy":
				return RobotBunny(**kwargs)
			elif item_type == "StuffedAnimal":
				return EasterBunny(**kwargs)
			elif item_type == "Candy":
				return CreamEggs(**kwargs)


class Product(ABC):
	"""
	This class is the parent class for all products.
	"""

	def __init__(self, item_type=None, quantity=0, name='No name', description='', product_id='', holiday=None):
		"""
		This method initializes the product class.
		:param item_type: item type
		:param quantity: quantity of the item
		:param name: name of the item
		:param description: description of the item
		:param product_id: product id of the item
		:param holiday: type of holiday
		"""
		self._item_type = item_type
		self._quantity = quantity
		self._name = name
		self._description = description
		self._product_id = product_id
		self._holiday = holiday

	def __str__(self):
		"""
		This method returns the string representation of the product.
		:return: the string representation of the product
		"""
		return "Product"

	def set_quantity(self, quantity):
		"""
		This method sets the quantity of the product.
		:param quantity: the quantity of the product to be set
		:return: the quantity of the product
		"""
		if quantity < 0:
			raise ValueError("Quantity cannot be negative")
		self._quantity = quantity

	def initial_process(self, initial_order_count):
		"""
		TODO: Add comments
		:param initial_order_count:
		:return:
		"""
		initial_count = 100
		processed_count = initial_count - initial_order_count
		self.set_quantity(processed_count)

	def add_quantity(self, quantity):
		"""
		TODO: Add comments
		:param quantity:
		:return:
		"""
		if quantity < 0:
			raise ValueError("Quantity cannot be negative")
		self._quantity = self.get_quantity() + quantity

	def subtract_quantity(self, quantity):
		"""
		TODO: Add comments
		:param quantity:
		:return:
		"""
		if quantity < 0:
			raise ValueError("Quantity cannot be negative")
		self._quantity = self.get_quantity() - quantity

	def set_name(self, name):
		"""
		This method sets the name of the product.
		:param name: the name of the product to be set
		:return: the name of the product
		"""
		self._name = name

	def get_quantity(self):
		"""
		This method returns the quantity of the product.
		:return: the quantity of the product
		"""
		return self._quantity

	def get_name(self):
		"""
		This method returns the name of the product.
		:return: the name of the product
		"""
		return self._name

	def get_product_id(self):
		"""
		This method returns the product id of the product.
		:return: the product id of the product
		"""
		return self._product_id

	@abc.abstractmethod
	def get_item_type(self):
		"""
		This is abstract method that returns the item type of the product.
		"""
		pass


class Toy(Product):
	"""
	This class is a child class of the Product class.
	"""

	@staticmethod
	def validate_attribute(attribute_dict):
		"""
		Validate toy's common attributes.
		:param attribute_dict: dictionary that has all the information required to create an item.
		"""
		valid_attributes_toy = {"quantity": 0, "description": "", "has_batteries": False, "min_age": 0}
		valid_attribute_count = 0
		for attribute in valid_attributes_toy.keys():
			if attribute in attribute_dict.keys():
				if attribute == "quantity" and type(attribute_dict[attribute]) == int:
					valid_attributes_toy["quantity"] = attribute_dict[attribute]
					valid_attribute_count += 1
				if attribute == "description" and attribute_dict[attribute] is not None:
					valid_attributes_toy["description"] = attribute_dict[attribute]
					valid_attribute_count += 1
				if attribute == "has_batteries":
					if attribute_dict["has_batteries"] == "N":
						valid_attributes_toy["has_batteries"] = False
						valid_attribute_count += 1
					elif attribute_dict["has_batteries"] == "Y":
						valid_attributes_toy["has_batteries"] = True
						valid_attribute_count += 1
					else:
						print("Invalid battery input")
					# valid_attributes_toy["has_batteries"] = attribute_dict[attribute]
				if attribute == "min_age" and type(attribute_dict[attribute]) == float:
					int_age = int(attribute_dict[attribute])
					valid_attributes_toy["min_age"] = int_age
					valid_attribute_count += 1
		if valid_attribute_count != len(valid_attributes_toy):
			print("Invalid order")
		else:
			return valid_attributes_toy

	def __init__(self, item_type='TOY', quantity=0, name='No name', description='', product_id='', holiday=None,
	             has_batteries=False,
	             min_age=0):
		"""
		This method initializes the toy class.
		:param item_type: the item type
		:param quantity: the quantity of the item
		:param name: the name of the item
		:param description: the description of the item
		:param product_id: the product id of the item
		:param holiday: the type of holiday
		:param has_batteries: the boolean value that indicates whether the toy has batteries or not
		:param min_age: the minimum age of the toy
		"""
		super().__init__(item_type, quantity, name, description, product_id, holiday)
		self._item_type = item_type
		self._has_batteries = has_batteries
		self._min_age = min_age

	def get_item_type(self):
		"""
		This method returns the item type of the product.
		:return: the item type of the product
		"""
		return self._item_type

	def __str__(self):
		"""
		This method returns the string representation of the toy class.
		:return: the string representation of the toy class
		"""
		return "Toy"


class SantasWorkshop(Toy):
	"""
	This class is a child class of the Toy class.
	"""

	@staticmethod
	def santa_detail_validator(att_dict):
		"""
		Validate Santa's attributes.
		:param att_dict: dictionary that has all the information required to create Santa Workshop.
		"""
		valid_santa_attributes = {"dimension": "", "num_rooms": 0}
		for key_att_dict in att_dict.keys():
			if key_att_dict == "dimensions":
				valid_santa_attributes["dimension"] = att_dict[key_att_dict]
			if key_att_dict == "num_rooms" and type(att_dict[key_att_dict]) != str:
				int_room_num = int(att_dict[key_att_dict])
				valid_santa_attributes["num_rooms"] = int_room_num
		if valid_santa_attributes["dimension"] == "" \
			or valid_santa_attributes["num_rooms"] == 0:
			return None
		else:
			return valid_santa_attributes

	def __init__(self, item_type='TOY', quantity=0, name='No name', description='', product_id='', holiday=None,
	             has_batteries=False, min_age='', dimension="", num_rooms=0):
		"""
		This method initializes the SantasWorkshop class.
		:param item_type: the item type
		:param quantity: the quantity of the item
		:param name: the name of the item
		:param description: the description of the item
		:param product_id: the product id of the item
		:param holiday: the type of holiday
		:param has_batteries: the boolean value that indicates whether the toy has batteries or not
		:param min_age: the minimum age of the toy
		:param dimension: the dimension of the toy
		:param num_rooms: the number of rooms in the toy
		"""
		super().__init__(item_type, quantity, name, description, product_id, holiday, has_batteries, min_age)
		self._dimension = dimension
		self._num_rooms = num_rooms

	def get_item_type(self):
		"""
		This method returns the item type of the product.
		:return: the item type of the product
		"""
		return self._item_type

	def __str__(self):
		"""
		This method returns the string representation of the SantasWorkshop class.
		:return: the string representation of the SantasWorkshop class
		"""
		ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
		      str(self.get_quantity()) + ", Name: " + self.get_name()
		return ret


class RCSpider(Toy):
	"""
	This class is a child class of the Toy class.
	"""

	@staticmethod
	def rc_spider_detail_validator(att_dict):
		"""
		Validate RC Spider's attributes.
		:param att_dict: dictionary that has all the information required to create RC Spider.
		"""

		valid_attribute_count = 0
		valid_spider_attributes = {"speed": 0, "jump_height": 0, "has_glow": "", "spider_type": ""}
		for key_att_dict in att_dict.keys():
			if key_att_dict == "speed" and att_dict[key_att_dict] != str:
				int_speed = int(att_dict[key_att_dict])
				valid_spider_attributes["speed"] = int_speed
				valid_attribute_count += 1
			if key_att_dict == "jump_height" and type(att_dict[key_att_dict]) != str:
				int_jump = int(att_dict[key_att_dict])
				valid_spider_attributes["jump_height"] = int_jump
				valid_attribute_count += 1
			if key_att_dict == "has_glow":
				if att_dict["has_glow"] == "N":
					valid_spider_attributes["has_glow"] = False
					valid_attribute_count += 1
				elif att_dict["has_glow"] == "Y":
					valid_spider_attributes["has_glow"] = True
					valid_attribute_count += 1
				else:
					print("Invalid glow input")
			if key_att_dict == "spider_type":
				if att_dict["spider_type"] == "Tarantula":
					valid_spider_attributes["spider_type"] = "Tarantula"
					valid_attribute_count += 1
				elif att_dict["spider_type"] == "Wolf Spider":
					valid_spider_attributes["spider_type"] = "Wolf Spider"
					valid_attribute_count += 1
				else:
					print("Invalid spider type input")
		if valid_spider_attributes["speed"] == 0 \
				or valid_spider_attributes["jump_height"] == 0 \
				or valid_spider_attributes["has_glow"] == "" \
				or valid_spider_attributes["spider_type"] == "":
			return None
		else:
			return valid_spider_attributes

	def __init__(self, item_type='TOY', quantity=0, name='No name', description='', product_id='', holiday=None,
	             has_batteries=False,
	             min_age=0, speed=0, jump_height=0, has_glow=False, spider_type=None):
		"""
		This method initializes the RCSpider class.
		:param item_type: the item type
		:param quantity: the quantity of the item
		:param name: the name of the item
		:param description: the description of the item
		:param product_id: the product id of the item
		:param holiday: the type of holiday
		:param has_batteries: the boolean value that indicates whether the toy has batteries or not
		:param min_age: the minimum age of the toy
		:param speed: the speed of the spider
		:param jump_height: the jump height of the spider
		:param has_glow: the boolean value that indicates whether the spider has glow or not
		:param spider_type: the type of the spider
		"""
		super().__init__(item_type, quantity, name, description, product_id, holiday, has_batteries, min_age)
		self._speed = speed
		self._jump_height = jump_height
		self._has_glow = has_glow
		self._spider_type = spider_type

	def get_item_type(self):
		"""
		This method returns the item type of the product.
		:return: the item type of the product
		"""
		return self._item_type

	def __str__(self):
		"""
		This method returns the string representation of the RCSpider class.
		:return: the string representation of the RCSpider class
		"""
		ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
		      str(self.get_quantity()) + ", Name: " + self.get_name()
		return ret


class RobotBunny(Toy):
	"""
	This class is a child class of the Toy class.
	"""

	@staticmethod
	def robot_bunny_detail_validator(att_dict):
		"""
		Validate Robot bunny's attributes.
		:param att_dict: dictionary that has all the information required to create Robot bunny.
		"""
		valid_attribute_count = 0
		valid_robot_bunny_details = {"num_sound": 0, "colour": ""}
		for key_att_dict in att_dict.keys():
			value_from_dict = att_dict[key_att_dict]
			if key_att_dict == "num_sound" and type(att_dict[key_att_dict]) != str:
				int_num_sound = int(att_dict[key_att_dict])
				valid_robot_bunny_details["num_sound"] = int_num_sound
				valid_attribute_count += 1
			if key_att_dict == "colour":
				# Orange, Blue, Pink
				if key_att_dict == "colour":
					if value_from_dict == "Orange":
						valid_robot_bunny_details["colour"] = "Orange"
					if value_from_dict == "Blue":
						valid_robot_bunny_details["colour"] = "Blue"
					if value_from_dict == "Pink":
						valid_robot_bunny_details["colour"] = "Pink"
				valid_attribute_count += 1
		if valid_robot_bunny_details["num_sound"] == 0 \
				or valid_robot_bunny_details["colour"] == "":
			return None
		else:
			return valid_robot_bunny_details

	def __init__(self, item_type='TOY', quantity=0, name='No name', description='', product_id='', holiday=None,
	             has_batteries=False, min_age=0, num_sound=0, colour=None):
		"""
		This method initializes the RobotBunny class.
		:param item_type: the item type
		:param quantity: the quantity of the item
		:param name: the name of the item
		:param description: the description of the item
		:param product_id: the product id of the item
		:param holiday: the type of holiday
		:param has_batteries: the boolean value that indicates whether the toy has batteries or not
		:param min_age: the minimum age of the toy
		:param num_sound: the number of sound effects
		:param colour: the colour of the robot bunny
		"""
		super().__init__(item_type, quantity, name, description, product_id, holiday, has_batteries, min_age)
		self._num_of_sound_effects = num_sound
		self._color = colour

	def get_item_type(self):
		"""
		This method returns the item type of the product.
		:return:
		"""
		return self._item_type

	def __str__(self):
		"""
		This method returns the string representation of the RobotBunny class.
		:return: the string representation of the RobotBunny class
		"""
		ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
		      str(self.get_quantity()) + ", Name: " + self.get_name()
		return ret


class StuffedAnimal(Product):
	"""
	This class is a child class of the Product class.
	"""
	@staticmethod
	def validate_attribute(attribute_dict):
		"""
		Validate Robot bunny's attributes.
		:param attribute_dict: dictionary that has all the information required to create Stuffed Animal.
		"""
		valid_attributes_stuffed_animal = {"quantity": 0, "description": "", "stuffing": "", "size": ""}
		valid_attribute_count = 0
		for attribute in valid_attributes_stuffed_animal.keys():
			if attribute in attribute_dict.keys():
				if attribute == "quantity" and type(attribute_dict[attribute]) == int:
					valid_attributes_stuffed_animal["quantity"] = attribute_dict[attribute]
					valid_attribute_count += 1
				if attribute == "description" and attribute_dict[attribute] is not None:
					valid_attributes_stuffed_animal["description"] = attribute_dict[attribute]
					valid_attribute_count += 1
				if attribute == "stuffing":
					if attribute_dict["stuffing"] == "Polyester Fibrefill":
						valid_attributes_stuffed_animal["stuffing"] = "Polyester Fibrefill"
						valid_attribute_count += 1
					elif attribute_dict["stuffing"] == "Wool":
						valid_attributes_stuffed_animal["stuffing"] = "Wool"
						valid_attribute_count += 1
					else:
						print("Invalid stuffing input")
				if attribute == "size":
					if attribute_dict["size"] == "S":
						valid_attributes_stuffed_animal["size"] = "S"
						valid_attribute_count += 1
					elif attribute_dict["size"] == "M":
						valid_attributes_stuffed_animal["size"] = "M"
						valid_attribute_count += 1
					elif attribute_dict["size"] == "L":
						valid_attributes_stuffed_animal["size"] = "L"
						valid_attribute_count += 1
					else:
						print("Invalid size input")
		return valid_attributes_stuffed_animal

	def __init__(self, item_type='StuffedAnimal', quantity=0, name='No name', description='', product_id='',
	             holiday=None, stuffing=None, size=None, fabric=None):
		"""
		This method initializes the StuffedAnimal class.
		:param item_type: the item type
		:param quantity: the quantity of the item
		:param name: the name of the item
		:param description: the description of the item
		:param product_id: the product id of the item
		:param holiday: the type of holiday
		:param stuffing: the stuffing of the stuffed animal
		:param size: the size of the stuffed animal
		:param fabric: the fabric of the stuffed animal
		"""
		super().__init__(item_type, quantity, name, description, product_id, holiday)
		self._stuffing = stuffing
		self._size = size
		self._fabric = fabric

	def get_item_type(self):
		"""
		This method returns the item type of the product.
		:return: the item type of the product
		"""
		return self._item_type

	def __str__(self):
		"""
		This method returns the string representation of the StuffedAnimal class.
		:return: the string representation of the StuffedAnimal class
		"""
		ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
		      str(self.get_quantity()) + ", Name: " + self.get_name()
		return ret


class DancingSkeleton(StuffedAnimal):
	"""
	This class is a child class of the StuffedAnimal class.
	"""
	@staticmethod
	def dancing_skeleton_detail_validator(att_dict):
		"""
		Validate Dancing Skeleton's attributes.
		:param attribute_dict: dictionary that has all the information required to create Dancing Skeleton.
		"""
		# valid_attributes_count = 6
		# if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
		#     # print("extra column dancing monkey")
		#     return None
		valid_dancing_skeleton_attributes = {"fabric": "", "has_glow": ""}
		for key_att_dict in att_dict.keys():
			value_from_dict = att_dict[key_att_dict]
			if key_att_dict == "fabric":
				if value_from_dict == "Linen":
					valid_dancing_skeleton_attributes["fabric"] = "Linen"
				if value_from_dict == "Cotton":
					valid_dancing_skeleton_attributes["fabric"] = "Cotton"
				if value_from_dict == "Acrylic":
					valid_dancing_skeleton_attributes["fabric"] = "Acrylic"
			if key_att_dict == "has_glow":
				if value_from_dict == "N":
					valid_dancing_skeleton_attributes["has_glow"] = False
				elif value_from_dict == "Y":
					valid_dancing_skeleton_attributes["has_glow"] = True
				else:
					print("Invalid fabric")
		if valid_dancing_skeleton_attributes["fabric"] == "" \
				or valid_dancing_skeleton_attributes["has_glow"] == "":
			return None
		else:
			return valid_dancing_skeleton_attributes

	def __init__(self, item_type='StuffedAnimal', quantity=0, name='No name', description='', product_id='',
	             holiday=None, stuffing=None, size=None, fabric=None, has_glow=False):
		"""
		This method initializes the DancingSkeleton class.
		:param item_type: the item type
		:param quantity: the quantity of the item
		:param name: the name of the item
		:param description: the description of the item
		:param product_id: the product id of the item
		:param holiday: the type of holiday
		:param stuffing: the stuffing of the stuffed animal
		:param size: the size of the stuffed animal
		:param fabric: the fabric of the stuffed animal
		:param has_glow: the boolean value of whether the dancing skeleton has glow
		"""
		super().__init__(item_type, quantity, name, description, product_id, holiday, stuffing, size, fabric)
		self._has_glow = has_glow

	def __str__(self):
		"""
		This method returns the string representation of the DancingSkeleton class.
		:return: the string representation of the DancingSkeleton class
		"""
		ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
		      str(self.get_quantity()) + ", Name: " + self.get_name()
		return ret


class Reindeer(StuffedAnimal):
	"""
	This class is a child class of the StuffedAnimal class.
	"""

	@staticmethod
	def rein_deer_detail_validator(att_dict):
		"""
		Validate Reindeer's attributes.
		:param att_dict: dictionary that has all the information required to create  Reindeer.
		"""
		valid_reindeer_attributes = {"fabric": "", "has_glow": ""}
		for key_att_dict in att_dict.keys():
			value_from_dict = att_dict[key_att_dict]
			if key_att_dict == "fabric":
				if value_from_dict == "Linen":
					valid_reindeer_attributes["fabric"] = "Linen"
				if value_from_dict == "Cotton":
					valid_reindeer_attributes["fabric"] = "Cotton"
				if value_from_dict == "Acrylic":
					valid_reindeer_attributes["fabric"] = "Acrylic"
			if key_att_dict == "has_glow":
				if value_from_dict == "N":
					valid_reindeer_attributes["has_glow"] = False
				elif value_from_dict == "Y":
					valid_reindeer_attributes["has_glow"] = True
				else:
					print("Invalid glow")
		if valid_reindeer_attributes["fabric"] == "" \
				or valid_reindeer_attributes["has_glow"] == "":
			return None
		else:
			return valid_reindeer_attributes

	def __init__(self, item_type='StuffedAnimal', quantity=0, name='No name', description='', product_id='',
	             holiday=None, stuffing=None, size=None, fabric=None, has_glow=False):
		"""
		This method initializes the Reindeer class.
		:param item_type: the item type
		:param quantity: the quantity of the item
		:param name: the name of the item
		:param description: the description of the item
		:param product_id: the product id of the item
		:param holiday: the type of holiday
		:param stuffing: the stuffing of the stuffed animal
		:param size: the size of the stuffed animal
		:param fabric: the fabric of the stuffed animal
		:param has_glow: the boolean value of whether the reindeer has glow
		"""
		super().__init__(item_type, quantity, name, description, product_id, holiday, stuffing, size, fabric)
		self._has_glow = has_glow

	def __str__(self):
		"""
		This method returns the string representation of the Reindeer class.
		:return: the string representation of the Reindeer class
		"""
		ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
		      str(self.get_quantity()) + ", Name: " + self.get_name()
		return ret


class EasterBunny(StuffedAnimal):
	@staticmethod
	def east_bunny_detail_validator(att_dict):
		"""
		Validate Easter Bunny's attributes.
		:param att_dict: dictionary that has all the information required to create Easter Bunny.
		"""
		valid_reindeer_attributes = {"fabric": "", "colour": ""}
		for key_att_dict in att_dict.keys():
			value_from_dict = att_dict[key_att_dict]
			if key_att_dict == "fabric":
				if value_from_dict == "Linen":
					valid_reindeer_attributes["fabric"] = "Linen"
				if value_from_dict == "Cotton":
					valid_reindeer_attributes["fabric"] = "Cotton"
				if value_from_dict == "Acrylic":
					valid_reindeer_attributes["fabric"] = "Acrylic"
			if key_att_dict == "colour":
				if value_from_dict == "Orange":
					valid_reindeer_attributes["colour"] = "Orange"
				if value_from_dict == "Blue":
					valid_reindeer_attributes["colour"] = "Blue"
				if value_from_dict == "Pink":
					valid_reindeer_attributes["colour"] = "Pink"
				if value_from_dict == "White":
					valid_reindeer_attributes["colour"] = "White"
				if value_from_dict == "Grey":
					valid_reindeer_attributes["colour"] = "Grey"
		if valid_reindeer_attributes["fabric"] == "" \
				or valid_reindeer_attributes["colour"] == "":
			return None
		else:
			return valid_reindeer_attributes

	def __init__(self, item_type='StuffedAnimal', quantity=0, name='No name', description='', product_id='',
	             holiday=None, stuffing=None, size=None, fabric=None, colour=None):
		"""
		This method initializes the EasterBunny class.
		:param item_type: the item type
		:param quantity: the quantity of the item
		:param name: the name of the item
		:param description: the description of the item
		:param product_id: the product id of the item
		:param holiday: the type of holiday
		:param stuffing: the stuffing of the stuffed animal
		:param size: the size of the stuffed animal
		:param fabric: the fabric of the stuffed animal
		:param colour: the colour of the stuffed animal
		"""
		super().__init__(item_type, quantity, name, description, product_id, holiday, stuffing, size, fabric)
		self._color = colour

	def __str__(self):
		"""
		This method returns the string representation of the EasterBunny class.
		:return: the string representation of the EasterBunny class
		"""
		ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
		      str(self.get_quantity()) + ", Name: " + self.get_name()
		return ret


class Candy(Product):
	"""
	This class represents the Candy class.
	"""

	@staticmethod
	def validate_attribute(attribute_dict):
		"""
		Validate Candy's common attributes.
		:param attribute_dict: dictionary that has all the information required to create Candy.
		"""
		valid_attributes_candy = {"quantity": 0, "description": "", "has_nuts": "", "has_lactose": ""}
		valid_attribute_count = 0
		for attribute in valid_attributes_candy.keys():
			if attribute in attribute_dict.keys():
				if attribute == "quantity" and type(attribute_dict[attribute]) == int:
					valid_attributes_candy["quantity"] = attribute_dict[attribute]
					valid_attribute_count += 1
				if attribute == "description" and attribute_dict[attribute] is not None:
					valid_attributes_candy["description"] = attribute_dict[attribute]
					valid_attribute_count += 1
				if attribute == "has_nuts":
					if attribute_dict["has_nuts"] == "N":
						valid_attributes_candy["has_nuts"] = False
						valid_attribute_count += 1
					elif attribute_dict["has_nuts"] == "Y":
						valid_attributes_candy["has_nuts"] = True
						valid_attribute_count += 1
					else:
						print("Invalid has_nuts input")
				if attribute == "has_lactose":
					if attribute_dict["has_lactose"] == "N":
						valid_attributes_candy["has_lactose"] = False
						valid_attribute_count += 1
					elif attribute_dict["has_lactose"] == "Y":
						valid_attributes_candy["has_lactose"] = True
						valid_attribute_count += 1
					else:
						print("Invalid has_lactose input")
		return valid_attributes_candy

	def __init__(self, item_type='Candy', quantity=0, name='No name', description='', product_id='', holiday=None,
	             has_nuts=False, has_lactose=False):
		"""
		This method initializes the Candy class.
		:param item_type: the item type
		:param quantity: the quantity of the item
		:param name: the name of the item
		:param description: the description of the item
		:param product_id: the product id of the item
		:param holiday: the type of holiday
		:param has_nuts: the has_nuts attribute
		:param has_lactose: the has_lactose attribute
		"""
		super().__init__(item_type, quantity, name, description, product_id, holiday)
		self._contains_nuts = has_nuts
		self._is_lactose_free = has_lactose

	def get_item_type(self):
		"""
		This method returns the item type.
		:return: the item type
		"""
		return self._item_type

	def __str__(self):
		"""
		This method returns the string representation of the Candy class.
		:return: the string representation of the Candy class
		"""
		ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
		      str(self.get_quantity()) + ", Name: " + self.get_name()
		return ret


class PumpkinCaramelToffee(Candy):
	"""
	This class represents the Pumpkin Caramel Toffee class.
	"""
	@staticmethod
	def pumpkin_toffee_detail_validator(att_dict):
		"""
		Validate Pumpkin Caramel Toffee's attributes.
		:param att_dict: dictionary that has all the information required to create  Pumpkin Caramel Toffee.
		"""
		# valid_attributes_count = 5
		# if len(att_dict.keys()) != valid_attributes_count:  # filter extra column
		#     # print("extra column")
		#     return None
		valid_halloween_candy_attributes = {"variety": ""}
		for key_att_dict in att_dict.keys():
			value_from_dict = att_dict[key_att_dict]
			if key_att_dict == "variety":
				if value_from_dict == "Sea Salt":
					valid_halloween_candy_attributes["variety"] = value_from_dict
				if value_from_dict == "Regular":
					valid_halloween_candy_attributes["variety"] = value_from_dict
		if valid_halloween_candy_attributes["variety"] == "":
			return None
		else:
			return valid_halloween_candy_attributes

	def __init__(self, item_type='Candy', quantity=0, name='No name', description='', product_id='', holiday=None,
	             has_nuts=False, has_lactose=False, variety=''):
		"""
		This method initializes the Pumpkin Caramel Toffee class.
		:param item_type: the item type
		:param quantity: the quantity of the item
		:param name: the name of the item
		:param description: the description of the item
		:param product_id: the product id of the item
		:param holiday: the type of holiday
		:param has_nuts: the has_nuts attribute
		:param has_lactose: the has_lactose attribute
		:param variety: the variety of the Pumpkin Caramel Toffee
		"""
		super().__init__(item_type, quantity, name, description, product_id, holiday, has_nuts, has_lactose)
		self._variety = variety

	def __str__(self):
		"""
		This method returns the string representation of the Pumpkin Caramel Toffee class.
		:return: the string representation of the Pumpkin Caramel Toffee class
		"""
		ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
		      str(self.get_quantity()) + ", Name: " + self.get_name()
		return ret


class CandyCanes(Candy):
	"""
	This class represents the Candy Canes class.
	"""

	@staticmethod
	def candy_cane_detail_validator(att_dict):
		"""
		Validate Pumpkin Candy Cane's attributes.
		:param att_dict: dictionary that has all the information required to create Candy Cane.
		"""
		valid_candy_cane_attributes = {"colour": ""}
		for key_att_dict in att_dict.keys():
			value_from_dict = att_dict[key_att_dict]
			if key_att_dict == "colour":
				if value_from_dict == "Red":
					valid_candy_cane_attributes["colour"] = value_from_dict
				if value_from_dict == "Green":
					valid_candy_cane_attributes["colour"] = value_from_dict
		if valid_candy_cane_attributes["colour"] == "":
			return None
		else:
			return valid_candy_cane_attributes

	def __init__(self, item_type='Candy', quantity=0, name='No name', description='', product_id='', holiday=None,
	             has_nuts=False, has_lactose=False, colour=None):
		"""
		This method initializes the Candy Canes class.
		:param item_type: the item type
		:param quantity: the quantity of the item
		:param name: the name of the item
		:param description: the description of the item
		:param product_id: the product id of the item
		:param holiday: the type of holiday
		:param has_nuts: the has_nuts attribute
		:param has_lactose: the has_lactose attribute
		:param colour: the colour of the Candy Canes
		"""
		super().__init__(item_type, quantity, name, description, product_id, holiday, has_nuts, has_lactose)
		self._strips = colour

	def __str__(self):
		"""
		This method returns the string representation of the Candy Canes class.
		:return: the string representation of the Candy Canes class
		"""
		ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
		      str(self.get_quantity()) + ", Name: " + self.get_name()
		return ret


class CreamEggs(Candy):
	"""
	This class represents the Pumpkin Cream Egg class.
	"""

	@staticmethod
	def cream_egg_detail_validator(att_dict):
		"""
		Validate Pumpkin Cream Egg's attributes.
		:param att_dict: dictionary that has all the information required to create Cream Egg.
		"""
		valid_cream_egg_attributes = {"pack_size": ""}
		for key_att_dict in att_dict.keys():
			value_from_dict = att_dict[key_att_dict]
			if key_att_dict == "pack_size" and type(value_from_dict) != str:
				int_pack_size = int(value_from_dict)
				valid_cream_egg_attributes["pack_size"] = int_pack_size
		if valid_cream_egg_attributes["pack_size"] == "":
			return None
		else:
			return valid_cream_egg_attributes

	def __init__(self, item_type='Candy', quantity=0, name='No name', description='', product_id='', holiday=None,
	             has_nuts=False, has_lactose=False, pack_size=0):
		"""
		This method initializes the Cream Eggs class.
		:param item_type: the item type
		:param quantity: the quantity of the item
		:param name: the name of the item
		:param description: the description of the item
		:param product_id: the product id of the item
		:param holiday: the type of holiday
		:param has_nuts: the has_nuts attribute
		:param has_lactose: the has_lactose attribute
		:param pack_size: the pack size of the Cream Eggs
		"""
		super().__init__(item_type, quantity, name, description, product_id, holiday, has_nuts, has_lactose)
		self._pack_size = pack_size

	def __str__(self):
		"""
		This method returns the string representation of the Cream Eggs class.
		:return: the string representation of the Cream Eggs class
		"""
		ret = "Item: " + self.get_item_type() + ", PID: " + self.get_product_id() + ", Qty: " + \
		      str(self.get_quantity()) + ", Name: " + self.get_name()
		return ret
