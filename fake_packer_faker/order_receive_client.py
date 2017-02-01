import requests
import json

GET_ORDER_URL = 'http://c4b301d7d229.ant.amazon.com:5000/packlist_creator/api/v1.0/get_order' 
CREATE_ORDER_URL = 'http://c4b301d7d229.ant.amazon.com:5000/packlist_creator/api/v1.0/create_order' 

def getMultipleOrders(orders) :
	resp = requests.post(CREATE_ORDER_URL, json = {'count':orders})
	if resp.status_code != 201:
	    # This means something went wrong.
	    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
	return resp.json()

def getOrder() :
	resp = requests.get(GET_ORDER_URL)
	if resp.status_code != 201:
	    # This means something went wrong.
	    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
	return resp.json()

if __name__ == "__main__" :
	print getOrder()
	print getMultipleOrders()
