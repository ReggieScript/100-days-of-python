import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
GREEN = "#00FF00"
RED = "#FF0000"
WHITE = "#FFFFFF"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.columnconfigure(index=2)
        self.window.rowconfigure(index=3)

        self.score_label = tk.Label(
            text=f"Score: {self.quiz.score}", highlightthickness=0, fg="white", bg=THEME_COLOR, font=("Arial", 15, "bold"))
        self.score_label.grid(column=1, row=0)
        self.score_label.config(padx=10, pady=10)

        self.canvas = tk.Canvas(width=300, height=250,
                                highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.question_label = self.canvas.create_text(
            150, 125, text="Question", font=("Arial", 18, "italic"), width=250)

        true_image = tk.PhotoImage(file=r"Day34_QuizzlerApp\images\true.png")
        self.true_button = tk.Button(
            image=true_image, highlightthickness=0, command=self.true, bd = 0)
        self.true_button.grid(row=2, column=0, pady=20)

        false_image = tk.PhotoImage(file=r"Day34_QuizzlerApp\images\false.png")
        self.false_button = tk.Button(
            image=false_image, highlightthickness=0, command=self.false, bd = 0)
        self.false_button.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_label, text=q_text)
        else:
            self.canvas.itemconfig(self.question_label, text = f"You've reached the end of the quiz. Your score is: {self.quiz.score}/10" )

    def true(self):
        self.check_question("true")

    def false(self):
        self.check_question("false")

    def check_question(self,input):
        if self.quiz.check_answer(input) == True:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.update()
        self.window.after(1000)
        self.canvas.config(bg = "white") 
        self.get_next_question()
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

        