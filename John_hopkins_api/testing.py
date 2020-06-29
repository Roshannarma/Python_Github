import requests
from matplotlib import pyplot as plt
import numpy as np
import datetime as dt
import matplotlib.dates as mdates
import better_spell_check as bsc
import time
f = open("D:\Python_Github\John_hopkins_api\some_countries.txt","r")
my_dict = eval(f.readline())
f.close()
my_input = input("Give a Country you want to look up: ")
f = open("D:\Python_Github\John_hopkins_api\slugs.txt","r")
my_slugs_list = eval(f.readline())
f.close()
#mytime = time.time()
my_country = bsc.spell_checker(my_input)
#print(time.time()-mytime)
print(my_country)
my_slug = my_slugs_list[my_dict.index(my_country)]
#print(my_slug)
url = "https://api.covid19api.com/total/dayone/country/" +  my_slug + "/status/confirmed"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)
response_json = response.json()
my_data = []
my_sum = 0
my_dates = []
for Date in response_json:
    my_dates.append(Date['Date'])
    my_data.append(Date["Cases"]-my_sum)
    my_sum += (Date["Cases"] - my_sum)

#    '2020-03-15T00:00:00Z'
x = []
for d in my_dates:
    x.append(dt.datetime.strptime(d[0:10],'%Y-%m-%d').date())
#print(x)
seven_day_sum = []
length = len(my_data)
for location in range(0,length):
    if location <= 3:
        seven_day_sum_temp = sum(my_data[0:location+3])
        seven_day_sum.append(seven_day_sum_temp/len(my_data[0:location+3]))
    elif location + 3 >= length:
        seven_day_sum_temp = sum(my_data[location-3:])
        seven_day_sum.append(seven_day_sum_temp/(length-(location-3)))
    else:
        seven_day_sum_temp = sum(my_data[location-3:location+4])
        seven_day_sum.append(seven_day_sum_temp/7)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval = 14))
#index_line = np.arange(len(seven_day_sum))
#index = np.arange(len(my_data))
seven_day_sum_graph = plt.plot(x,seven_day_sum, color = "red", Label = "7 day sum")
my_display = plt.bar(x,my_data,1, Label = "Daily Charts")
plt.tight_layout()
plt.gcf().autofmt_xdate()
plt.show()
#f = open("D:\Python_Github\John_hopkins_api\my_testing.txt","w")
#f.write(str(response_json))
