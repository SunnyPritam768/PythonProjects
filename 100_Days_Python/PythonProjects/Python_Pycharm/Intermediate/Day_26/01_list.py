# Today we learn about list and dictionary Comprehension
numbers = [1, 2, 3, 4, 5]

new_list = [item+45 for item in numbers]
print(new_list)

names = "Sunny"
print([name for name in names])

