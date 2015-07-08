import requests
import urllib2
import xml.etree
import base64

import rest_helper

class VCloudDriver:
	"""
	An API driver for accessing the various services of VCloud Air On Demand
	 
	"""
    def __init__(self,username):
		self.username = username
		self.basic_authorization = ""
		self.xvcloud_authorization = ""

	def encode(organization,password):
		encoded_text = self.username + "@" + organization + ":" + password
		return base64.b64encode(encoded_text)

	def login(self,organization,password):
		"""
		Login to VCA on demand service and get the OAuth Token

		"""
		url = "https://us-virginia-1-4.vchs.vmware.com/api/compute/api/sessions" 
		headers = rest_helper.buildHeaders(Accept="application/*+xml;version=5.11",Authorization="Basic "+encode(organization,password))
		response = requests.post(url, headers=headers)
		return response.headers["x-vcloud-authorization"]

		

		





