#Sys Admin custom functions
import os
import subprocess

def new_user():
    confirm='N'
    while confirm != 'Y':
        username=input("Enter the user name: ")
        print("Using the user name: '" + username + "'? Y/N ")
        confirm=input().upper()
    os.system("sudo adduser "+username)

def del_user():
    confirm='N'
    while confirm != 'Y':
        username=input("Enter the user name to delete: ")
        print("confirm the user to be deleted: '" + username + "'? Y/N ")
        confirm=input().upper()
    os.system("sudo userdel -r "+username)
    
def add_user_to_group():
    username=input("Enter the name of the user that you want to add to a group: ")
    output=subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0]
    print("Enter a list of groups to add the user to")
    print("The list should be separated by spaces, for example:\r\n group1 group2 group3")
    
    # used decode('utf-8') to specified on strings
    print("The available groups are:\n " + output.decode('utf-8'))
    chosenGroups=str(input("Groups: "))

    # used split(b" "), in order to split bytes 
    output = output.split(b" ")
    chosenGroups = chosenGroups.split(" ")
    print("Add To :")
    found=True
    groupString=""
    
    for grp in chosenGroups:
        for existingGrp in output:
            if grp==existingGrp:
                found=True
                print("- Existing Group : " + grp)
                groupString = groupString + grp + ","
        if found == False:
            print("- New Group : " + grp)
            groupString = groupString + grp + ","
        else:
            found = False
            
        groupString=groupString[:-1]+" "
        confirm=""
        while confirm != "Y" and confirm != "N":
            print("Add user '"+username+"' to these groups? (Y/N)")
            confirm=input().upper()
        if confirm=="N":
            print("User '"+username+"' not added")
        elif confirm=="Y":
            os.system("sudo usermod -aG "+groupString+username)
            print("User '"+username+"' added")

add_user_to_group()

# new_user()