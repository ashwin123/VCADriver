import requests
from xml.etree import ElementTree
import urllib2
import xml.etree
import base64

import rest_helper

def _encode(password):
	encoded_text = "ashwin.naresh94@gmail.com@c8cad1b3-4f3e-459a-b515-3b29de47add4@:" + password
	return base64.b64encode(encoded_text)

def login(password):
	"""
		Login to VCA on demand service and get the OAuth Token

	"""
	url = "https://us-virginia-1-4.vchs.vmware.com/api/compute/api/sessions" 
	headers = rest_helper.buildHeaders(Accept="application/*+xml;version=5.11",Authorization="Basic "+_encode(password))
	response = requests.post(url, headers=headers)
	#xvcloud_authorization = response.headers["x-vcloud-authorization"]
	print(response)
	tree = ElementTree.fromstring(response.content)
#login("Hybridcloud1@vmare")
f=open("login.txt","w")
f.write(_encode("Hybridcloud1@vmare"))
