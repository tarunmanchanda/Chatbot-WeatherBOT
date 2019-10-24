# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:02:32 2019

@author: Hp
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import json

class ActionWeather(Action):
	def name(self):
		print('in self method')
		return 'action_weather'
	
	# def readFile(location):
	# #loc = 'France'
		# with open('data.txt') as json_file:
			# data = json.load(json_file)
			# for result in data['current']:
				# #print('Country Name:' + result['countryLocation'])
				# if result['countryLocation'] == location or result['cityLocation'] == location:
					# print('country Found')
					# country = result['countryLocation']
					# city = result['cityLocation']
					# condition = result['condition']
					# temperature_c = result['temp_c']
					# humidity = result['humidity']
					# wind_mph = result['wind_mph']
					# break
		# response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
		# print(response)
		# return response
		
	def run(self, dispatcher, tracker, domain):
		print('in run method')
		loc = ''
		loc = tracker.get_slot('location')
		print(loc)
		response = ''
		with open('data.txt') as json_file:
			data = json.load(json_file)
			for result in data['current']:
				print('Country Name:' + result['countryLocation'])
				if result['countryLocation'].lower() == loc.lower() or result['cityLocation'].lower() == loc.lower():
					print('country Found')
					country = result['countryLocation']
					city = result['cityLocation']
					condition = result['condition']
					temperature_c = result['temp_c']
					humidity = result['humidity']
					wind_mph = result['wind_mph']
					response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition,city, temperature_c, humidity, wind_mph)
					print(response)
				elif():
					response = """ Country or city location is not available"""
					print(response)
                
		dispatcher.utter_message(response)
		loc = ''
		return [SlotSet('location',loc)]
		
	
	# def readFile(location):
	# #loc = 'France'
		# with open('data.txt') as json_file:
			# data = json.load(json_file)
			# for result in data['current']:
				# #print('Country Name:' + result['countryLocation'])
				# if result['countryLocation'] == location or result['cityLocation'] == location:
					# print('country Found')
					# country = result['countryLocation']
					# city = result['cityLocation']
					# condition = result['condition']
					# temperature_c = result['temp_c']
					# humidity = result['humidity']
					# wind_mph = result['wind_mph']
					# break
		# response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
		# print(response)
		# return response
