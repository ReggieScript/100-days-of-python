import tkinter as tk
import pandas as pd
from pandas import DataFrame
import random

BACKGROUND_COLOR = "#B1DDC6"

#Reading the file

french_csv=pd.read_csv(r"Day31_FlashCards\data\french_words.csv")
word_dict=french_csv.to_dict(orient="records")

#FUNCTIONS

def disp_word():
    global rand_word
    rand_word=random.choice(word_dict)
    canvas.itemconfig(background, image=card_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=rand_word["French"], fill="black")
    window.after(3000,disp_eng)

def disp_eng():
    canvas.itemconfig(background, image=card_back)
    canvas.itemconfig(word, text=rand_word["English"], fill="white")
    canvas.itemconfig(language, text="English", fill="white")



#GUI

window=tk.Tk()

window.title("Flashcards")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
window.columnconfigure(index=2)
window.rowconfigure(index=2)

# IMAGES
canvas=tk.Canvas(width=800,height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back=tk.PhotoImage(file="Day31_FlashCards\images\card_back.png")
card_front=tk.PhotoImage(file="Day31_FlashCards/images/card_front.png")
background=canvas.create_image(400,263,image=card_front)


language=canvas.create_text(400,150,text="French", font=("Arial", 40, "italic"))
word=canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)





#Buttons


wrong_img=tk.PhotoImage(file="Day31_FlashCards/images/wrong.png")
wrong_button=tk.Button(image=wrong_img ,highlightthickness=0, command=disp_word)
wrong_button.grid(row=1,column=1)

right_img=tk.PhotoImage(file="Day31_FlashCards/images/right.png")
right_button=tk.Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=0)



window.mainloop()