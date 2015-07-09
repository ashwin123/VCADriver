"""
Module which helps find elements inside xml response

"""
from xml.etree import ElementTree as ET

def getHref(xmlText,key):
	root = EL.fromstring(xmlText)
	for EL in root:
		t = EL.get('type')
		#print(t)
		#print(str(t.find(key+'+xml')))
		if t.find(key+'+xml') != -1:
			return EL.get('href')
	return 'not Found'