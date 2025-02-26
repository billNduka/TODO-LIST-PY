from tkinter import * 

def make_entry(event):
    Checkbutton(task_frame, highlightbackground='grey').pack(side='left')
    Label(task_frame, fg='white', text=task.get()).pack(side='top', pady='1')
    task.delete(0,len(task.get()))


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
    highlightbackground='grey'
)




task_frame.pack(side='top', fill='x')
frame.pack(side='left', fill='y')
#checked.pack(side="left")
task.bind("<Return>", make_entry)
task.pack(side="left")

window.mainloop()