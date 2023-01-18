import tkinter as tk
import random
import pyperclip
import json
from tkinter import messagebox

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """Generates a random password"""

    password_entry.delete(0, "end")
    rand_password = ''.join(
        [random.choice(random.choice([letters, numbers, symbols])) for i in range(10)])
    pyperclip.copy(rand_password)
    password_entry.insert(0, rand_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """Saves wb(website), user(username/email) and pwd(password) into a txt file """

    wb = website_entry.get()
    user = username_entry.get()
    pwd = password_entry.get()

    if len(wb) == 0 or len(pwd) == 0 or len(user) == 0:
        messagebox.showinfo(message="Woops! You are missing info, try again.", title="Whoops!")
    
    else:
        new_data = {
            wb: {
                "email": user,
                "password": pwd,
            }
        }
        with open("Day29_PasswordManager\passwordmanager.json", "w") as output:
            json.dump(new_data, output, indent=4)

        website_entry.delete(0, "end")
        username_entry.delete(0, "end")
        password_entry.delete(0, "end")

        messagebox.showinfo(message="Your username and passwod are safe now!  :)", title="Info")



def search():
    """Looks for previously saved passwords"""
    wb = website_entry.get()
    try:
        open("Day29_PasswordManager\passwordmanager.json", "r")
    except FileNotFoundError:
        data_file=open("Day29_PasswordManager\passwordmanager.json", "w")
        msg="The username and password were not found."
    
    else:
        with open("Day29_PasswordManager\passwordmanager.json", "r") as data_file:
            try:
                json_data=json.load(data_file)
            except json.decoder.JSONDecodeError:
                msg="The username and password were not found."
            else:
                if wb in json_data:
                    msg=f"Username: {json_data[wb]['email']} \n Password: {json_data[wb]['password']}"
                else:
                    msg="The username and password were not found."
    messagebox.showinfo(message=msg, title="Info")  

# ---------------------------- UI SETUP ------------------------------- #

# Creating the window


window = tk.Tk()

window.title("MyPass")
window.minsize(height=400, width=400)
window.config(padx=40, pady=20)

window.columnconfigure(2, weight=1)
window.rowconfigure(4, weight=1)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tk.PhotoImage(file="Day29_PasswordManager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=3)

website = tk.StringVar()
username = tk.StringVar()
password = tk.StringVar()


# Labels

website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1, columnspan=2, pady=2)

username_label = tk.Label(text="Email/Username:")
username_label.grid(column=0, row=2, columnspan=2, pady=2)

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3, columnspan=2, pady=2)


# Entries


website_entry = tk.Entry(width=30, textvariable=website)
website_entry.grid(column=2, row=1, columnspan=3, sticky="W", pady=2)

username_entry = tk.Entry(width=45, textvariable=username)
username_entry.grid(column=2, row=2, columnspan=2, sticky="W", pady=2)

password_entry = tk.Entry(width=21, textvariable=password)
password_entry.grid(column=2, row=3, sticky="W", pady=2)

# Buttons

search_button = tk.Button(text="Search", command=search, width=10)
search_button.grid(column=3, row=1, columnspan=1, sticky="E")

pw_button = tk.Button(text="Generate Password", command=generate_password)
pw_button.grid(column=3, row=3, sticky="W", pady=2)

add_button = tk.Button(text="Add Password", width=36, command=save)
add_button.grid(column=2, row=4, pady=2, columnspan=2, sticky="N")

website_entry.focus()

window.mainloop()
