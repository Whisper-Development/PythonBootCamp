import tkinter as tk
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)== 0 or len(email)==0 or len(password)==0:
        messagebox.showerror(title="Ooops", message="All fields required")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Details entered:\n Email:{email}\nPassword:{password}\nIs it okay to save?")
        
        if is_ok:
            with open('day 29/data.txt', 'a') as f:
                saved_password = f"{website} | {email} | {password}\n"
                f.write(saved_password)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Canvas
canvas = tk.Canvas(width=200, height=200)
lock_image = tk.PhotoImage(file="day 29\logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

#Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tk.Label(text="Password")
password_label.grid(row=3, column=0)

#Entries
website_entry = tk.Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = tk.Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "whisper@email.com")
password_entry = tk.Entry(width=31)
password_entry.grid(column=1, row=3)

#Buttons
generate_button = tk.Button(text="Generate Password", width=15, command=gen_password)
generate_button.grid(column=2, row=3)
add_button = tk.Button(text="Add", width=45, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()