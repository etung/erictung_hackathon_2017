import json
import random

class MerchantInventory :
	def __init__ (self, inventory_json) :
		self.inventory = json.loads(inventory_json)

	def get_random_item (self) :
		return self.inventory[random.randint(0, len(self.inventory) - 1)]