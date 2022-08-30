#demo.py
import subprocess

def add_user_to_group():
    #username=input("Enter the name of the user that to add to a group: ")
    output=subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0]
    #print("Enter a list of groups to add the user to")
    #print("The list should be separated by spaces, for example:\r\n group1 group2 group3")
    print("The available groups are:\r\n " + str(output))
    
add_user_to_group()