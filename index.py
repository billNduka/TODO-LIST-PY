from tkinter import * 

window = Tk() # Create a window
icon = PhotoImage(file="image.png")

window.title("Index title")
window.geometry("400x400")
window.maxsize(600, 600)
window.iconphoto(True, icon)

checked = Checkbutton(window)
task = Entry(window, width=50)

checked.grid(column=0,row=0)
task.grid(column=1, row=0)

window.mainloop()