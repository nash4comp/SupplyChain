import gift_factory as gf


class Inventory:
	def __init__(self):
		self._inventory_toy = [gf.Toy(), gf.SantasWorkshop(), gf.RCSpider(), gf.RobotBunny()]
		self._inventory_stuffed_animal = [gf.StuffedAnimal(), gf.DancingSkeleton(), gf.Reindeer(), gf.EasterBunny()]
		self._inventory_candy = [gf.Candy(), gf.PumpkinCaramelToffee(), gf.CandyCanes(), gf.CreamEggs()]

	def check_inventory(self, quantity):
		if quantity >= 10:
			return "In Stock"
		elif 10 > quantity >= 3:
			return "Low"
		elif 3 > quantity > 0:
			return "Very Low"
		else:
			return "Out of Stock"

	def inventory_test(self):
		self._inventory_toy[0].set_name("Nash's Toy")
		self._inventory_toy[0].set_quantity(15)
		self._inventory_toy[1].set_name("Taylor's SW")
		self._inventory_toy[1].set_quantity(5)
		self._inventory_toy[2].set_name("Jeff's RC Spider")
		self._inventory_toy[2].set_quantity(2)
		self._inventory_toy[3].set_name("Mark's RobotBunny")
		self._inventory_toy[3].set_quantity(0)

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
