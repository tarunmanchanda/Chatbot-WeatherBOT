import json

data = {}  
data['current'] = []  
data['current'].append({  
    'countryLocation': 'France',
    'cityLocation': 'Paris',
    'region': 'EU',
	'temp_c': 23,
	'humidity': 87,
	'wind_mph': 9.4,
	'condition': 'Partly Cloudy'
})
data['current'].append({  
    'countryLocation': 'Italy',
    'cityLocation': 'Rome',
    'region': 'EU',
	'temp_c': 11,
	'humidity': 100,
	'wind_mph': 0,
	'condition': 'Partly Cloudy'
})
data['current'].append({  
    'countryLocation': 'Netherlands',
    'cityLocation': 'Amsterdam',
    'region': 'EU',
	'temp_c': 8,
	'humidity': 93,
	'wind_mph': 10.4,
	'condition': 'Light Rain Shower'
})

with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)
