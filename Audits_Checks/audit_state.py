import xml.etree.cElementTree as ET
from collections import defaultdict

x = defaultdict(lambda : 0)
for _,element in ET.iterparse('philadelphia_pennsylvania.osm'):	
	for tag in element:
		attr = tag.attrib
		try:
			if(attr['k']=='addr:state'):
				x[attr['v']] = x[attr['v']] + 1
		except KeyError:
			pass
	if element.tag == 'member':
		break

print(x)

