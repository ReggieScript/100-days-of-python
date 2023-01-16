import tkinter as tk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# Creating the window

window = tk.Tk()
window.title("MyPass")
window.minsize(height=400, width=400)
window.config(padx=20, pady=20)

window.columnconfigure(2, weight=1)
window.rowconfigure(4, weight=1)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tk.PhotoImage(file="Day29_PasswordManager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, columnspan=3)

website = tk.Label(text="Website:")
website.grid(column=0, row=1, columnspan=2, pady=2)

website_entry = tk.Entry(width=35)
website_entry.grid(column=2, row=1, columnspan=3, sticky="W", pady=2)

username = tk.Label(text="Email/Username:")
username.grid(column=0, row=2, columnspan=2, pady=2)

username_entry = tk.Entry(width=35)
username_entry.grid(column=2, row=2, columnspan=2, sticky="W", pady=2)

password = tk.Label(text="Password:")
password.grid(column=0, row=3, columnspan=2, pady=2)

password_entry = tk.Entry(width=21)
password_entry.grid(column=2, row=3, sticky="W", pady=2)

pw_button = tk.Button(text="Generate Password")
pw_button.grid(column=3, row=3, sticky= "W", pady=2)

add_button= tk.Button(text="Add Password", width=36)
add_button.grid(column=2, row=4, pady=2, columnspan=2, sticky="N")

window.mainloop()
