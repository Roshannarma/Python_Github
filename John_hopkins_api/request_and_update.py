import requests
import re
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
"""
f = open("D:\Python_Github\John_hopkins_api\countries.txt","w")
f.write(str(actual_country))
f.close()
"""
#make basic auto-correct for countries
pattern = re.compile("[A-Za-z0-9 ]+")
english_name = {"C":"cote d'ivoire", "R":"reunion","S":"saint barthelemy"}
korea_china_dict = {"Korea (North)":"north korea","Korea (South)":"south korea","Hong Kong, SAR China":"hong kong","Macao, SAR China":"macao","Macedonia, Republic of":"macedonia","Guinea-Bissau":"guniea bissau","Micronesia, Federated States of":"micronesia","Virgin Islands, US":"virgin islands","Iran, Islamic Republic of":"iran","Timor-Leste":"timor leste","Taiwan, Republic of China":"taiwan","Tanzania, United Republic of":"tanzania"}
my_dict = actual_country
for x in range(0,len(my_dict)):
    if my_dict[x] in korea_china_dict.keys():
        my_dict[x] = korea_china_dict[my_dict[x]]
    elif "(" in my_dict[x]:
        location = my_dict[x].index("(")
        my_dict[x] = (my_dict[x][0:location-1]).lower()
    elif pattern.fullmatch(my_dict[x]) is None:
        print(my_dict[x])
        my_dict[x] = english_name[my_dict[x][0]]
    else:
        my_dict[x] = my_dict[x].lower()
f.close()
f = open("D:\Python_Github\John_hopkins_api\some_countries.txt","w")
f.write(str(my_dict))
f.close()
