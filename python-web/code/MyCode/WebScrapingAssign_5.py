import urllib.request,urllib.error,urllib.parse;
import json

url = "http://py4e-data.dr-chuck.net/json?"
address = input("Enter Address");
params = dict()
params['address'] = address
params['key'] = 42
address_url = url + urllib.parse.urlencode(params)
print(address_url)
data = urllib.request.urlopen(address_url).read().decode()

json_data = json.loads(data)
print(json_data['results'][0]['place_id'])

