import ijson
from urllib.request import urlopen

with open('./tinyTwitter.json') as f:
	rows = ijson.items(f, 'rows.item.value')
	for row in rows:
		print(type(row))
		# print(row['properties']['text'])
		row['geometry']['coordinates'][0]
		row['geometry']['coordinates'][1]


