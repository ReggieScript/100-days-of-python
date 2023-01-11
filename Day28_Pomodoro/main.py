# ---------------------------- LIBRARIES ------------------------------- #
import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#379b46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro Timer")
window.minsize(height=400,width=450)
window.config(padx=50,pady=50, bg=YELLOW)

window.columnconfigure(2,weight=1)
window.rowconfigure(4,weight=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW,highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="Day28_Pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00",fill="white",font=(FONT_NAME,35, "bold"))
canvas.grid(column=2, row=3)


title=tkinter.Label(text="Timer", fg=GREEN,font=(FONT_NAME,50,"bold"), bg=YELLOW)
title.grid(column=2, row = 0)

start_button=tkinter.Button(text="Start", highlightthickness=0)
start_button.grid(column=1, row=4)

reset_button=tkinter.Button(text="Reset", highlightthickness=0)
reset_button.grid(column=3, row=4)

checkmarks=tkinter.Label(text="✔️", fg=GREEN, bg =YELLOW,font=(FONT_NAME,12,"bold"))
checkmarks.grid(column=2, row =4)


window.mainloop()
