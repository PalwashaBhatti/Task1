# -*- coding: utf-8 -*-
"""Task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gu7MV9UBafJagFhdhonY3M8eVB6HNBoU
"""

#!/usr/bin/env python3

import requests
from datetime import datetime
from hashlib import sha256
import hmac
import json

''' This function will make a POST request to the specified url with the specified parameters in data : dictionary object'''
def make_request(
	url : str,
	data : dict
):
	
	''' Making the actual request '''
	r = requests.post(
		url,
		data = data,
	)

	''' If the valid request made (200), then displaying the hash '''
	if r.status_code == 200:
		''' Converting the data into a parse-able format for the hmac function: '''
		enc_data = json.dumps(data, indent=2).encode('utf-8')

		''' Key for the hmac '''
		key = b"V3RyS7r0nGK3y"

		''' Calculating the HMAC '''
		enc_body = hmac.new(
			key=key,
			msg=enc_data,
			digestmod = sha256
		).hexdigest()

		print(f"Data sent: {enc_body}")
	else:
		print("Bad Request:")
		print(
			f"[{data['client_id']}]_[{data['timestamp']}]: [{data['description']}]"
		)


def main():


	''' Specify the following parameters '''
	url = "https://studios.sapphireapps.com/ct/q1"
	client_id = "125"
	media_url = "None"
	description = "This is a very strong test description for the python program."
	timestamp = str(datetime.now()) # This will fetch the current time.

	''' The data that will be sent with the post request. '''
	data = {
		"client_id" : client_id,
		"media_url" : media_url,
		"timestamp" : timestamp,
		"description" : description
	}

	# Making the actual request.
	make_request(
		url = url,
		data = data
	)

if __name__ == "__main__":
	main()