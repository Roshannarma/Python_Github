from tkinter import *
from library import *
Font = ("Times New Roman",15)
global option
global first_choice
global second_choice
with open("my_new_data.txt","r") as f:
    currency_to_country = eval(f.readline())
    country_to_currency = eval(f.readline())
    f.close()
def overall(choice):
    my_country = input("Give country")

    if choice == "country":
        first_choice =

def country_cmd():
    overall("country")
def currency_cmd():
    overall("currency")
def get_currency():
    currency_window = Tk()
    currency_window.geometry("1000x500")
    [currency,country] = button_generator(currency_window,"currency","country")
    currency.config(command = currency_cmd)
    country.config(command = country_cmd)
    currency.pack()
    country.pack()
    currency_window.mainloop()
def american_dollar():
    first_choice = (1.0, "U.S. Dollar")
def other_dollar():
    pass
"""
main_window = Tk()
main_window.geometry("1000x500")
american = Button(main_window,text="American",font=Font,command = american_dollar)
other = Button(main_window,text="other",font=Font,command = other_dollar)
main_window.destroy()
"""
get_currency()
