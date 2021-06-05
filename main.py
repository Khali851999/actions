import urllib, json

url  = "https://raw.githubusercontent.com/Khali851999/actions/main/t.json"
response = urllib.urlopen(url)
req = response.read()
data = json.loads(req.decode("utf-8"))
print (data)

with open("Readme.md") as file:
    file.write(data['x'])