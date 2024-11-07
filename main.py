# Programmers: Oreoluwa Adebusoye, Antonio Dueno Martinez
# Course: CS151, Zelalem Yalew
# Due Date: 10/30
# Programming Assignment: Lab 07
# Problem Statement:  The Flooring Cost Calculator program allows users to input the dimensions and flooring type
# for up to five rooms, calculating and displaying the individual and total costs based on the specified parameters.
# Data In: For each room (up to 5 rooms), the user will provide:
#  - Width of the room (in feet)
#  - Length of the room (in feet)
#  - Type of flooring (options: hardwood, carpet, tile)
# Data Out: For each room, the program outputs the individual cost based on the area and flooring type.
#  At the end of the input for all rooms, the program outputs the total cost for flooring all specified rooms.
# Credits: None


# Purpose: Collects and validates the dimensions and flooring type for a room.
# Parameters: None
# Return: width(float), length(float), and flooring type(float) of the room
def get_width():
    # Get the width of the room
    width = float(input("Enter the width of the room (in feet): "))

    # Validate that the input is a positive number
    while float(width) <= 0:
        print("Invalid input. Please enter a valid positive number.")
        width = float(input("Enter the width of the room (in feet): "))

    # Convert the valid input to a float
    return width


def get_length():
    # Get the length of the room
    length = float(input("Enter the length of the room (in feet): "))

    # Validate that the input is a positive number
    while float(length) <= 0:
        print("Invalid input. Please enter a valid positive number.")
        length = float(input("Enter the length of the room (in feet): "))

    # Convert the valid input to a float
    return length


def get_flooring_type():
    # Get the flooring type with validation
    flooring_type = input("Enter flooring type (options: hardwood, carpet, tile): ").strip().lower()

    # Validate the flooring type
    while flooring_type != 'hardwood' and flooring_type != 'carpet' and flooring_type != 'tile':
        print("Invalid flooring type.")
        flooring_type = input("Enter flooring type (options: hardwood, carpet, tile): ").strip().lower()
    return flooring_type


# Purpose: Calculates the cost of flooring based on room dimensions and type of flooring.
# Parameters:
    #   width (float) - width of the room in feet
    #   length (float) - length of the room in feet
    #   flooring_type (str) - type of flooring (hardwood, carpet, or tile)
# Return: float - total cost of flooring for the room.
def calculate_cost(width, length, flooring_type):
    area = width * length  # Calculate the area of the room
    cost_per_sqft = 0  # Initialize cost variable

    # Determine the cost per square foot based on flooring type
    if flooring_type == 'hardwood':
        cost_per_sqft = 1.39
    elif flooring_type == 'carpet':
        cost_per_sqft = 3.99
    elif flooring_type == 'tile':
        cost_per_sqft = 4.99
    return area * cost_per_sqft   # Return the total cost for the flooring

# Purpose: Runs the Flooring Cost Calculator, collecting user input and displaying costs.
# Parameters: None
# Return: None
def main():
    # Welcome message and purpose
    print("Welcome to the Flooring Cost Calculator!")
    print("This program will help you calculate the cost of flooring for up to 5 rooms.")
    print("You will need to provide the width and length of each room,")
    print("as well as the type of flooring you want (hardwood, carpet, or tile).")
    print("Let's get started!\n")

    check_another = "yes"    # Flag to determine if the user wants to perform another calculation

    while check_another == "yes":
        total_cost = 0
        room_count = 0

        print("Enter room details for each room.")

        # Loop to collect details for each room
        while room_count < 5:  # Continue until 5 rooms are entered
            print(f"\nDetails for Room {room_count + 1}:")
            width = get_width()
            length = get_length()
            flooring_type = get_flooring_type()
            room_cost = calculate_cost(width, length, flooring_type)  # Calculate cost
            total_cost += room_cost  # Add to total cost
            print(f"The cost for room {room_count + 1} is: ${room_cost:.2f}")
            room_count += 1  # Increment the room count

        # Display total cost for all rooms
        print(f"\nThe total cost for all rooms for this design is: ${total_cost:.2f}")

        check_another = input("\nWould you like to check the cost of another design? (Input 'yes' or 'no'): ").lower().strip()

        while check_another != "no" and check_another != "yes":
            print ("Invalid input. Please try again!")
            check_another = input("\nWould you like to check the cost of another design? (Input yes or no): ").lower().strip()
        if check_another == "no":
            print("\nThank you for using the flooring cost calculator! Goodbye!")

# Run the main function
main()