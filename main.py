import urllib.request, json

url  = "https://raw.githubusercontent.com/Khali851999/actions/main/t.json"
response = urllib.request.urlopen(url)
req = response.read()
data = json.loads(req.decode("utf-8"))
print (data)

with open("Readme.md", 'w') as file:
    file.write(str(data['x']))