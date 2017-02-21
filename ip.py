import requests as r
import json
#g = r.get('http://122.181.186.42:9200')
g = r.get('http://122.181.186.42:9200/aishu')
json_str = g.text
json_dict = json.dumps(json_str)
print json_dict
#g = r.post('http://122.181.186.42:9200/aishu',{'name':'aishu'}) 
#print g.text


print  json_st
