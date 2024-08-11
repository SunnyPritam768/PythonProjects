# Tip Calculator!
print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill ? $"))
tip = int(input("How much tip do you want to give($10,$12,$15): $"))
num_people = int(input("How many people to split the bill ?"))
average = round(((bill+tip)/num_people),2)
print(f"Each person should pay: ${average}")
