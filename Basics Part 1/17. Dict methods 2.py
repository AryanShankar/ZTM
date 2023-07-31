user = {
        "name": "john",
        "sex": "M",
        "age": 20
        }

print("john" in user.items())
print(('name', 'john') in user.items())
print("sex" in user)

print("john" in user.values())
print("sex" in user.keys())

print(user.items())     # returns a list containing a tuple for each key value pair

print(user.clear()) #returns None
print(user)

print("\nPART2\n")

user2 = {
        "name": "pepy",
        "sex": "F",
        "age": 45
        }

print(user2.pop("age")) #removes age and returns whats removed
print(user2)

print(user2.update({"sex": "M"}))
print(user2)

print(user2.update({"size": 32}))
print(user2)

print(user2.popitem())  # it randomly pops an item (after python 3.7 it pops of last item)
print(user2)

print(user2.keys())
print(user2.values())

print("\nPART 3\n")


user3 = {
        'age': 45, 
        'username': "john", 
        'weapons': ["gun"], 
        'is_active': True,
        'clan': "army"
        }

user3['weapons'].append('shield')
user3["weapons"] = user3["weapons"] + ["pistol"]
print(user3)