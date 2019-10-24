import json

def readFile(location):
	#loc = 'France'
		with open('data.txt') as json_file:
			data = json.load(json_file)
			for result in data['current']:
				#print('Country Name:' + result['countryLocation'])
				if result['countryLocation'] == location or result['cityLocation'] == location:
					print('country Found')
					country = result['countryLocation']
					city = result['cityLocation']
					condition = result['condition']
					temperature_c = result['temp_c']
					humidity = result['humidity']
					wind_mph = result['wind_mph']
					break
		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
		print(response)
				
				
if __name__ == '__main__':
	loc = 'Paris'
	readFile(loc)