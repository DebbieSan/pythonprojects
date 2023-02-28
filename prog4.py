print("Program author: Debbie San")
print("Welcome to Program Three: Functions")
print("")
print("")

# This is an area and perimeter program.
# It asks users to select a calculation to be performed
# The choices are to calculate the areas of square,rectangle or circle
# Or to calculate the perimeters of square, rectangle or circle.
# After a selection has been made, the program
# asks users for inputs to make the necessary calculations.

import math  # for the math.pi constant

while True:
    print("")
    print("Menu")
    print("1.Area of Square")
    print("2.Area of Rectangle")
    print("3.Area of Circle")
    print("4.Perimeter of Square")
    print("5.Perimeter of Rectangle")
    print("6.Perimeter of Circle") 
    print("7.Exit")
    print("")

    # Make sure the user enters a valid integer selection
    try:
        menu = int(input("Please pick a number to make your selection:"))  # User makes a selection here

        if menu == 1:
            print("You have chosen Area of Square")
            side = float(input("Please enter a positive integer for the side of Square:"))
            if side < 0:  # Check for positive value
                print("Please input a positive integer!")
            else:
                area = side * side
                # round float precision to 2 decimal points
                print("The area of the square is:" + "%.2f" % round(area, 2))

        elif menu == 2:
            print("You have chosen Area of Rectangle")
            length = float(input("Please enter a positive integer for the length of Rectangle:"))
            width = float(input("Please enter a positive integer for the width of Rectangle:"))
            if length < 0 or width < 0:  # Check for positive value
                print("Please input a positive integer!")
            else:
                area = length * width
                # round float precision to 2 decimal points
                print("The area of the rectangle is:" + "%.2f" % round(area, 2))

        elif menu == 3:
            print("You have chosen Area of Circle")
            radius = float(input("Please enter a positive integer for the radius of the circle:"))
            if radius < 0:  # Check for positive value
                print("Please input a positive integer!")
            else:
                area = math.pi * radius ** 2
                # round float precision to 2 decimal points
                print("The area of the circle is:" + "%.2f" % round(area, 2))

        elif menu == 4:
            print("You have chosen Perimeter of a Square")
            side = float(input("Please enter a positive integer for the side of Square:"))
            if side < 0:  # Check for positive value
                print("Please input a positive integer!")
            else:
                perimeter = 4 * side
                # round float precision to 2 decimal points
                print("The perimeter of the square is:" + "%.2f" % round(perimeter, 2))

        elif menu == 5:
            print("You have chosen Perimeter of a Rectangle")
            length = float(input("Please enter a positive integer for the length of Rectangle:"))
            width = float(input("Please enter a positive integer for the width of Rectangle:"))
            if length < 0 or width < 0:  # Check for positive value
                print("Please input a positive integer!")
            else:
                perimeter = 2 * length + 2 * width
                # round float precision to 2 decimal points
                print("The perimeter of the rectangle is:" + "%.2f" % round(perimeter, 2))

        elif menu == 6:
            print("You have chosen Perimeter of a Circle")
            radius = float(input("Please enter a positive integer for the radius of Circle:"))
            if radius < 0:  # Check for positive value
                print("Please input a positive integer!")
            else:
                perimeter = 2 * math.pi * radius
                # round float precision to 2 decimal points
                print("The perimeter of the circle is:" + "%.2f" % round(perimeter, 2))

        elif menu == 7:
            print("Goodbye!")
            break

        else:
            print("This is not a valid choice.")
            print("")

    # Exceptions for invalid input will be caught here
    except ValueError:
        print("Please input a valid integer!")
