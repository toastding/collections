from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    # if it's the 8th rep"
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        # if it's 2nd/4th/6th rep:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK, bg=YELLOW)
    else:
        # if it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"

    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# window


window = Tk()
window.title("Pomodoro")
window.config(padx=30, pady=30, bg=YELLOW)

# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 134, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)



# title_label
title_label = Label(text="TIMER", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# check_label
check_label = Label(text="✔", fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

# start_btn
start_btn = Button(text="START", highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

# restart_btn
reset_btn = Button(text="RESET", highlightthickness=0)
reset_btn.grid(column=2, row=2)

window.mainloop()