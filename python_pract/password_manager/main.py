# ---------------------------- PASSWORD GENERATOR ------------------------------- #

import string
import random
from tkinter import Button, Canvas, Entry, Label, PhotoImage, messagebox, Tk
from tkinter.constants import END
import pyperclip
import json

FONT = ('Roboto', 13, 'normal')
FONT_LABEL = ('Roboto', 16, 'bold')


def password_generator():
    password = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase +
                                     string.digits) for _ in range(12))
    password_entry.insert(0, password)
    pyperclip.copy(password)

# FIND PASSWORD


def find_password():
    website = website_entry.get()
    try:
        with open('passwords.json') as file_data:
            data = json.load(file_data)
    except FileNotFoundError:
        messagebox.showwarning(
            title='Error', message='No Database Found, add something to create one.')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(
                title=website, message=f'Email : {email} \nPassword : {password}.')
        else:
            messagebox.showwarning(
                title='Error', message=f'No details for {website} exists.')


# SAVE PASSWORD
def save():
    website_name = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {website_name: {
        'email': email,
        'password': password
    }}

    if len(website_name) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Error", message="Please make sure you haven't left any field empty.")
    else:
        try:
            with open("passwords.json", "r") as file_data:
                data = json.load(file_data)
        except FileNotFoundError:
            with open('passwords.json', 'w') as file_data:
                json.dump(new_data, file_data, indent=4)
        else:
            data.update(new_data)
            with open('passwords.json', 'w') as file_data:
                json.dump(data, file_data, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# UI SETUP

EMAIL_FIELD = "email@example.com"

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website : ", width=20, font=FONT_LABEL)
website_label.grid(row=1, column=0)

email_label = Label(text="Email / Username : ", width=20, font=FONT_LABEL)
email_label.grid(row=2, column=0)

password_label = Label(text="Password : ", width=20, font=FONT_LABEL)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=42, border=5, borderwidth=5, font=FONT)
website_entry.grid(row=1, column=1)
website_entry.focus()

search = Button(
    text="Search", command=find_password, width=18, border=5, borderwidth=5, font=FONT, bg='#006ee6', fg='white')
search.grid(row=1, column=2, pady=9)

email_entry = Entry(width=62, border=5, borderwidth=5, font=FONT)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, EMAIL_FIELD)

password_entry = Entry(width=42, border=5, borderwidth=5, font=FONT)
password_entry.grid(row=3, column=1, pady=9)

# Buttons
generate_password = Button(
    text="Generate Password", command=password_generator, width=18, border=5, borderwidth=5, font=FONT, bg='#006ee6', fg='white')
generate_password.grid(row=3, column=2, pady=9)

add_button = Button(text="Add Password", width=62, command=save,
                    border=5, borderwidth=5, font=FONT, bg='#006ee6', fg='white')
add_button.grid(row=4, column=1, pady=9, columnspan=2)


window.mainloop()
