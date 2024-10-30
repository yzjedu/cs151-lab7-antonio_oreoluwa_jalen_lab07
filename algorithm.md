# Algorithm Document

1. Function: get_room_info()
   - Purpose: To collect and validate the dimensions and flooring type for a room. 
   - Parameters: None 
   - Returned Value: width(float), length(float), and flooring type(float) of the room. 
   - Algorithm:
     1. Prompt the user to enter the width of the room. 
     2. While the input is not a positive number: 
        1. Prompt the user to re-enter the width. 
     3. Convert the valid width input to a float. 
     4. Prompt the user to enter the length of the room.
     5. While the input is not a positive number:
        1. Prompt the user to re-enter the length. 
     6. Convert the valid length input to a float. 
     7. Prompt the user to enter the flooring type. 
     8. While the flooring type is not one of the valid options (hardwood, carpet, tile):
        1. Prompt the user to re-enter the flooring type. 
     9. Return the width, length, and flooring type.

2. Function: calculate_cost(width, length, flooring_type)
   - Purpose: To calculate the cost of flooring based on room dimensions and type of flooring. 
   - Parameters: width (float), length (float), flooring_type (str)
   - Returned Value: float - total cost of flooring for the room. 
   - Algorithm:
     1. Calculate the area of the room by multiplying width and length. 
     2. Initialize cost_per_sqft to 0. 
     3. If flooring type is 'hardwood': 
        1. set cost_per_sqft to 1.39.
     4. If flooring type is 'carpet':
        1. set cost_per_sqft to 3.99.
     5. If flooring type is 'tile':
        1. set cost_per_sqft to 4.99.
     6. Calculate the total cost by multiplying the area by cost_per_sqft.
     7. Return the total cost.

3. Function: main()
   - Purpose: To orchestrate the overall flow of the program, collecting inputs for multiple rooms and displaying the total cost. 
   - Parameters: None 
   - Returned Value: None 
   - Algorithm:
   1. Output an introductory greeting to the user. 
   2. Initialize check_another as "yes" to start the loop for entering room details. 
   3. While check_another is "yes":
      1. Initialize total_cost to 0 and room_count to 0. 
      2. Output a message prompting the user to enter details for 5 rooms. 
      3. While room_count is less than 5:
         1. Output the current room number being entered. 
         2. Call get_room_info() to collect room dimensions and flooring type. 
         3. Call calculate_cost(width, length, flooring_type) to compute the cost for the current room. 
         4. Add the room cost to total_cost. 
         5. Output the cost for the current room. 
         6. Increment room_count. 
         7. Output progress (how many rooms have been entered).
      4. Output the total cost for all rooms. 
      5. Ask the user if they want to check the cost for another design.
      6. While user does not input "yes" or "no":
         1. Prompt the user for valid entry
      7. If the answer is "no", 
         1. Output a goodbye message.