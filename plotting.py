import plotly
from pymongo import MongoClient
import plotly.graph_objs as go
import plotly.plotly as py
#from plotly.graph_objs import Scatter, Layout


def return_top_five(field):
	pipe = list()
	f = '$' + field
	pipe.append({'$match' : {field : {'$exists' : 1}}})
	pipe.append({'$group' : {'_id' : f ,'count' : {'$sum' : 1}}})
	pipe.append({'$sort' : {'count' : -1}})
	pipe.append({'$limit' : 5})
	return pipe

client = MongoClient('mongodb://localhost:27017/')
db = client['philly']
collection = db['data']

pipe = list()
pipe = return_top_five('leisure')

result = db.command('aggregate','data',pipeline = pipe)
leisure = dict()				
for x in result['result']:
	leisure[x['_id']] = x['count']
print(leisure)
values_list = (sorted(leisure.values()))
keys_list = list()

for keys in leisure.keys():
	for item in values_list:
		if leisure[keys] == item:
			keys_list.append(keys)

data = [go.Bar(x = keys_list , y = values_list)]
py.iplot(data, filename='basic-bar')