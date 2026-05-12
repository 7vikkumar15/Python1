
'''
from tkinter import *
window = Tk()
window.title("Demo Window")
window.geometry("800x700")

window.mainloop()
'''

#Import neccesary
from tkinter import *
from datetime import date
#Create Window
root = Tk()
root.title('Getting Started with widgets')
root.geometry('500x500')

#Widgets
lbl = Label(text = "Hey There!" , fg="white" , bg = "#07257F" , height = 1 , width = 300)

#  Add label for name
name_lbl = Label(text = "Full Name" , bg = "#3895D3")
name_entry = Entry()

lbl.pack()
name_lbl.pack()
name_entry.pack()


def display():
    name = name_entry.get()
    global Message
    message = "Welcome to the Application! \n Today's date is: "
    greet = "Hello "+name+"\n"

    text_box.insert(END , greet)
    text_box.insert(END  , message)
    text_box.insert(END  , date.today())


#btn
btn = Button(text = "Begin" , height=1 , bg = "#1261A0" ,command=display ,  fg = "white")
btn.pack()

text_box = Text(height=3)
text_box.pack()



root.mainloop()