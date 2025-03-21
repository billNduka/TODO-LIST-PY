from tkinter import * 

i = 0
tasks = []
task_status = []

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
    i += 1

def checkbox_toggle(i):
    if task_status[i].get():
        tasks[i].config(font=('Verdana', 12, "overstrike"))
    else:
        tasks[i].config(font=('Verdana', 12))



window = Tk() # Create a window
icon = PhotoImage(file="image.png")

window.title("Index title")
window.geometry("1200x2400")
# window.maxsize(600, 600)
window.iconphoto(True, icon)
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


window.mainloop()