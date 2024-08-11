# How to create your own class
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

person_1 = User("001", "Sunny Pritam")
print(person_1)
print(person_1.id)
print(person_1.username)

person_2 = User("002", "Isha Pritam")
print(person_2)
print(person_2.id)
print(person_2.username)
