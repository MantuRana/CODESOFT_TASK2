from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    
ws = Tk()
ws.geometry('500x400')
ws.title('To-Do-List')
ws.config(bg='black')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=2)

lb = Listbox(
    frame,
    width=40,
    height=5,
    font=('Times', 18),
    bd=0,
    fg='black',
    highlightthickness=0,
    selectbackground='blue',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'Thank you @codesoft🙏😊. ',
 
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=10)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    fg = "white",
    bg='green',
    padx=15,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    fg = "white",
    bg='red',
    padx=15,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()