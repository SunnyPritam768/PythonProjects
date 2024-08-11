# Guessing a number Challenge Game
import random
# logo = """
#
#   / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __
#  / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
# / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |
# \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|
#
# """

print("Welcome to the Game of Guessing")
print("Can you think the number between 1 to 100")
difficulty = input("Choose your difficulty: Type 'easy' or 'hard':= ")
if difficulty == 'easy':
    attempts = 12
else:
    attempts = 8
print(f"You have {attempts} attempts remaining to guess the number! ")
actual_no = random.randint(1,100)
while attempts>0:
    guess = int(input("Enter the number: "))
    if guess < actual_no:
        print("Too Low")
    elif guess > actual_no:
        print("Too High")
    elif guess == actual_no:
        print(f"You got the right answer & the number is {actual_no}")
        exit()
    attempts -= 1
    print(f"You have {attempts} left!")
if attempts == 0:
    print("You have no attempts left! Sorry You loose!")
    print(f"And the number is {actual_no}")
