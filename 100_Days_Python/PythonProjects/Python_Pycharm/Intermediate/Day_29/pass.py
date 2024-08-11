from tkinter import *
from tkinter import messagebox
import json
fonte = ("Times New Roman", 12, "bold")

# ---------------------------Generator Code ----------------------------#

def Generate_Pass():
    import random
    print("Welcome to the Password Generator Project")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    num_letters = 4
    num_symbols = 2
    num_numbers = 2

    f_letter = str(random.choice(letters))
    for i in range(1, num_letters):
        f_letter += random.choice(letters)
    print(f"Letters: ", f_letter)

    f_symbol = str(random.choice(symbols))
    for j in range(1, num_symbols):
        f_symbol += random.choice(symbols)
    print(f"Symbols: ", f_symbol)

    f_number = str(random.choice(numbers))
    for k in range(1, num_numbers):
        f_number += random.choice(numbers)
    print(f"Numbers: ", f_number)

    Password = f_letter + f_symbol + f_number

    pass_list = list(Password)
    random.shuffle(pass_list)
    string_Pass = ""
    for i in range(0, len(pass_list)):
        string_Pass += pass_list[i]
    print(f"Your Password is: ", string_Pass)
    
    Pw = string_Pass
    pabox.insert(0, Pw)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    webs = webox.get()
    email = mebox.get()
    password = pabox.get()

    new_data = {
        webs: {
            "Email ": email,
            "Password ": password,
        }
    }
    
    if webs == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops!", message="You have skipped some details\nFill first all the details!")
    else:
        is_ok = messagebox.askokcancel(title="Confirm", message=f"These are the details entered:\nWebsite: {webs}\nEmail: {email}\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            with open("Data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)

            webox.delete(0, END)
            pabox.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("PASSWORD GENERATOR")
windows.config(pady=20, padx=20)
windows.minsize(height=400, width=540)

# Main Heading
heading = Label(text="Welcome To Password Generator Project", font=("Times New Roman", 20, "bold"))
heading.place(x=0, y=0)

# Lock Image
canvas = Canvas(height=200, width=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.place(x=150, y=40)

# Website Text
website = Label(text="Website: ", font=fonte, height=1)
website.place(x=0, y=250)
# Website Textbox
webox = Entry(width=50)
webox.focus()
webox.place(x=150, y=250)

# Email/Username Text
mail = Label(text="Email/Username: ", font=fonte, height=1)
mail.place(x=0, y=275)
# Email/Username Textbox
mebox = Entry(width=50)
mebox.insert(0,"sunnypritam@gmail.com")
mebox.place(x=150, y=275)

# Password Text
passw = Label(text="Password: ", font=fonte, height=1)
passw.place(x=0, y=300)
# Password Textbox
pabox = Entry(width=31)
pabox.place(x=150, y=300)
# Password Button
pas_button = Button(text="Generate Password", command=Generate_Pass)
pas_button.place(x=344, y=300)

# Add Button
add_button = Button(text="Add", width=42, command=save)
add_button.place(x=150, y=325)

windows.mainloop()
