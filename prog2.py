print("Program author: Debbie San")
print("Welcome to Program Two: Using Input")
print("")
print("")

# A program to ask users to input their full name
# display their full name
# obtain 2 favourite numbers
# display the result of the multiplication of the 2 favourite integers


firstName = (input("What's your first name?\n"))  # user's first name

lastName = (input("What's your last name?\n")) #user's second name


while True: 
    
    try:
    
        favNum1 = int(input("Please type your first favourite integer:\n"))#
        
        favNum2 = int(input("Please type your second favourite integer:\n"))

        multiplication= favNum1 * favNum2

        print(firstName,lastName)

        print(multiplication)
        break


    except ValueError: #warns user if an integer was not entered in the favourite number question.
        print("You didn't input a valid integer!")
