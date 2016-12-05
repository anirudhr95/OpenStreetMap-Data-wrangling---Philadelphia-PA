import xml.etree.cElementTree as ET
import re
from collections import defaultdict
x = defaultdict(lambda : 0)

def process_item(item):
	value = item
	if ' ' in item:
		value = value.replace(' ','-')
	if '(' in item:
		value = value.replace('(','')
	if ')' in item:
		value = value.replace(')','')
	if '+' in item:
		value = value.replace('+','')
	value = value.strip()
	value = re.sub(r'\b'+ '1' + r'\b','', value).strip()
	if(value.startswith('-')):
		value = value.replace('-','',1)
	return value.strip()


count = 0 
for _,element in ET.iterparse('philadelphia_pennsylvania.osm'):	
	if element.tag=='way':
		for tag in element:
			attr = tag.attrib
			try:
				if(attr['k'] == 'phone'):
					x[attr['v']] = x[attr['v']] + 1
			except KeyError:
				pass
	if element.tag=='member':
		break

#print(x)
phone_numbers = x.keys()

for i,item in enumerate(phone_numbers):
	phone_numbers[i] = process_item(item)

print(phone_numbers)



# if element.tag == 'tag' :
	# 	for tag in element:
	# 		value = tag.attrib
	# 		if(values['k']=='phone'):
	# 			print(values['v']) 
	#This produced nothing , meaning only way tags have a phone key!