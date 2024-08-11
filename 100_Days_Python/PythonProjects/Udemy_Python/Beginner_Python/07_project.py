# Guess the fruits_name 
# Project Game
import random
print("Welcome\n Hello this is the Game of Guessing a word")
word_list = ["Apple", "Mango", "Banana", "Grapes","Fig",'MuskMelon','WaterMelon','Guava','Dates','Blueberry','Stawberry','Papaya','Litchi','DragonFruit','PineApple','Orange','Kiwi','Rasberry','Coconut','Pomegranate','Pear']

chosen_word = random.choice(word_list).lower()
print(f"The chosen word has {len(chosen_word)} letters.")

empty_list = ["_"] * len(chosen_word)
print(f"Empty list is: {empty_list}")

space_filled = True
life = 5
while space_filled:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                empty_list[i] = guess
        print("Correct")
    else:
        life -= 1
        print(f"Incorrect guess.\nYou have {life} lives left.")
        if life == 0:
            print("You've run out of lives.\nGame Over.")
            space_filled = False

    print(f"Current progress: {empty_list}")

    if "_" not in empty_list:
        space_filled = False
        print("You Won!\nGame Over")

print(f"The word was: {chosen_word}")



