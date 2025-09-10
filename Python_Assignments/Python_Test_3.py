# Assignment :
 
# Problem Statement
# You are asked to design a Flight Management System in Python using exception handling. 
# The system should:
# - Read flight information from a file called flights.txt.
# - Each line has: flight_number available_seats price_per_ticket
#   Example: AI101 50 6000 
# Ask the user for:
# - Flight number
# - Number of tickets to book 
# Implement the following exception rules: (Questions below) 
# (a) Raise FlightNotFoundError (custom) if the entered flight number does not exist. 
# (b) Raise SeatsUnavailableError (custom) if requested tickets exceed available seats.
# (c) Handle ValueError if user enters invalid input (like string instead of integer). 
# (d) Handle ZeroDivisionError if user enters 0 tickets (while calculating discount per ticket). 
# (e) Always close the file using finally. 
# The program should print:
# - Flight details
# - Total booking cost
# - Discount per ticket (total / tickets) 
# Note**:
# Use nested try-except: 
# Inner block for booking operations. 
# Outer block for file handling & re-raised exceptions


try 
    print("Enter the flight number:")
    int fNo = 




 