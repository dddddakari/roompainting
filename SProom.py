# Function to calculate and display the area to be painted in a room based on user input
def RoomArea(roomNumber):
    print(f"\nRoom {roomNumber}")
    # Print room number for user
    print("Select the shape of the room:")
    print("1. Rectangular")
    print("2. Square")
    print("3. Custom (more or less than 4 walls, all square or rectangles)")
    choice = int(input(" "))


   # Depending on user's choice, calculate the area of the walls
    if choice == 1:
        area = rectangleWallsArea() # Function to calculate area for rectangular rooms
    elif choice == 2:
        area = squareWallsArea() # Function to calculate area for square rooms
    elif choice == 3:
        area = customWallsArea() # Function to calculate area for rectangular rooms
    else:
        print("Invalid choice.")
        return None # Returning None for invalid choice
    
    # Calculate the amount of paint needed and the cost
    gallonsNeeded = gallons(area)
    cost = paintCost(area)

    
    # Print the calculated area, gallons needed, and total cost for the room
    print(f"For Room {roomNumber}, the area to be painted is {area:.2f} square ft and will require {gallonsNeeded:.2f} gallons. This will cost the customer {cost:.2f}$")

    return area  # Returning the area for calculation in main


# Function to calculate the area of walls in a rectangular room
def rectangleWallsArea():
    # Asking for dimensions to calculate
    length = float(input("Enter the length of the room in feet:"))
    width = float(input("Enter the width of the room in feet:"))
    height = float(input("Enter the height of the room in feet:"))
    # Calculate the area of the four walls
    area = 2 * (length * height + width * height)
    # Substracting Windows and Doors
    area -= windowsDoorArea()
    return area

# Function to calculate the area of walls in a square room
def  squareWallsArea():
    side = float(input("Enter the length of one side of the room \n"))
    # Calculate the area of the four walls
    area = 4 * (side * side)
    # Substracting Windows and Doors
    area -= windowsDoorArea()
    return area

# Function to calculate 
# the area of walls in a custom-shaped room
def customWallsArea():
    # the number of walls from user input
    numWalls = int(input("Enter the number of walls in the room: \n"))
    totalArea = 0
    # Loop through each wall to calculate its area
    for i in range(numWalls):
        height = float(input(f"Enter the height of wall {i+1} in feet\n"))
        length = float(input(f"Enter the length of wall {i+1} in feet\n"))
        totalArea += length * height
    # Substracting Windows and Doors
    totalArea -= windowsDoorArea()
    return totalArea

# Function to calculate the total area of windows and doors
def windowsDoorArea():
    # Number of windows and doors from user input
    numWindowsDoor = int(input("Enter the number of windows/doors: \n"))
    totalArea = 0
    # Loop through each window/door to calculate its area
    for i in range(numWindowsDoor):
        length = float(input(f"Enter window/door length for window/door {i+1} in feet \n"))
        width = float(input(f"Enter window/door width for window/door {i+1} in feet \n"))
        totalArea += length * width
    return totalArea


# Calculate the number of gallons of paint required based on area
def gallons(area):
    pergallon = 350 # gallons of paint per square feet
    return area / pergallon

# Calculate the cost of paint required based on area
def paintCost(area):
    costPerG = 42 # Cost per gallon of paint in dollars
    reqGallons = gallons(area) # Calculate required gallons
    return reqGallons * costPerG  # Calculate total cost



def main():
    # Welcome message
    print("Welcome to Shiny Paint Company for indoor painting!")
    #  The number of rooms from user input
    numRooms  = int(input("How many Rooms do you want to paint: \n"))
    print("Thank you!")

    totalArea = 0
    # Loop through each room to calculate its area and accumulate total area
    for i in range(1,numRooms + 1):
        roomAreas = RoomArea(i)
        if roomAreas is not None: # Forcing a valid area to be returned
            totalArea += roomAreas

    # Calculate total gallons and cost for all rooms
    totalGallons = gallons(totalArea)
    totalCost = paintCost(totalArea)


    # Print the total area, gallons needed, and total cost
    print(f"Area to be painted is {totalArea:.2f} square ft and will require {totalGallons:.2f} gallons. This will cost the customer {totalCost:.2f}")

if __name__ == "__main__":
    main()