#!/usr/bin/env python3
from tkinter import * 
import json
import os

def save_tasks(tasks, memory="memory.json"):
    json_file = json.dumps(tasks)
    f = open(memory, "w")
    f.write(json_file)
    f.close()



i = 0
tasks = []
task_status = []
task_data = []
#save_tasks(task_data)

def load_tasks():
    global task_data
    if os.path.exists("memory.json"):
        with open("memory.json") as file:
            task_data = json.load(file)
        
        for j, task in enumerate(task_data):
            make_saved_entry(j, task["title"], task["completed"])
        save_tasks(task_data)

def make_saved_entry(j, title, completed):
    global i
    task_status.append(IntVar(value=1 if completed else 0))
    task_container = Frame(task_frame, bg='#534B41')
    task_container.pack(side='top', fill='x', anchor='w', pady=2)
    Checkbutton(
        task_container, 
        highlightbackground='#534B41', 
        variable=task_status[j], 
        command=lambda idx=j : checkbox_toggle(idx), 
        onvalue=1, 
        offvalue=0
        ).pack(side='left')
    tasks.append(Label(task_container, 
        fg='whitesmoke',
        bg='#534B41', 
        text=title,
        font=('Verdana', 12))
        )
    tasks[j].pack(side='left', pady='1')
    #task_data.append({"index": j, "title": title, "completed": completed})
    i += 1


def make_entry(event):
    global i
    task_status.append(IntVar())
    task_container = Frame(task_frame, bg='#534B41')
    task_container.pack(side='top', fill='x', anchor='w', pady=2)
    Checkbutton(
        task_container, 
        highlightbackground='#534B41', 
        variable=task_status[i], 
        command=lambda idx=i : checkbox_toggle(idx), 
        onvalue=1, 
        offvalue=0
        ).pack(side='left')
    tasks.append(Label(task_container, 
        fg='whitesmoke',
        bg='#534B41', 
        text=task.get(),
        font=('Verdana', 12))
        )
    tasks[i].pack(side='left', pady='1')
    task.delete(0,len(task.get()))
    task_data.append({"index": i, "title": tasks[i].cget("text"), "completed": 0})
    save_tasks(task_data)
    i += 1

def checkbox_toggle(i):
    if task_status[i].get():
        tasks[i].config(font=('Verdana', 12, "overstrike"))
        task_data[i]["completed"] = 1
    else:
        tasks[i].config(font=('Verdana', 12))
        task_data[i]["completed"] = 0
    save_tasks(task_data)




window = Tk() # Create a window

window.title("Index title")
window.geometry("800x2400")
# window.maxsize(600, 600)
window.config(background='#423C34')

frame = Frame(
    window, 
    width=250,
    bg='#534B41',
    #height=2400,
    relief='groove',
)

task_frame = Frame(
    window, 
    width=600,
    bg='#534B41',
    height=100,
    relief='groove',
)


checked = Checkbutton(
    window,   
    highlightbackground='grey'
)

task = Entry(   
    window, 
    width=2100, 
    fg="black", 
    bg='#35302A',
    relief='flat',
    highlightbackground='grey',
    font=('Verdana', 12)
)




task_frame.pack(side='top', fill='x')
frame.pack(side='left', fill='y')
#checked.pack(side="left")
task.bind("<Return>", make_entry)
task.pack(side="left")

load_tasks()
window.mainloop()
