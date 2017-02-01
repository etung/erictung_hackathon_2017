import order_receive_client
import time
import random
import json

TEST_TIME = time.time()

def increment_and_add_time (TEST_TIME) :
	TEST_TIME = TEST_TIME + random.random() * 500
	return TEST_TIME

def pack_fake (order_json) :
	TEST_TIME = time.time()
	order = json.loads(order_json)
	order["packlistStartTimeEpoch"] = TEST_TIME
	for item in order["asinList"] :
		item["pickTimeEpoch"] = increment_and_add_time(TEST_TIME)
	order["packlistEndTimeEpoch"] = increment_and_add_time(TEST_TIME)
	order["TimeToPack"] = order["packlistEndTimeEpoch"] - order["packlistStartTimeEpoch"]
	return order

def get_time_diffs (order_json) :
	order = json.loads(order_json)
	last_time = order["packlistStartTime"]
	times = []
	order["asinList"] = sorted(order["asinList"], key=lambda item: item["pickTime"])
	for item in order["asinList"] :
		times.append(item["pickTime"] - last_time)
		last_time = item["pickTime"]

	for time in times :
		print "Pick time for item" ,time
	print "Total Time:", (order["packlistEndTime"] - order["packlistStartTime"])

if __name__ == "__main__" :
	result = pack_fake (order_receive_client.getOrder())
	#print json.dumps(result , sort_keys=True,                
	#	 indent=4, separators=(',', ': '))

	get_time_diffs(json.dumps(result))

	result = pack_fake (json.dumps(result))
	#print json.dumps(result , sort_keys=True,                
	#	 indent=4, separators=(',', ': '))

	get_time_diffs(json.dumps(result))