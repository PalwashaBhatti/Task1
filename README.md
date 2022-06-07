# task1

''' This function will make a POST request to the specified url with the specified parameters in data : dictionary object'''
     
     def make_request
	
	
	''' If the valid request made (200), then displaying the hash '''
	if r.status_code == 200:
		''' Converting the data into a parse-able format for the hmac function: '''
		enc_data = json.dumps(data, indent=2).encode('utf-8')


		''' Calculating the HMAC '''
		enc_body = hmac.new(
....
		print data

def main():

