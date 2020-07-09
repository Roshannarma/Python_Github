from tkinter import *
def set_empty_list(**kwargs):
    for x in kwargs:
        exec("{} = []".format(x))
        print(x)
def create_new_class(class_name, name, list_of_attributes):
#    exec(f"{name} ={class_name}({*list_of_attributes})")
    exec("{} = {}({})".format(name,class_name,*list_of_attributes))
def window_generator(string,size="1000x500"):
    exec(f"{string}_window = Tk()")
    exec(f"{string}_window.geometry({size})")
def button_generator(window,*args):
    Font = ("Times New Roman",15)
    mylist = []
    for text in args:
        exec(f"{text} = Button(window,text='{text}',font = Font)")
        mylist.append(eval(text))
    return mylist
