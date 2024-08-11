#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you:

# Let's Begin
Place_Holder = "[name]"
with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_contents = letter_file.read()
    print(letter_contents)
    for values in names:
        stripped_name = values.strip()
        new_letter = letter_contents.replace(Place_Holder, stripped_name)
        with open(f"./Output/ReadyToSend/{stripped_name}.txt", mode="w") as sender_file:
            sender_file.write(new_letter)





