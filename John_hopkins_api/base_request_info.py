import requests

url = "https://api.covid19api.com/countries"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
response_json = response.json()
#print(response_json)
#f = open("D:\Python_Github\John_hopkins_api\data.txt","wb")
#f.write(response.text.encode('utf8'))
actual_country = []
slugs = []
for country in response_json:
    actual_country.append(country["Country"])
    slugs.append(country["Slug"])
f = open("D:\Python_Github\John_hopkins_api\slugs.txt","w")
f.write(str(slugs))
f.close()
f = open("D:\Python_Github\John_hopkins_api\countries.txt","w")
f.write(str(actual_country))
f.close()

#make basic auto-correct for countries
