# Miles to Kilometer Converter Project
from tkinter import *
YELLOW = "#f7f5dd"
windows = Tk()
windows.title("Miles to Kilometer Converter")
windows.config(padx=20, pady=20, bg=YELLOW, highlightthickness=0)
windows.minsize(width=400, height=200)

# Welcome Text
welcome_label = Label(text="Welcome! This is your New Project", font=("Arial", 14, "bold"))
welcome_label.place(x=10, y=10)

# Entry for miles
miles_entry = Entry(width=10)
miles_entry.insert(END, string="0")
miles_entry.place(x=10, y=53)

# Text after entry miles
after_that = Label(text="miles is equal to", font=("Arial", 12))
after_that.place(x=80, y=50)

# initialize kilometers
km = 0
initial = Label(text=f" {km}    kilometers",  font=("Arial", 12))
initial.place(x=200, y=50)

# Button to click and get the answer
def action():
    value = miles_entry.get()
    new_value = round(float(value)*1.609)
    final = initial.config(text=f" {new_value}   kilometers", font=("Arial", 12))

click = Button(text="click here", command=action)
click.place(x=150, y=90)

windows.mainloop()
