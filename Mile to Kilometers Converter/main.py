from tkinter import *


# Window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# unit label(Miles)
label1 = Label(text="Miles", font=("Arial", 12))
label1.grid(column=2, row=0)

# unit label(is equal to)
label2 = Label(text="is equal to", font=("Arial", 12))
label2.grid(column=0, row=1)

# unit label(Km)
label3 = Label(text="Km", font=("Arial", 12))
label3.grid(column=2, row=1)

# label(convert km)
km_label = Label(text=0, font=("Arial", 12))
km_label.grid(column=1, row=1)

# input
input = Entry(width=7)
input.insert(END, string=0)
input.grid(column=1, row=0)


# button
def button_clicked():
    miles = float(input.get())
    km = miles * 1.609
    km_label.config(text=f"{km}")
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
