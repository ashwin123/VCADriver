import requests
import urllib2
import xml.etree

class VCloudDriver:
	"""
	An API driver for accessing the various services of VCloud Air On Demand
	 
	"""
    def __init__(self,username=username,password=password):
		self.username = username;
		self.password = password;
		self.basic_authorization = "";
		self.xvcloud_authorization = "";

	def login(self):
		pass

		





