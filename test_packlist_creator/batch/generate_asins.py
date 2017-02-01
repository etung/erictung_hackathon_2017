import random
import json
categories = ["Meat", "Produce", "Laundry","Appliances"]

asins = []
for x in xrange (0,200) :
   asins.append( {
   "asin":"B" + str(random.randint(100000,999999)),
   "category":categories[random.randint(0,len(categories)-1)]})
  
print json.dumps(asins)
