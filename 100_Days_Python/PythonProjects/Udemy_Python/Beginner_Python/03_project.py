print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
first = name1.lower()
second = name2.lower()
word=first+second

t = word.count("t")
r = word.count("r")
u = word.count("u")
e = word.count("e")
true = t+r+u+e

l = word.count("l")
o = word.count("o")
v = word.count("v")
e = word.count("e")
love = l+o+v+e

print(f"Your score is {true}{love}")

