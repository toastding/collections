from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    with open("data.txt", mode="a") as file:
        file.write(f"\n{web} | {email} | {password}")
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
generate_btn = Button(text="Generate Password")
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
