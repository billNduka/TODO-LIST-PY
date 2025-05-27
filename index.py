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
            make_saved_entry(j, task["title"], task["completed"], task["taskType"])
        save_tasks(task_data)

def make_saved_entry(j, title, completed, task_type):
    global i

    def get_frame(argument):
        if argument == "daily_tasks_frame":
            return daily_tasks_frame
        elif argument == "routine_tasks_frame":
            return routine_tasks_frame
        elif argument == "short_term_tasks_frame":
            return short_term_tasks_frame
        elif argument == "long_term_tasks_frame":
            return long_term_tasks_frame

    task_type = get_frame(task_type)

    task_status.append(IntVar(value=1 if completed else 0))
    task_container = Frame(task_type, bg='#534B41')
    task_container.pack(side='top', fill='x', anchor='w', pady=2)
    Checkbutton(
        task_container, 
        highlightbackground='#534B41', 
        variable=task_status[j], 
        command=lambda idx=j : checkbox_toggle(idx), 
        onvalue=1, 
        offvalue=0,
        ).pack(side='left')
    tasks.append(Label(task_container, 
        fg='whitesmoke',
        bg='#534B41', 
        text=title,
        font=('Verdana', 12, "overstrike") if completed else ('Verdana', 12))
        )
    Button(task_container, 
            fg='whitesmoke',
            bg='#534B41', 
            text="X",
            command=lambda idx=j : delete_entry(idx),
            font=('Verdana', 12)).pack(side='right', pady='1')
    tasks[j].pack(side='left', pady='1')
    #task_data.append({"index": j, "title": title, "completed": completed})
    i += 1

def make_entry(event, task_frame, entry_input):
    global i
    task_status.append(IntVar())

    def get_frame(argument):
        if argument == "daily_tasks_frame":
            return daily_tasks_frame
        elif argument == "routine_tasks_frame":
            return routine_tasks_frame
        elif argument == "short_term_tasks_frame":
            return short_term_tasks_frame
        elif argument == "long_term_tasks_frame":
            return long_term_tasks_frame

    task_type = get_frame(task_frame)

    task_container = Frame(task_type, bg='#534B41')
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
        text=entry_input.get(),
        font=('Verdana', 12))
        )
    Button(task_container, 
        fg='whitesmoke',
        bg='#534B41', 
        text="X",
        command=lambda idx=i : delete_entry(idx),
        font=('Verdana', 12)).pack(side='right', pady='1')
    tasks[i].pack(side='left', pady='1')
    entry_input.delete(0,len(entry_input.get()))
    task_data.append({"index": i, "title": tasks[i].cget("text"), "completed": 0, "taskType": task_frame})
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

def delete_entry(i):
    print("Delete")


window = Tk() 

window.title("Index title")
window.geometry("800x2400")
window.config(background='#423C34')

daily_tasks_frame = Frame( #Change name to daily_tasks_frame
    window, 
    width=600,
    bg='#534B41',
    height=100,
    relief='groove',
    borderwidth=5
)

routine_tasks_frame = Frame(
    window, 
    width=600,
    bg='#534B41',
    height=100,
    relief='groove',
    borderwidth=5
)

short_term_tasks_frame = Frame(
    window, 
    width=600,
    bg='#534B41',
    height=100,
    relief='groove',
    borderwidth=5
)

long_term_tasks_frame = Frame(
    window, 
    width=600,
    bg='#534B41',
    height=100,
    relief='groove',
    borderwidth=5
)

daily_tasks_label = Label(
    daily_tasks_frame,
    fg='whitesmoke',
    bg='#534B41', 
    text="Daily Tasks",
    font=('Verdana', 15)
)

routine_tasks_label = Label(
    routine_tasks_frame,
    fg='whitesmoke',
    bg='#534B41', 
    text="Routine Tasks",
    font=('Verdana', 15)
)

short_term_tasks_label = Label(
    short_term_tasks_frame,
    fg='whitesmoke',
    bg='#534B41', 
    text="Short Term Tasks",
    font=('Verdana', 15)
)

long_term_tasks_label = Label(
    long_term_tasks_frame,
    fg='whitesmoke',
    bg='#534B41', 
    text="Long Term Tasks",
    font=('Verdana', 15)
)

checked = Checkbutton(
    window,   
    highlightbackground='grey'
)

daily_task = Entry(   
    daily_tasks_frame, 
    width=2100, 
    fg="black", 
    bg='#35302A',
    relief='flat',
    highlightbackground='grey',
    font=('Verdana', 12),
)
routine_task = Entry(   
    routine_tasks_frame, 
    width=2100, 
    fg="black", 
    bg='#35302A',
    relief='flat',
    highlightbackground='grey',
    font=('Verdana', 12),
)
short_term_task = Entry(   
    short_term_tasks_frame, 
    width=2100, 
    fg="black", 
    bg='#35302A',
    relief='flat',
    highlightbackground='grey',
    font=('Verdana', 12),
)
long_term_task = Entry(   
    long_term_tasks_frame, 
    width=2100, 
    fg="black", 
    bg='#35302A',
    relief='flat',
    highlightbackground='grey',
    font=('Verdana', 12),
)


daily_tasks_frame.pack(side='top', fill='x')
routine_tasks_frame.pack(side='top', fill='x')
short_term_tasks_frame.pack(side='top', fill='x')
long_term_tasks_frame.pack(side='top', fill='x')

#checked.pack(side="left")
daily_task.bind("<Return>", lambda event: make_entry(event, "daily_tasks_frame", daily_task))
daily_task.pack(side="bottom")

routine_task.bind("<Return>", lambda event: make_entry(event, "routine_tasks_frame", routine_task))
routine_task.pack(side="bottom")

short_term_task.bind("<Return>", lambda event: make_entry(event, "short_term_tasks_frame", short_term_task))
short_term_task.pack(side="bottom")

long_term_task.bind("<Return>", lambda event: make_entry(event, "long_term_tasks_frame", long_term_task))
long_term_task.pack(side="bottom")

daily_tasks_label.pack(side = "top", pady=3)
routine_tasks_label.pack(side='top', fill='x')
short_term_tasks_label.pack(side='top', fill='x')
long_term_tasks_label.pack(side='top', fill='x')

load_tasks()
window.mainloop()
