from xml.etree import ElementTree as ET

tree = ET.parse('tes1.xml')
root = tree.getroot()
def getRef(root,key):
	for EL in root:
		t=EL.get('type')
		#print(t)
		#print(str(t.find(key+'+xml')))
		if t.find(key+'+xml') != -1:
			return EL.get('href')
	return 'not Found'
print(getRef(root,'orgList'))