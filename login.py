#!/usr/bin/env python3
from tkinter import * 
from tkinter import messagebox 
import requests
from main_app import run_main_app
import main_app

def show_login_page():
    window = Tk() 

    window.title("Login page")
    window.geometry("800x410")
    window.config(background='#534B41', pady=2)

    title_frame = Frame(
        window,
        bg='#534B41',
        relief='groove',
        borderwidth=5
    ).pack(side="top", pady=5, fill='x')

    title_label = Label(
        title_frame,
        fg='whitesmoke',
        bg='#534B41', 
        text="LOGIN",
        font=('Verdana', 30)
    ).pack(side="top", pady=3, fill='x')

    entry_frame = Frame(
        window,
        bg='#534B41',
        relief='groove',
        borderwidth=5
    ).pack(side="top", pady=20, fill='x')

    username_label = Label(
        entry_frame,
        fg='whitesmoke',
        bg='#534B41', 
        text="USERNAME",
        font=('Verdana', 30)
    ).pack(side="top", pady=3, anchor="nw")

    username_entry = Entry(
        entry_frame, 
        width=40,
        fg="white", 
        bg='#35302A',
        relief='flat',
        highlightbackground='grey',
        font=('Verdana', 20)
    )
    username_entry.pack(side="top", pady=3, fill='x')

    password_label = Label(
        entry_frame,
        fg='whitesmoke',
        bg='#534B41', 
        text="PASSWORD",
        font=('Verdana', 30),
    ).pack(side="top", pady=3, anchor="nw")

    password_entry = Entry(
        entry_frame, 
        width=40, 
        fg="white", 
        bg='#35302A',
        relief='flat',
        highlightbackground='grey',
        font=('Verdana', 20),
        show="*"
    )
    password_entry.pack(side="top", pady=3, fill='x')

    submit_button = Button(
        window,
        text="LOGIN",
        fg="white",
        bg="#423C34",
        width=10,
    )
    submit_button.pack(side="top", pady=5)
    register_submit_button = Button(
        window,
        text="REGISTER",
        fg="white",
        bg="#423C34",
        width=10,
    )
    register_submit_button.pack(side="top", pady=5)


    def login():
        print("Logging in")
        username = username_entry.get()
        password = password_entry.get()
        if not username or not password:
            return
        try:
            response = requests.post("http://127.0.0.1:5000/user/login", json={"username": username, "password": password})
            response_data = response.json()
            if response.status_code == 201:
                messagebox.showinfo("Success", "Login successful!")
                main_app.token = response_data.get("token")
                window.destroy()
                run_main_app()
            else:
                messagebox.showerror("Error", response_data.get("message", "Login failed"))
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to connect to server: {e}")
    
    def register():
        print("Logging in")
        username = username_entry.get()
        password = password_entry.get()
        if not username or not password:
            return
        try:
            response = requests.post("http://127.0.0.1:5000/user/register", json={"username": username, "password": password})
            response_data = response.json()
            if response.status_code == 201:
                messagebox.showinfo("Success", "Registration successful!")                
            else:
                messagebox.showerror("Error", response_data.get("message", "Registration failed"))
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to connect to server: {e}")

    submit_button.config(command=login)
    register_submit_button.config(command=register)

    window.mainloop()



show_login_page()