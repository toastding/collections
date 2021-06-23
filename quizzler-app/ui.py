from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text='Some Question Text',
            fill=THEME_COLOR,
            font=('Arial', 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        cross_img = PhotoImage(file="images/false.png")
        check_img = PhotoImage(file="images/true.png")

        self.wrong_btn = Button(image=cross_img, highlightthickness=0)
        self.wrong_btn.grid(column=1, row=2)

        self.right_btn = Button(image=check_img, highlightthickness=0)
        self.right_btn.grid(column=0, row=2)

        self.window.mainloop()
