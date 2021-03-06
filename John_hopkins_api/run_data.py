import requests
from matplotlib import pyplot as plt
import numpy as np
import datetime as dt
import matplotlib.dates as mdates
# normally called SpellChecker but had to move into file to edit code for my use
import better_spell_check as bsc
import time
from tkinter import *

# Extracting data from txt files
f = open("D:\Python_Github\John_hopkins_api\some_countries.txt","r")
my_dict = eval(f.readline())
f.close()
f = open("D:\Python_Github\John_hopkins_api\slugs.txt","r")
my_slugs_list = eval(f.readline())
f.close()

#taking in input from user
"""
my_input = input("Give a Country you want to look up: ")
my_country = bsc.spell_checker(my_input)
print(my_country)
my_slug = my_slugs_list[my_dict.index(my_country)]
"""

country_input_window = Tk()
country_input_window.geometry("250x150")
country_input_window.title("Country")
country_entry = Entry(country_input_window)
country_label = Label(country_input_window,text="Give a Country you want to look up: ")
country_entry.place(x=35,y=50)
country_label.place(x=25,y=10)
def country_exit():
    human_spelling = str(country_entry.get())
#    print(human_spelling)
    global my_country
    my_country = bsc.spell_checker(human_spelling)
#    print(my_country)
    global my_slug
    my_slug = my_slugs_list[my_dict.index(my_country)]
    country_input_window.destroy()

    # gathering data from api based on country
    data_window = Tk()
    data_window.title("Deaths/recovered/confirmed")
    global my_choice
    my_choice = 0
    def my_deaths():
        data_window.destroy()
        next("deaths")
    def my_recovered():
        data_window.destroy()
        next("recovered")
    def my_confirmed():
        x = 5
        data_window.destroy()
        next("deaths")
    deaths = Button(data_window,text="Deaths",command = my_deaths)
    recovered = Button(data_window,text="recovered",command = my_recovered)
    confirmed = Button(data_window,text="confirmed",command = my_confirmed)
    deaths.pack()
    recovered.pack()
    confirmed.pack()
    data_window.mainloop()
def next(my_choice):
    url = "https://api.covid19api.com/total/dayone/country/" +  my_slug + "/status/" + my_choice
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    response_json = response.json()

    #organizing my data
    my_data = []
    my_sum = 0
    my_dates = []
    for Date in response_json:
        my_dates.append(Date['Date'])
        my_data.append(Date["Cases"]-my_sum)
        my_sum += (Date["Cases"] - my_sum)

    # changing the dates to a readable and useable format
    x = []
    for d in my_dates:
        x.append(dt.datetime.strptime(d[0:10],'%Y-%m-%d').date())

    #creating a seven-day-sum
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

    # Setting up graph properties and displaying
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval = 14))
    seven_day_sum_graph = plt.plot(x,seven_day_sum, color = "red", Label = "7 day sum")
    my_display = plt.bar(x,my_data,1, Label = "Daily Charts")
#    plt.tight_layout()
    plt.gcf().autofmt_xdate()
    plt.title(f"{my_country}",pad=1.0)
    plt.show()
    #f = open("D:\Python_Github\John_hopkins_api\my_testing.txt","w")
    #f.write(str(response_json))
Button(country_input_window,command = country_exit,text="Done",font=("Times New Roman",15)).place(x = 75, y= 100)
country_input_window.mainloop()
