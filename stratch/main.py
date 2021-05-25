# import random
# names = ['Alan', 'Bath', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_score = {student: random.randint(1, 100) for student in names}
# print(students_score)
# passed_students = {student: score for (student, score) in students_score.items() if score > 60}
# print(passed_students)

from tkinter import *


def button_clicked():
    print("I got clicked!")
    # my_label.config(text="Button Got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)

# creating a new window and configuration
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=30)

# label
my_label = Label(text="I Am a Label", font=("Arial", 30, "bold"))
my_label.config(text="New Text")
# my_label["text"] = "New Text!!"
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

# button
button = Button(text="Click me!!", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# new button
new_button = Button(text="New !", command=button_clicked)
# button.pack()
new_button.grid(column=2, row=0)

# Entry
input = Entry()
print(input.get())
# input.pack()
input.grid(column=3, row=2)

window.mainloop()
