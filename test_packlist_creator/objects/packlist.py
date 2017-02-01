'''packlistModel = {
    'orderId' : 'ORDER-ID',
    'asinList' :
    [
        {
        'asin' : 'ASIN1',
        'category' : 'Fruits'
    },
    {
        'asin' : 'ASIN2',
        'category' : 'Diary'
    }
]
}
'''
from sets import Set
import json
import random

def createUniqueList (packlist_asins) :
	category_asin_dict = {}
	for asin_cat_entry in packlist_asins :
		if not (asin_cat_entry["category"] in category_asin_dict) :
			category_asin_dict[asin_cat_entry["category"]] = Set([])
		category_asin_dict[asin_cat_entry["category"]].add(
				asin_cat_entry["asin"])

	output_list = []
	for category in category_asin_dict :
		for asin in  category_asin_dict[category]:
			output_list.append({
				"asin":asin,
				"category":category
				})
	return output_list

def pprintJson (json_value) :
	print json.dumps(json_value, sort_keys=True,
                 indent=4, separators=(',', ': '))


class PackList :
	def __init__(self):
   		self.data = {}
   		self.data["orderId"] = str(random.randint(100000,999999))
   		self.data["asinList"] = []

	def _set_OrderId(self, order_id) :
		self.data["orderId"] = order_id

	def pack (self, asin, category = "Dairy") :
		data_input = {"asin":asin,"category":category}
		self.data["asinList"].append(data_input)
		self.data["asinList"] = createUniqueList(self.data["asinList"])

	def _dump_asin_list (self) :
		return self.data["asinList"]

	def _dump_packlist (self) :
		return self.data

	def print_packlist (self) :
		return pprintJson(self._dump_packlist())

	def get_list_contents(self) :
		return self.data


def testItemsPacking () :
	packlist = PackList()
	packlist.pack("ASIN1", "Produce")
	packlist.pack("ASIN1", "Produce")
	packlist.pack("ASIN2", "Produce")
	packlist.pack("ASIN3", "Meat")
	packlist.pack("ASIN4", "Cleaning Supplies")
	packlist.pack("ASIN5", "Appliances")
	packlist.pack("ASIN6", "Cleaning Supplies")
	packlist.pack("ASIN7", "Appliances")
	#packlist.pack("ASIN7", "Produce")

	packlist.print_packlist()
	print packlist.get_list_contents()

def testUnique() :

	pre_unique = [
	        {
	        'asin' : 'ASIN1',
	        'category' : 'Fruits'
	    },
	    {
	        'asin' : 'ASIN2',
	        'category' : 'Diary'
	    },
        {
	        'asin' : 'ASIN1',
	        'category' : 'Fruits'
	    }
	]
	post_unique = [
		        {
	        'asin' : 'ASIN1',
	        'category' : 'Fruits'
	    },
	    {
	        'asin' : 'ASIN2',
	        'category' : 'Diary'
	    }
    ]
	print createUniqueList(pre_unique)
	if createUniqueList(pre_unique) != post_unique :
		print "Test Failed"
   	else :
		print "Test Passed"

# Basic test
if __name__ == "__main__" :
	testUnique()
	testItemsPacking()
