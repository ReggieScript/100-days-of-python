# ---------------------------- LIBRARIES ------------------------------- #
import tkinter
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#f26849"
GREEN = "#379b46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
checkmark_text=""
reps=1
tempo=None

# ---------------------------- TIMER RESET ------------------------------- #

def timer_reset():
    global reps
    title.config(text="Timer", fg=GREEN)
    reps=0
    checkmarks.config(text = "")
    window.after_cancel(tempo) #Issue: for some reason it wont stop the timer
    checkmarks.config(text = checkmark_text)
    

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_sec=WORK_MIN*60
    short_sec=SHORT_BREAK_MIN*60
    long_sec=LONG_BREAK_MIN*60

    if reps == 9:
        timer_reset()
    elif reps == 8:
        title.config(text="Long Break!",fg=PINK)
        count_down(long_sec)
    elif reps % 2 == 0:
        title.config(text="Short Break!",fg=GREEN)
        count_down(short_sec)
    else:
        title.config(text="Work Time!", fg=RED)
        count_down(work_sec)

def increase_reps():
    global checkmark_text
    global reps
    if reps % 2 != 0:
        checkmark_text=checkmark_text+"✔️"
    reps += 1

def break_time():
    count_down(SHORT_BREAK_MIN*60)

def raise_above_all():
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(time): 

    minutes = int(time // 60)
    seconds = int(time % 60) 

    if time > 0:
        if seconds < 10:
            # this condition is made to prevent the timer from showing ex. 25:0 instead of 25:00
            seconds = "0" + str(seconds)

        if minutes < 10:
            minutes = "0" + str(minutes)

        tempo=window.after(1000, count_down, time-1) 
        time_text = (f"{minutes}:{seconds}")
        canvas.itemconfig(timer, text=time_text)

    else:
        time_text="00:00"
        increase_reps()
        window.lift()
        canvas.itemconfig(timer, text=time_text)
        checkmarks.config(text = checkmark_text)
        raise_above_all()
        start_timer()
    canvas.itemconfig(timer, text=time_text)
    
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro Timer")
window.minsize(height=400, width=450)
window.config(padx=50, pady=50, bg=YELLOW)

window.columnconfigure(2, weight=1)
window.rowconfigure(4, weight=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="Day28_Pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text="00:00",
                           fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=3)


title = tkinter.Label(text="Timer", fg=GREEN, font=(
    FONT_NAME, 30, "bold"), bg=YELLOW)
title.grid(column=2, row=0)

# Note to self: be careful with parenthesis and invoking functions!
start_button = tkinter.Button(
    command=start_timer, text="Start", highlightthickness=0)
start_button.grid(column=1, row=4)

reset_button = tkinter.Button(command=timer_reset,text="Reset", highlightthickness=0)
reset_button.grid(column=3, row=4)

checkmarks = tkinter.Label(
    text=checkmark_text, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
checkmarks.grid(column=2, row=4)


window.mainloop()
