from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
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
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, columnspan=1)

# Buttons
generate_btn = Button(text="Generate Password")
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
