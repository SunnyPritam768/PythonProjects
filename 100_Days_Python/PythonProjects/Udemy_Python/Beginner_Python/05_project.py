# Password Generator Project
import random
print("Welcome to the Password Generator Project")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
num_letters = int(input("How many letters you want in your password: "))
num_symbols = int(input("How many symbols you like in your password: "))
num_numbers = int(input("How many numbers you like in your password: "))

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
string = ""
for i in range(0, len(pass_list)):
    string += pass_list[i]
print(f"Your Password is: ", string)
