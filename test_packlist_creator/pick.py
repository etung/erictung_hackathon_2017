from objects.packlist import PackList
from objects.inventory import MerchantInventory
import random

DEFAULT_PACKED_ITEMS = 20

def getPacklistFromJson (inventory_json, random_items_to_pack = DEFAULT_PACKED_ITEMS) :
	inventory = MerchantInventory(inventory_json)

	packlist = PackList()
	for x in xrange(random.randint(6, random_items_to_pack)) :
		item = inventory.get_random_item()
		packlist.pack(item["asin"], item["category"])

	return packlist.get_list_contents()
