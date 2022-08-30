import json

filename='userName.json'
name=''
#check for a history file
try:
    with open(filename,'r') as r:
        name=json.load(r)
except IOError:
     print("First-time login")
#If the user was found in the history file
if name != "":
    print("Welcome back, "+name+"!")
else:
    name=input("Hello! What's your name?")
    print("Welcome, "+name+"!")   
# #Save the user's name to the history file
try:
    with open(filename, 'w') as f:
        json.dump(name, f)
except IOError:
    print("There was aproblem writing to the history file.")