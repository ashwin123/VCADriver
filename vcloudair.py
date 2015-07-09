import requests
import urllib2
import xml.etree
import base64

import rest_helper
import xml_helper

class VCloudDriver:
	"""
	An API driver for accessing the various services of VCloud Air On Demand
	 
	"""
    def __init__(self,username,organization):
		self.username = username
		self.organization = organization
		self.xvcloud_authorization = ""
		self.baseCloudXML="";

	def _encode(password):
		encoded_text = self.username + "@" + self.organization + ":" + password
		return base64.b64encode(encoded_text)

	def login(self,password):
		"""
		Login to VCA on demand service and get the OAuth Token

		"""
		url = "https://us-virginia-1-4.vchs.vmware.com/api/compute/api/sessions" 
		headers = rest_helper.buildHeaders(Accept="application/*+xml;version=5.11",Authorization="Basic "+_encode(self.organization,password))
		response = requests.post(url, headers=headers)
		self.baseCloudXML=response.content;
		self.xvcloud_authorization = response.headers["x-vcloud-authorization"]
	
	def getOrganisation(self):
		"""
		Retrieve XML representation of the organization

		"""
		url = xml_helper.getHref(baseCloudXML,'orgList')
		headers = rest_helper.buildHeaders(Accept="application/*+xml;version=5.11",x-vcloud-authorization=xvcloud_authorization)
		response = requests.get(url, headers=headers)
		return response.content
		
	def getCatalog(self):
		"""
		Retrieve XML representation of the organization

		"""
		url = xml_helper.getHref(self.getOrganisation(),'catalog')
		headers = rest_helper.buildHeaders(Accept="application/*+xml;version=5.11",x-vcloud-authorization=xvcloud_authorization)
		response = requests.get(url, headers=headers)
		return response.content
		
	def getCatalogItem(self):
		"""
		Retrieve XML representation of the organization

		"""
		url = xml_helper.getHref(self.getCatalog(),'catalogItem')
		headers = rest_helper.buildHeaders(Accept="application/*+xml;version=5.11",x-vcloud-authorization=xvcloud_authorization)
		response = requests.get(url, headers=headers)
		return response.content
			
	def getVDC(self):
		"""
		Retrieve XML representation of the organization

		"""
		url = xml_helper.getHref(self.getOrganisation,'vdc')
		headers = rest_helper.buildHeaders(Accept="application/*+xml;version=5.11",x-vcloud-authorization=xvcloud_authorization)
		response = requests.get(url, headers=headers)
		return response.content
		
	def getVappTemplate(self)
		return xml_helper.getHref(self.getVDC(),'instantiateVAppTemplateParams')
	def deployVapp(self,name):
		url = xml_helper.getHref(self.getCatalog(),'catalogItem')
		headers = rest_helper.buildHeaders(Accept="application/*+xml;version=5.11",x-vcloud-authorization=xvcloud_authorization)
		response = requests.get(url, headers=headers)
		return response.content

	def deploy_vApp(self,name):







		

		





