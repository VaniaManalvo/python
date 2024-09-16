#Vania Manalvo
#PI04-NST

import email
from tkinter import messagebox
import tkinter as tk
import csv
import hashlib


#function entry
def username():
    window.entry()

#funtion exit
def close_window():
    window.destroy()

#funtion autentication
def autentication():
    userid = username.entry.get()
    password = password.entry.get()
    if userid == "usermame" and password == "password": 
        messagebox.showinfo("Login Sucessful! ", "Correct!", userid)
    else: messagebox.showerror("Login Incorrect!", "User or Password")

#user creation
def user():
    user = email.entry.get()
    password = password.entry.get()
    if user == "email" and password == "password":
        messagebox.showinfo("Login Sucessful!" "Correct!")
    else: messagebox.showerror("Login Incorret!", "User or Password Incorret!")


#window creation
window = tk.Tk()
window.title("Login")

#label creation
label = tk.Label(window, text="Welcome!")
label.pack(padx=25,pady=25)
def user_text():
    username_entry.delete(0, "end")

#user space
username_label = tk.Label(window, text="Usename:")
username_label.pack()
username_entry = tk.Entry(window, textvariable="s")
username_entry.pack()
username_entry.pack(padx=10,pady=10)

#password space
password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")#show de password
password_entry.pack()
password_entry.pack(padx=10,pady=10)

#button for login and close
username_button = tk.Button(window, text="Login", command=autentication)
username_button.pack(padx=10,pady=10)
close_button = tk.Button(window, text="Close", command=close_window)
close_button.pack(padx=10,pady=10)

#to execute loop
window.mainloop()