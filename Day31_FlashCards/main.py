import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"

window=tk.Tk()

window.title("Flashcards")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
window.columnconfigure(index=2)
window.rowconfigure(index=2)

# IMAGES


# card_back=tk.PhotoImage(r"Day31_FlashCards\images\card_back.png")



#Buttons
right_img=tk.PhotoImage(r"Day31_FlashCards\images\right.png")
right_button=tk.Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=0)
wrong_img=tk.PhotoImage(r"Day31_FlashCards\images\wrong.png")
wrong_button=tk.Button(image=wrong_img,highlightthickness=0)
wrong_button.grid(row=1,column=1)


canvas=tk.Canvas(width=800,height=526, highlightthickness=0)
card_front=tk.PhotoImage("Day31_FlashCards\images\card_front.png")
canvas.create_image(500,500,image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

window.mainloop()