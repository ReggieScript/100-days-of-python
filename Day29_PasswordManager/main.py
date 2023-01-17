import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """Saves wb(website), user(username/email) and pwd(password) into a txt file """
    with open("Day29_PasswordManager\passwordmanager.txt", "a") as output:
        wb = website_entry.get()
        user = username_entry.get()
        pwd = password_entry.get()
        output.write(f"{wb} | {user} | {pwd}\n")
    website_entry.delete(0,"end")
    username_entry.delete(0,"end")
    password_entry.delete(0,"end")
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


website_entry = tk.Entry(width=45, textvariable=website)
website_entry.grid(column=2, row=1, columnspan=3, sticky="W", pady=2)


username_entry = tk.Entry(width=45, textvariable=username)
username_entry.grid(column=2, row=2, columnspan=2, sticky="W", pady=2)

password_entry = tk.Entry(width=21, textvariable=password)
password_entry.grid(column=2, row=3, sticky="W", pady=2)

# Buttons

pw_button = tk.Button(text="Generate Password")
pw_button.grid(column=3, row=3, sticky="W", pady=2)

add_button = tk.Button(text="Add Password", width=36, command=save)
add_button.grid(column=2, row=4, pady=2, columnspan=2, sticky="N")

website_entry.focus()

window.mainloop()
