from tkinter import *

window = Tk()

window.title("My First GUI Page")
window.minsize(width=600, height=300)

# Labels
my_label = Label(text="My First Label", font=("Arial", 14, "bold"))
my_label.pack()
# Buttons
def button_clicked():
    print("I got clicked")
    my_label.config(text="Label Changed")
    

my_button = Button(text="click here", command=button_clicked)
my_button.pack()

window.mainloop()

