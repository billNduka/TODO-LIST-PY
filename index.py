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
    used_indices = {task["index"] for task in task_data}
    temp_i = 0
    while temp_i in used_indices:
        temp_i += 1

    task_status.insert(temp_i, IntVar())  # Insert at correct index
    def get_frame(argument):
        return {
            "daily_tasks_frame": daily_tasks_frame,
            "routine_tasks_frame": routine_tasks_frame,
            "short_term_tasks_frame": short_term_tasks_frame,
            "long_term_tasks_frame": long_term_tasks_frame
        }[argument]

    task_type = get_frame(task_frame)
    task_container = Frame(task_type, bg='#534B41')
    task_container.pack(side='top', fill='x', anchor='w', pady=2)

    Checkbutton(
        task_container,
        highlightbackground='#534B41',
        variable=task_status[temp_i],
        command=lambda idx=temp_i: checkbox_toggle(idx),
        onvalue=1,
        offvalue=0
    ).pack(side='left')

    label = Label(task_container,
                  fg='whitesmoke',
                  bg='#534B41',
                  text=entry_input.get(),
                  font=('Verdana', 12))
    tasks.insert(temp_i, label)  # Insert at correct index
    label.pack(side='left', pady='1')

    Button(task_container,
           fg='whitesmoke',
           bg='#534B41',
           text="X",
           command=lambda idx=temp_i: delete_entry(idx),
           font=('Verdana', 12)).pack(side='right', pady='1')

    entry_input.delete(0, len(entry_input.get()))
    task_data.append({
        "index": temp_i,
        "title": label.cget("text"),
        "completed": 0,
        "taskType": task_frame
    })

    save_tasks(task_data)
    if temp_i == i:
        i += 1  

def checkbox_toggle(i):
    if task_status[i].get():
        tasks[i].config(font=('Verdana', 12, "overstrike"))
        task_data[i]["completed"] = 1
    else:
        tasks[i].config(font=('Verdana', 12))
        task_data[i]["completed"] = 0
    save_tasks(task_data)

def delete_entry(idx):
    global i

    # 1. Find and destroy the task's UI container
    if idx < len(tasks):
        task_label = tasks[idx]
        task_container = task_label.master  # The parent frame
        task_container.destroy()

    # 2. Remove from task_data
    task_data[:] = [task for task in task_data if task["index"] != idx]

    # 3. Remove from tasks and task_status lists
    if idx < len(tasks):
        tasks.pop(idx)
    if idx < len(task_status):
        task_status.pop(idx)

    # 4. Update file
    save_tasks(task_data)

    # 5. Update `i` if we deleted the last task with the highest index
    used_indices = {task["index"] for task in task_data}
    while i > 0 and i - 1 not in used_indices:
        i -= 1


window = Tk() 

window.title("Index title")
window.geometry("800x1200")
window.config(background='#423C34')

parent_frame = Canvas(
    window,
    width=600,
    height=800,
    bg='#534B41'
)

vertical_scrollbar = Scrollbar(
    window,
    orient=VERTICAL,
    command=parent_frame.yview,
    jump=1
)
    
second_frame = Frame(parent_frame)

parent_frame.configure(yscrollcommand=vertical_scrollbar.set)
second_frame.bind(
    '<Configure>', lambda e: parent_frame.configure(scrollregion=parent_frame.bbox("all"))
)

def resize_frame(event):
    canvas_width = event.width
    parent_frame.itemconfig(second_frame_window, width=canvas_width)

second_frame_window = parent_frame.create_window((0, 0), window=second_frame, anchor="nw")
parent_frame.bind("<Configure>", resize_frame)






daily_tasks_frame = Frame( 
    second_frame, 
    width=600,
    bg='#534B41',
    height=100,
    relief='groove',
    borderwidth=5
)

routine_tasks_frame = Frame(
    second_frame, 
    width=600,
    bg='#534B41',
    height=100,
    relief='groove',
    borderwidth=5
)

short_term_tasks_frame = Frame(
    second_frame, 
    width=600,
    bg='#534B41',
    height=100,
    relief='groove',
    borderwidth=5
)

long_term_tasks_frame = Frame(
    second_frame, 
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
    width=40, 
    fg="black", 
    bg='#35302A',
    relief='flat',
    highlightbackground='grey',
    font=('Verdana', 12),
)
routine_task = Entry(   
    routine_tasks_frame, 
    width=40, 
    fg="black", 
    bg='#35302A',
    relief='flat',
    highlightbackground='grey',
    font=('Verdana', 12),
)
short_term_task = Entry(   
    short_term_tasks_frame, 
    width=40, 
    fg="black", 
    bg='#35302A',
    relief='flat',
    highlightbackground='grey',
    font=('Verdana', 12),
)
long_term_task = Entry(   
    long_term_tasks_frame, 
    width=40, 
    fg="black", 
    bg='#35302A',
    relief='flat',
    highlightbackground='grey',
    font=('Verdana', 12),
)

vertical_scrollbar.pack(side='right', fill='y')
parent_frame.pack(side='left', fill='both', expand=True)

# Pack labels and entries into their frames first
daily_tasks_label.pack(side="top", pady=3, fill='x', expand=True)
daily_task.pack(side="bottom", fill='x', expand=True)

routine_tasks_label.pack(side='top', fill='x', expand=True)
routine_task.pack(side="bottom", fill='x', expand=True)

short_term_tasks_label.pack(side='top', fill='x', expand=True)
short_term_task.pack(side="bottom", fill='x', expand=True)

long_term_tasks_label.pack(side='top', fill='x', expand=True)
long_term_task.pack(side="bottom", fill='x', expand=True)

# Now pack the task frames into the scrollable frame
daily_tasks_frame.pack(side='top', fill='x', expand=True)
routine_tasks_frame.pack(side='top', fill='x', expand=True)
short_term_tasks_frame.pack(side='top', fill='x', expand=True)
long_term_tasks_frame.pack(side='top', fill='x', expand=True)

daily_task.bind("<Return>", lambda event: make_entry(event, "daily_tasks_frame", daily_task))
daily_task.pack(side="bottom")

routine_task.bind("<Return>", lambda event: make_entry(event, "routine_tasks_frame", routine_task))
routine_task.pack(side="bottom")

short_term_task.bind("<Return>", lambda event: make_entry(event, "short_term_tasks_frame", short_term_task))
short_term_task.pack(side="bottom")

long_term_task.bind("<Return>", lambda event: make_entry(event, "long_term_tasks_frame", long_term_task))
long_term_task.pack(side="bottom")

daily_tasks_label.pack(side = "top", pady=3, fill='x')
routine_tasks_label.pack(side='top', fill='x')
short_term_tasks_label.pack(side='top', fill='x')
long_term_tasks_label.pack(side='top', fill='x')

load_tasks()
parent_frame.update_idletasks() 
window.mainloop()
