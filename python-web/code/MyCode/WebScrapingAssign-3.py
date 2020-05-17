import urllib.request,urllib.parse,urllib.error
import json

url = input("Enter Url - ");

data = urllib.request.urlopen(url).read().decode()
data = json.loads(data)
comment = data["comments"]
sum = 0
for temp in comment:
    sum+=temp["count"]
print(sum)