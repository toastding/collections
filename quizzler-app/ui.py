from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Some Question Text',
            fill=THEME_COLOR,
            font=('Arial', 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        cross_img = PhotoImage(file="images/false.png")
        check_img = PhotoImage(file="images/true.png")

        self.wrong_btn = Button(image=cross_img, highlightthickness=0, command=self.false_pressed)
        self.wrong_btn.grid(column=1, row=2)

        self.right_btn = Button(image=check_img, highlightthickness=0, command=self.true_pressed)
        self.right_btn.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        self.quiz.check_answer('True')

    def false_pressed(self):
        self.quiz.check_answer('False')
