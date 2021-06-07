from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

# read csv
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict('records')
current_card = {}


# <-------------------------RANDOM FRENCH WORD-------------------------------->
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black", font=("Ariel", 40, "italic"))
    canvas.itemconfig(card_word, text=current_card["French"], fill="black", font=("Ariel", 40, "italic"))
    canvas.itemconfig(card_background, image=old_img)
    flip_timer = window.after(3000, card_flip)


# <-------------------------FLIP THE CARD-------------------------------->
def card_flip():
    canvas.itemconfig(card_background, image=new_img)
    canvas.itemconfig(card_title, fill="white", text="English")
    canvas.itemconfig(card_word, fill="white", text=current_card["English"])


# <-------------------------CHECK AND SAVE-------------------------------->


# window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, card_flip)


# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
old_img = PhotoImage(file="images/card_front.png")
new_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=old_img)
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button
cross_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=cross_img, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)

check_img = PhotoImage(file="images/right.png")
right_btn = Button(image=check_img, highlightthickness=0, command=next_card)
right_btn.grid(column=1, row=1)

next_card()
window.mainloop()

