# -*- coding: utf-8 -*-
"""
Created on Sun May 13 15:19:12 2018

@author: Lesley
"""

from tkinter.ttk import *
from tkinter.ttk import Progressbar
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import Menu
window = Tk()
window.title("my window")
window.geometry('450x300') #set window size

label_one = Label(window, text = "name", font = ("Arial Bold", 20))
label_one.grid(row = 0, column = 0)

def clicked():
    msg = "Your name is \n" + textbox_one.get()
    label_one.configure(text = msg)
    yr = combo_one.get()
    label_two.configure(text = yr)
    #label_one.configure(text = "button was clicked")

button_one = Button(window, text = 'click me' , bg = "yellow", fg = "black", command = clicked)
button_one.grid(column = 0, row = 7)

def messa():
    messagebox.showinfo('alert', 'entries cannot be empty')

button_two = Button(window, text = 'message' , bg = "blue", fg = "black", command = messa)
button_two.grid(column = 1, row = 7)

def err():
    messagebox.showerror('error', 'error !!!')
    
button_two = Button(window, text = 'error' , bg = "green", fg = "black", command = err)
button_two.grid(column = 2, row = 7)

def warn():
    messagebox.showwarning('warning', 'warning!!!')

button_two = Button(window, text = 'warning' , bg = "orange", fg = "black", command = warn)
button_two.grid(column = 3, row = 7)



textbox_one = Entry(window, width = 20) #to disable widget use state = "disabled"
textbox_one.grid(row = 0, column = 1)
textbox_one.focus()

label_two = Label(window, text = "gender", font = ("Arial Bold", 20))
label_two.grid(row = 1, column = 0)

combo_one = Combobox(window)
combo_one['values'] = ('male', 'female')
combo_one.grid(row = 1, column = 1)
combo_one.current(1)

#check_state = IntVar()
#check_state(0)
checkbutton_one = Checkbutton(window,text= "single")
checkbutton_one.grid(row =4, column = 0)

checkbutton_two = Checkbutton(window,text= "married")
checkbutton_two.grid(row =4, column = 1)

checkbutton_three = Checkbutton(window,text= "divorced")
checkbutton_three.grid(row =4, column = 2)

radiobutton_one = Radiobutton(window, text = "one", value = 1)
radiobutton_one.grid(column = 0 , row = 3)

radiobutton_two = Radiobutton(window, text = "two", value = 2)
radiobutton_two.grid(column = 1 , row = 3)

radiobutton_three = Radiobutton(window, text = "one", value = 3)
radiobutton_three.grid(column = 2 , row = 3)

#spinbox_one = Spinbox(window, from_ = 0, to = 100, width = 10)
spinbox_one = Spinbox(window, values= (2,4,6), width = 10)
spinbox_one.grid(row = 2, column = 1)

label_three = Label(window, text = "age", font = ("Arial Bold", 20))
label_three.grid(row = 2, column = 0)

label_three = Label(window, text = "progress", font = ("Arial Bold", 20))
label_three.grid(row = 5, column = 0)

style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar" ,background = 'blue')
progressbar_one = Progressbar(window, length = 150 , style = "black.Horizontal.TProgressbar")
progressbar_one['value'] = 70
progressbar_one.grid(row = 5, column = 1)

label_four = Label(window, text = "photo", font = ("Arial Bold", 20))
label_four.grid(row = 6, column = 0)


window.mainloop()


