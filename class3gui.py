'''

window = Tk()
window.title("Event Handler")

window.geometry("100x100")

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

window.bind("<Key>" , handle_keypress)

def handle_click(event):
    print("\n The button wass clicked")


button = Button(text="Click Me !")
button.pack()

button.pack()

button.bind("<Button-1>" , handle_click)

window.mainloop()
'''

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('200x200')

def msg():
    messagebox.showerror("Warning" , "There is a Virus found in your system . Please scan your system immediately you are cooked")

btn = Button(root ,text="Scan Now" , command=msg)
btn.place(x=40 , y=80)

def msg2():
    messagebox.askretrycancel("Question Box" , "Your system is safe and secure")

btn2 = Button(root ,text="Click Me" , command=msg2)
btn2.place(x=40 , y=120)

root.mainloop()