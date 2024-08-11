from prettytable import PrettyTable
table = PrettyTable()  # This will create an object called table
table.add_column("Pokemon_Name",["Pikachu", "Sqirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
