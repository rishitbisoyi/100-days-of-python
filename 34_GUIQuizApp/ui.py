from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain

        self.window = Tk()
        self.window.title("Quizzz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.config(background="white")
        self.question_text=self.canvas.create_text(150,
                                                   125,
                                                   width=280,
                                                   text="Some question",
                                                   fill=THEME_COLOR,
                                                   font=("Arial",20,"bold"))
        self.canvas.grid(column=0, columnspan=2, row=1)

        self.score_text = Label(self.window, text="Score: 0")
        self.score_text.config(
            background=THEME_COLOR,
            font=("Arial", 15, "bold"),
            foreground="white",
            padx=20,
            pady=20
        )
        self.score_text.grid(column=1, row=0)

        self.true_img = PhotoImage(file="34_GUIQuizApp/images/true.png")
        self.true_button = Button(
            image=self.true_img,
            highlightthickness=0,
            borderwidth=0,
            command=self.true_answer
        )
        self.true_button.grid(column=0, row=2,padx=20,pady=25)

        self.false_img = PhotoImage(file="34_GUIQuizApp/images/false.png")
        self.false_button = Button(
            image=self.false_img,
            highlightthickness=0,
            borderwidth=0,
            command=self.false_answer
        )
        self.false_button.grid(column=1,row=2,padx=20,pady=25)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the QUIZ!!!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self): 
        self.give_feedback(is_right=self.quiz.check_answer("True"))

    def false_answer(self):
        self.give_feedback(is_right=self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)