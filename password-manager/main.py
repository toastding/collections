from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please don't leave any empty!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"There are the details entered: \nEmail: {email} "                                                f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{web} | {email} | {password}\n")
                web_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=180, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(102, 102, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# Entries
web_entry = Entry(width=40)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "toast@gmail.com")

password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)


# Buttons
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
