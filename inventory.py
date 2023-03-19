import gift_factory as gf


class Inventory:
	def __init__(self):
		# self._inventory_toy = [gf.SantasWorkshop(), gf.RCSpider(), gf.RobotBunny()]
		# self._inventory_stuffed_animal = [gf.DancingSkeleton(), gf.Reindeer(), gf.EasterBunny()]
		# self._inventory_candy = [gf.PumpkinCaramelToffee(), gf.CandyCanes(), gf.CreamEggs()]
		self._inventory_toy = []
		self._inventory_stuffed_animal = []
		self._inventory_candy = []

	def check_inventory(self, quantity):
		if quantity >= 10:
			return "In Stock"
		elif 10 > quantity >= 3:
			return "Low"
		elif 3 > quantity > 0:
			return "Very Low"
		else:
			return "Out of Stock"

	def add_item(self, item, product_name, quantity, theme):
		if item == "Toy":
			if theme == gf.Theme.Christmas:
				self._inventory_toy.append(gf.SantasWorkshop())
			elif theme == gf.Theme.Halloween:
				self._inventory_toy.append(gf.RCSpider())
			elif theme == gf.Theme.Easter:
				self._inventory_toy.append(gf.RobotBunny())
		elif item == "StuffedAnimal":
			if theme == gf.Theme.Christmas:
				self._inventory_stuffed_animal.append(gf.DancingSkeleton())
			elif theme == gf.Theme.Halloween:
				self._inventory_stuffed_animal.append(gf.Reindeer())
			elif theme == gf.Theme.Easter:
				self._inventory_stuffed_animal.append(gf.EasterBunny())
		elif item == "Candy":
			if theme == gf.Theme.Christmas:
				self._inventory_candy.append(gf.PumpkinCaramelToffee())
			elif theme == gf.Theme.Halloween:
				self._inventory_candy.append(gf.CandyCanes())
			elif theme == gf.Theme.Easter:
				self._inventory_candy.append(gf.CreamEggs())

	def inventory_test(self):
		self._inventory_toy[0].set_name("Nash's Toy")
		self._inventory_toy[0].set_quantity(15)
		self._inventory_toy[1].set_name("Taylor's SW")
		self._inventory_toy[1].set_quantity(5)
		self._inventory_toy[2].set_name("Jeff's RC Spider")
		self._inventory_toy[2].set_quantity(2)

	def display_inventory(self):
		print("Inventory List")
		print("<Toys>")
		for item in self._inventory_toy:
			print(item.get_product_type() + ", " + item.get_name() + ", " + str(item.get_quantity()) +
			      ", " + self.check_inventory(item.get_quantity()))
		print("\n<Stuffed Animals>")
		for item in self._inventory_stuffed_animal:
			print(item.get_product_type() + ", " + item.get_name() + ", " + str(item.get_quantity()) +
			      ", " + self.check_inventory(item.get_quantity()))
		print("\n<Candy>")
		for item in self._inventory_candy:
			print(item.get_product_type() + ", " + item.get_name() + ", " + str(item.get_quantity()) +
			      ", " + self.check_inventory(item.get_quantity()))
		print("\n")
