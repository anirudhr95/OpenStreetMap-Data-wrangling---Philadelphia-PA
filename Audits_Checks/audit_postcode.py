import xml.etree.cElementTree as ET
from collections import defaultdict
import re
def process_values(value):
	code =  (re.findall(r'\d+',value))
	code = ''.join(code)
	code = code[0:5]
	if(code.startswith('1')):
		return int(code.strip())
	return None
x = defaultdict(lambda : 0)
for _,element in ET.iterparse('philadelphia_pennsylvania.osm'):	
	for tag in element:
		attr = tag.attrib
		try:
			if(attr['k']=='addr:postcode'):
				x[attr['v']] = x[attr['v']] + 1
		except KeyError:
			pass
	if element.tag == 'member':
		break


values = x.keys()
for i,item in enumerate(values):
	values[i] = process_values(item)

filter(None,values)
print(values)

"""
[None, None, '19134', '19446', None, None, None, None, None, None, '19006', '198
10', None, '19014', '19015', '19016', '19010', '19012', '19013', '19018', None,
'19317', '198039997', '19314', '19312', '190873696', None, '19406', '19405', '19
151', '19150', '19401', '19152', None, '19468', '19464', '19703', None, '19460',
 None, '19462', None, None, None, None, None, None, None, '19061', '19060', '190
63', '19064', '19067', '19066', '19380', '18966', '19382', '19105', '190733299',
 '19301', '190103224', '19148', '19149', '19146', '19147', '19144', '19145', u'1
9147', '19143', '19140', '19141', None, '19478', '19477', '19474', None, '19473'
, '19154', '18969', '19078', '19072', '19073', '19070', '19076', '19074', '1719'
, '19079', '18974', None, '18976', None, None, None, None, None, '19355', '19443
', '193121239', '19440', '19446', '19444', '191489996', None, '18956', None, '19
1042989', '18964', '18954', '19047', '19046', None, '19044', '190411228', '19041
', '19020', '19050', '18929', None, '18901', '18194', None, '19341', '19342', '1
9153', '190969998', '19111', '19112', '19115', '19114', '19116', '19119', '19118
', '19052', '19053', '19054', '19055', '19057', None, None, None, None, None, No
ne, None, None, '18914', None, None, '19129', None, None, '19333', None, None, N
one, '19407', None, None, None, None, '19135', '19102', '19103', '19106', '19107
', '19104', None, '19403', None, None, '19454', None, None, '19029', '19153', No
ne, '19025', None, '19027', None, None, '18925', '19083', '19082', '19081', '190
87', '19086', '19085', None, '1723', '191543131', '189440', None, None, '19040',
 '19142', '18936', '19139', '19138', '19137', '19136', None, '19134', '19133', '
19132', '19131', '19130', None, None, '19422', None, '19038', '19426', '19036',
'19428', '19034', '19035', '19033', '19030', '19031', '1713', None, '19095', '19
096', None, '19090', None, '19720', '19803', '19802', '19801', '19806', None, '1
9456', None, '19809', None, '19438', '19128', '18940', '19120', '19121', '19122'
, '19123', '19124', '19125', '19126', '19127', None, None, '19008', '19428', Non
e, None, '19003', '19002', '19001', '190304005', '19007', None, None, '19004']
"""