
from tkinter import *
import random, string



# Create the main window
window = Tk()

window.geometry("400x280")

window.configure(bg='yellow')


window.title("Password Generator APP")


title = StringVar()
label = Label(window, textvariable=title,bg="yellow",fg="red").pack()

title.set("CHOOSE AN OPTIONS")


def selection():
    global selection
    selection = choice.get()



choice = IntVar()
R1 = Radiobutton(window, text="WEAK", fg = "black", bg="yellow",variable=choice, value=1, command=selection).pack(anchor=CENTER)
R2 = Radiobutton(window, text="AVERAGE", fg = "black",bg="yellow", variable=choice, value=2, command=selection).pack(anchor=CENTER)
R3 = Radiobutton(window, text="STRONG", fg = "black", bg="yellow",variable=choice, value=3, command=selection).pack(anchor=CENTER)
labelchoice = Label(window)
labelchoice.pack()


title = StringVar()
label = Label(window, textvariable=title,bg="yellow",fg="red").pack()

title.set("Password length:")




val = IntVar()
spinlenght = Spinbox(window, from_=4, to_=24, textvariable=val,bg="cyan", width=15).pack()



def callback():
    lsum.config(text=passgen())



passgenButton = Button(window, text="Generate Password", bg = 'green',fg = "white", bd=5, command=callback)
passgenButton.pack(pady=20)
password = str(callback)


lsum = Label(window, text="Password here", fg="blue" ,bg = "yellow",font=("arial", 20))
lsum.pack(side=BOTTOM, anchor="n")


poor= string.ascii_uppercase + string.ascii_lowercase
average= string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
advance = poor+ average + symbols


def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))


window.mainloop()
