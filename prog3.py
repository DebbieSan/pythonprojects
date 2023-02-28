print("Program author: Debbie San")
print("Welcome to Program Three: Loops and If Conditions")
print("")
print("")

# A program that asks the user to input a password
# then asks the user to input their name, compare to other names and
# gives a compliment.
# If password is wrong, program will ask user to try again until user gets it.


password = (input("Welcome! What's the password?\n"))  # user inputs password
while password != "hello":
    password = input("Try again\n>")
    
print("Welcome to the second part of the program!")    

name = (input("What's your name?\n"))  # user inputs their name

if name == "Cher" or name == "Madonna":
    print("May I have your autograph, please?")

elif name == 'Debbie':
    print("What a great name!")

else:
    print(name, ",", "that's a nice name.")
