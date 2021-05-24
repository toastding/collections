# import random
# names = ['Alan', 'Bath', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_score = {student: random.randint(1, 100) for student in names}
# print(students_score)
# passed_students = {student: score for (student, score) in students_score.items() if score > 60}
# print(passed_students)

from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label

my_label = Label(text="I Am a Label", font=("Arial", 30, "bold"))
my_label.pack()

my_label.config(text="New Text")
# my_label["text"] = "New Text!!"


# button

def button_clicked():
    print("I got clicked!")
    # my_label.config(text="Button Got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click me!!", command=button_clicked)
button.pack()

# input
input = Entry()
input.pack()
print(input.get())

window.mainloop()
