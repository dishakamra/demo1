import sys

num1 = int(input("Input a number to start: "))
num2 = int(input("Input another number to end: "))
file_path=input("Enter the file name to store the result: ")
print("Prime numbers between {} and {} stored in {}".format(num1,num2,file_path))

sys.stdout=open(file_path,"w")
print("Displaying prime numbers between {} and {}.".format(num1,num2))

for x in range(num1,num2):
    prime=True
    for i in range(2,x):
        if(x%i==0):
            prime=False
    if prime == True:
        print(x)
        
print("Done!")