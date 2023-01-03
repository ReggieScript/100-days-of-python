import tkinter

window = tkinter.Tk()

#Config of the window

window.title("Miles to Kilometers converter")
window.minsize(width=250,height=150)
window.config(padx=20,pady=20)

#Setting up the grid

window.columnconfigure(5,weight=1)
window.rowconfigure(3,weight=1)

#Label for "miles"

miles_label=tkinter.Label(text="miles",font="Arial")
miles_label.grid(row=2,column=4)

#Box entry

miles_entry = tkinter.Entry(width=10)
miles_entry.insert(tkinter.END,string="0")
miles_entry.grid(row=2,column=3)

#label for "km"

km_label=tkinter.Label(text="Km", font="Arial")
km_label.grid(row=3,column=4)

#label for the converted result

km_converted=tkinter.Label(text="0",font="Arial")
km_converted.grid(row=3,column=3)

#text label used for user comprehension

text=tkinter.Label(text="is equal to: ", font="Arial")
text.grid(row=3,column=2)

def convert(): #function used to convert from miles to km
    km=round(int(miles_entry.get())*1.60934,ndigits=2)
    km_converted.config(text=str(km))
     
#Button to calculate
button=tkinter.Button(text="Calculate", command=convert, font="Arial")
button.grid(row=4,column=3)

window.mainloop()