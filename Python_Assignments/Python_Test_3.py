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


class FlightNotFoundError(Exception):
    pass

class SeatsUnavailableError(Exception):
    pass


try:    
    file_path = open("Python_Assignments\\flights.txt", "r")
    flightDetail = {}
    file = None
    try:
        with open("Python_Assignments\\flights.txt", "r") as file:
            for line in file:
                data = line.strip().split()
                flight_number, seats, price = data
                flightDetail[flight_number] = {
                "available_seats": int(seats),
                "price": float(price)
                }

            print(flightDetail)
    except FileNotFoundError:
        print("File not found")

    finally:
        file.close()

    flightNo = input("Please enter the flight number\n")       
    if flightNo not in flightDetail:
        raise FlightNotFoundError(f"Flight {flightNo} not found.")

    reqd_tickets = int(input("Please enter number tickets you want\n"))
    flight = flightDetail[flightNo]
    if reqd_tickets > flight["available_seats"]:
        raise SeatsUnavailableError("Not enough seats available.")

    total_cost = reqd_tickets * flight["price"]
    discount = total_cost / reqd_tickets

    # Print booking details
    print("\n--- Booking Confirmed ---")
    print(f"Flight Number : {flightNo}")
    print(f"Tickets Booked: {reqd_tickets}")
    print(f"Price per Ticket: {flight['price']}")
    print(f"Total Cost    : {total_cost}")
    print(f"Discount per Ticket: {discount}")
except ZeroDivisionError as e:
    print('ZeroDivisionError', e)
except ValueError as e:
    print('ValueError:', e)            
except Exception as e:
    print('Exception occurred:', e)




 