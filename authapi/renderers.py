#Custom JSON Renderer for user responses
#This renderer is designed to handle the serialization of response data, ensuring a 
#consistent JSON format .
#It specifically addresses cases where the response data includes 'ErrorDetail' object.

from rest_framework import renderers
import json

class UserRenderer(renderers.JSONRenderer):
	#Set the charset for the JSON response
	charset = 'utf-8'
	def render(self, data, accepted_media_type=None, renderer_context=None):
		response = ''
		#check if the response data contains 'ErrorDetail' objects
		if 'ErrorDetail' in str(data):
			#if there are errors format them in errors key
			response = json.dumps({'errors':data})
		else:
			#if no errors, simply format the data as JSON
			response = json.dumps(data)

