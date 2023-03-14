import abc
from abc import ABC


class GiftFactory(ABC):
	def __init__(self):
		pass

	@staticmethod
	def classify_item(theme, item, num):
		if theme == 'Christmas':
			cf = ChristmasGiftFactory()
			cf.create_item(item, num)
		elif theme == 'Halloween':
			hf = HalloweenGiftFactory()
			hf.create_item(item, num)
		elif theme == 'Easter':
			ef = EasterGiftFactory()
			ef.create_item(item, num)


class ChristmasGiftFactory(GiftFactory):

	def create_item(self, item, num):
		if item == 'Toys':
			self.create_toy(num)
		elif item == 'Stuffed_animal':
			self.create_stuffed_animal(num)
		elif item == 'Candy':
			self.create_candy(num)

	def create_toy(self, num):
		print("Christmas toy created: " + str(num) + " toys created")

	def create_stuffed_animal(self, num):
		print("Christmas stuffed animal created: " + str(num) + " stuffed animals created")

	def create_candy(self, num):
		print("Christmas candy created: " + str(num) + " candies created")


class HalloweenGiftFactory(GiftFactory):
	def create_item(self, item, num):
		if item == 'Toys':
			self.create_toy(num)
		elif item == 'Stuffed_animal':
			self.create_stuffed_animal(num)
		elif item == 'Candy':
			self.create_candy(num)

	def create_toy(self, num):
		print("Halloween toy created: " + str(num) + " toys created")

	def create_stuffed_animal(self, num):
		print("Halloween stuffed animal created: " + str(num) + " stuffed animals created")

	def create_candy(self, num):
		print("Halloween candy created: " + str(num) + " candies created")


class EasterGiftFactory(GiftFactory):
	def create_item(self, item, num):
		if item == 'Toys':
			self.create_toy(num)
		elif item == 'Stuffed_animal':
			self.create_stuffed_animal(num)
		elif item == 'Candy':
			self.create_candy(num)

	def create_toy(self, num):
		print("Easter toy created: " + str(num) + " toys created")

	def create_stuffed_animal(self, num):
		print("Easter stuffed animal created: " + str(num) + " stuffed animals created")

	def create_candy(self, num):
		print("Easter candy created: " + str(num) + " candies created")


class Product(ABC):
	def __init__(self, name, description, pid, theme):
		self._name = name
		self._description = description
		self._pid = pid
		self._theme = theme

	def __str__(self):
		return "Product"


class Toy(Product):
	def __init__(self, name, description, pid, theme, is_battery_operated, min_age):
		super().__init__(name, description, pid, theme)
		self._is_battery_operated = is_battery_operated
		self._min_age = min_age

	def __str__(self):
		return "Toy"


class SantasWorkshop(Toy):
	def __init__(self, name, description, pid, theme, is_battery_operated, min_age, width, height, num_of_rooms):
		super().__init__(name, description, pid, theme, is_battery_operated, min_age)
		self._width = width
		self._height = height
		self._num_of_rooms = num_of_rooms

	def __str__(self):
		return "SantasWorkshop"


class RCSpider(Toy):
	def __init__(self, name, description, pid, theme, is_battery_operated, min_age, speed, jump_height, is_glowing,
	             spider_type):
		super().__init__(name, description, pid, theme, is_battery_operated, min_age)
		self._speed = speed
		self._jump_height = jump_height
		self._is_glowing = is_glowing
		self._spider_type = spider_type

	def __str__(self):
		return "RCSpider"


class RobotBunny(Toy):
	def __init__(self, name, description, pid, theme, is_battery_operated, min_age, num_of_sound_effects, color):
		super().__init__(name, description, pid, theme, is_battery_operated, min_age)
		self._num_of_sound_effects = num_of_sound_effects
		self._color = color

	def __str__(self):
		return "RobotBunny"
