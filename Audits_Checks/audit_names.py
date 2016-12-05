import xml.etree.cElementTree as ET

sol = set()

for _,element in ET.iterparse('philadelphia_pennsylvania.osm'):
	if element.tag == 'way':
		for x in element:
			try:
				k = x.attrib['k']
				if k == 'name':
					if len(x.attrib['v'].split(' ')) > 1 :
						sol.add(x.attrib['v'].split(' ')[-1])
			except KeyError:
				pass

print(sol)
