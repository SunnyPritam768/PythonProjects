# Rock Paper Scissor Game
import random
print("Welcome to the Game of Rock Paper & Scissors")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Here is the code below
choice = True
while choice:
    print("What do you want to choose?")
    user_number = int(input("Enter 1:Rock, 2:Paper, 3:Scissors = "))
    computer_number = random.randint(1, 3)
    print(f"computer_number", computer_number)
    print(f"user_number:", user_number)

    print("--Computer's hand--")
    if computer_number == 1:
        print(rock)
    elif computer_number == 2:
        print(paper)
    else:
        print(scissors)

    print("--User's hand--")
    if user_number == 1:
        print(rock)
    elif user_number == 2:
        print(paper)
    else:
        print(scissors)


    if user_number == 1 and computer_number == 2:
        print("You lose")
    elif user_number == 2 and computer_number == 3:
        print("You lose")
    elif user_number == 3 and computer_number == 1:
        print("You lose")
    elif user_number == 2 and computer_number == 1:
        print("You win")
    elif user_number == 3 and computer_number == 2:
        print("You win")
    elif user_number == 1 and computer_number == 3:
        print("You win")
    elif user_number == computer_number:
        print("Draw Start again!")
    print("Do you want to continue(Yes(y) or No(n)")
    value = input()
    if value == 'y':
        choice = True
    else:
        choice = False
print("Thankyou for playing this game Bye Bye........")

