from tkinter import *
from matplotlib import pyplot as plt
import numpy as np
import copy
import tkinter.messagebox
from pathlib import Path
import time
from datetime import datetime
double_check = tkinter.messagebox.askquestion
class Group:
    def __init__(self,name):
        self.name = name
        self.group_list = []
    def add_to_group(self,item):
        self.group_list.append(item)
class Category:
    List_of_all = []
    def __init__(self,name,budget,spent,total_list):
        self.name = name
        self.budget = budget
        self.spent = spent
        Category.List_of_all.append(self)
        self.expense_list = total_list
        self.label = ""
        self.button = ""
        self.entry= ""
        self.entry2 = ""
Font = ("Times New Roman",15)
window = Tk()
window.geometry("1000x500")
location = str(Path(__file__).parent.absolute())
myFile = open(location + "\data.txt","r")
def start_up():
    myFile = open(location + "\data.txt","r")
    for line in myFile.readlines():
        attributes = line.split("$")
        name_object = copy.deepcopy(attributes[0])
        name_object = ''.join(name_object.split())
        exec("{} = Category('{}',{},{},{})".format(name_object,*attributes))
    myFile.close()
def file_save():
    myFile = open(location + "\data.txt","w")
    for thing in Category.List_of_all:
        myFile.write("{}${}${}${}\n".format(thing.name,thing.budget,thing.spent,thing.expense_list))
    myFile.close()
def add_remove():
    add_remove_window = Tk()
    add_remove_window.geometry("200x100")
    add_remove_window.title("Category")
    L1 = Label(add_remove_window, text="Name")
    L1.place(x = 0, y = 0)
    E1 = Entry(add_remove_window)
    E1.place(x = 50, y= 0)
    L2 = Label(add_remove_window, text="Budget")
    L2.place(x = 0, y = 25)
    E2 = Entry(add_remove_window)
    E2.place(x = 50, y = 25)
    def add_remove_exit():
        name = E1.get()
        budget = E2.get()
        name_object = copy.deepcopy(name)
        name_object = ''.join(name_object.split())
        Msgbox = double_check("Check input","Name: {}\nBudget: {}".format(name,budget))
        if Msgbox == "yes":
            exec("{} = Category('{}',{}, 0, [])".format(name_object,name,budget))
        add_remove_window.destroy()
    done_btn = Button(add_remove_window,command = add_remove_exit, text = "Done",font=Font)
    done_btn.place(x = 50, y= 50)

def display():
    def budget_pie():
        labels = []
        sizes = []
        for thing in Category.List_of_all:
            labels.append(thing.name)
            sizes.append(thing.budget)
        def make_autopct(values):
            def my_autopct(pct):
                total = sum(sizes)
                val = int(round(pct*total/100.0))
                return '{v:d}'.format(v=val)
            return my_autopct
        plt.pie(sizes, labels=labels,autopct=make_autopct(sizes))
        plt.axis('equal')
        plt.title("Budget percentages")
        plt.show()
    def bar_chart():
        fig, ax = plt.subplots()
        index = np.arange(len(Category.List_of_all))
        bar_width = .35
        budget_list = []
        expense_list = []
        name_list = []
        for thing in Category.List_of_all:
            budget_list.append(thing.budget)
            expense_list.append(thing.spent)
            name_list.append(thing.name)
        budget_display = plt.bar(index+bar_width,budget_list,bar_width, label = "Budget")
        expense_display = plt.bar(index,expense_list,bar_width, label = "Expense")
        plt.xlabel("Budget/Expense")
        plt.ylabel("Dollars this month")
        plt.title("Budget/Expense vs Dollars this month")
        plt.xticks(index+bar_width/2,name_list)
        plt.legend()
        plt.tight_layout()
        plt.show()
    def expense_pie():
        labels = []
        sizes = []
        for thing in Category.List_of_all:
            labels.append(thing.name)
            sizes.append(thing.spent)
        def make_autopct(values):
            def my_autopct(pct):
                total = sum(sizes)
                val = int(round(pct*total/100.0))
                return '{v:d}'.format(v=val)
            return my_autopct
        plt.pie(sizes, labels=labels, autopct=make_autopct(sizes))
        plt.axis('equal')
        plt.title("Spent percentages")
        plt.show()
    def read_purchases():
        all_purchases_window = Tk()
        def all_purchases_exit(thing):
            message = ""
            for my_tuple in thing.expense_list:
                message += "{}: {} dollars".format(my_tuple[1],my_tuple[0])
                message += "\n"
            tkinter.messagebox.showinfo(thing.name,message)
        for thing in Category.List_of_all:
            thing.button = Button(all_purchases_window,command=lambda x=thing: all_purchases_exit(x),text=thing.name)
            thing.button.pack()
            print(thing.name)
    display_window = Tk()
    display_window.geometry("1000x500")
    budget_pie_btn = Button(display_window,command = budget_pie,text = "Budget pie chart",font = Font,wraplength = 100)
    bar_chart_btn = Button(display_window,command = bar_chart,text = "Overall bar chart",font = Font)
    expense_pie_btn = Button(display_window,command = expense_pie,text = "Expense pie chart",font = Font)
    read_purchases_btn = Button(display_window,command = read_purchases,text = "All purchases",font = Font)
    budget_pie_btn.place(x = 125,y = 100, height=200, width=150)
    bar_chart_btn.place(x = 325,y = 100,height=200, width=150)
    expense_pie_btn.place(x = 525,y = 100,height=200, width=150)
    read_purchases_btn.place(x = 725, y =100, height=200, width=150)
def set_budget():
    set_budget_window = Tk()
    set_budget_window.title("Budget")
    location_x = 0
    location_y = 0
    for thing in Category.List_of_all:
        thing.label = Label(set_budget_window,text=thing.name)
        thing.label.place(x=location_x,y=location_y)
        thing.entry = Entry(set_budget_window)
        thing.entry.place(x=location_x+50,y=location_y)
        location_y += 25
    def set_budget_exit():
        for thing in Category.List_of_all:
            try:
                thing.budget = float(thing.entry.get())
            except:
                pass
        set_budget_window.destroy()
    Button(set_budget_window,command = set_budget_exit,text="Done",font=Font).place(x = location_x+50, y= location_y +50)
def set_expense():
    set_expense_window = Tk()
    set_expense_window.title("expense")
    location_x = 0
    location_y = 25
    for thing in Category.List_of_all:
        thing.label = Label(set_expense_window,text=thing.name)
        thing.label.place(x=location_x,y=location_y)
        thing.entry = Entry(set_expense_window)
        thing.entry.place(x=location_x+50,y=location_y)
        thing.entry2 = Entry(set_expense_window)
        thing.entry2.place(x = location_x+100, y =location_y)
        location_y += 25
    def set_expense_exit():
        for thing in Category.List_of_all:
            try:
                amount = float(thing.entry.get())
                thing.spent += amount
                thing.expense_list.append([amount,thing.entry2.get()])
            except:
                continue
        set_expense_window.destroy()
    Button(set_expense_window,command = set_expense_exit,text="Done",font=Font).place(x = location_x+50, y= location_y +50)
def exit():
    window.destroy()
def end_month():
    my_check = double_check("Check input","Do you want to end the month")
    if my_check == "yes":
        with open(location + "\year.txt","a") as f:
            datem = datetime.today().strftime("%m/%y")
            month = int(str(datem)[:2]) - 1
            month = str(month) + datem[2:]
            with open(location + "\data.txt","r+") as txt:
                my_month_data = txt.readlines()
                txt.close()
            with open(location + "\data.txt","w") as txt:
                txt.close()
            f.write("\n")
            f.write(month + "\n")
            for x in my_month_data:
                f.write(x)
            f.close()
add_remove_category_btn = Button(window,command = add_remove,text = "Add/remove category",font = Font,wraplength = 100)
display_btn = Button(window,command = display,text = "Display budget",font = Font)
set_budget_btn = Button(window,command = set_budget,text = "Set Budget",font = Font)
add_expense_btn = Button(window,command = set_expense,text = "Add an expense",font = Font)
exit_btn = Button(window,command = exit,text = "Exit",font = Font)
end_month_btn = Button(window,command = end_month,text="End month", font =Font)
end_month_btn.place(x =450, y = 450, height = 50, width = 100)
add_remove_category_btn.place(x = 125,y = 100, height=200, width=150)
display_btn.place(x = 325,y = 100,height=200, width=150)
set_budget_btn.place(x = 525,y = 100,height=200, width=150)
add_expense_btn.place(x = 725, y =100, height=200, width=150)
exit_btn.place(x = 450,y= 350, height=50, width=100)
start_up()
window.mainloop()
file_save()
