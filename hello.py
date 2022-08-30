import os

#To display the current list of files/directories
curdir=os.listdir()
print("The list of current directory: "+ str(curdir))

#To create a new folder and then display the current list
fname=input("Enter the name of NEW folder: ")
os.mkdir(fname)
curdir=os.listdir()
print("The list of current directory after creating the new folder: "+ str(curdir))

#To delete the folder and then display the current list
fname=input("Enter the folder name to delete: ")
os.rmdir(fname)
curdir=os.listdir()
print("The list of current directory after deleting the folder: "+ str(curdir))

#To display the current user name
curlog=os.getlogin()
print("The current login: "+str(curlog))
