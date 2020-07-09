import pandas as pd
import requests
from bs4 import BeautifulSoup
res = requests.get("https://www.fiscal.treasury.gov/reports-statements/treasury-reporting-rates-exchange/current.html")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0]
df = pd.read_html(str(table))
mylist = df[0].to_json(orient='records')
new_list_of_dictionary = []
currency_names = {}
for x in eval(mylist):
    my_temp_dict = {}
    my_temp_list = x['Country - Currency'].split("-")
    my_temp_dict['Country'] = my_temp_list[0]
    if my_temp_list[1] in currency_names.keys():
        currency_names[my_temp_list[1]] += ", " + my_temp_list[0]
    else:
        currency_names[my_temp_list[1]] = my_temp_list[0]
    my_temp_dict['Currency'] = my_temp_list[1]
    my_temp_dict['Exchange rate'] = x['Foreign Currency to $1.00']
    new_list_of_dictionary.append(my_temp_dict)
with open("D:\Python_Github\currency_exchanger\my_new_data.txt","w") as f:
    f.write(str(new_list_of_dictionary)+"\n"+str(currency_names))
