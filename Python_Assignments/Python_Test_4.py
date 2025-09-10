# Create a base class Flight with basic flight information. Create a derived class ScheduledFlight that adds scheduling information.
# Requirements:
# -Flight should have attributes: flight number, airline.
# -ScheduledFlight should add departure time and arrival time.
# -Include methods to display complete flight information.

class Flight:
    def __init__(self, flNumber, airline):
        self.FlightNumber= flNumber
        self.AirLine = airline


    def DisplayInfo(self):
        print(f"Flight Number: {self.FlightNumber}, Airline: {self.AirLine}")
    
        

class ScheduledFlight(Flight):
    def __init__(self,fightNumber,airLine, depTime, arrTime):
        super().__init__(fightNumber,airLine)
        self.DepartureTime= depTime
        self.ArrivalTime = arrTime


    def DisplayInfo(self):
        super().DisplayInfo()
        print(f"DepartureTime: {self.DepartureTime}, ArrivalTime: {self.ArrivalTime}")
       
       
scheduledFlight = ScheduledFlight("IN00123", "Indigo", "09:00 AM","12:30 PM")
scheduledFlight.DisplayInfo()


# Create a base class Person, derived class CrewMember, and a further derived class Pilot.
# -Person contains name and ID.
# -CrewMember adds role (e.g., "Cabin Crew", "Pilot").
# -Pilot adds license number and rank (e.g., "Captain").
 
class Person:
    def __init__(self,name, ID):
        self.name = name
        self.ID = ID
       
    def show_details(self):
        print(f"name: {self.name}, ID. {self.ID}")

class CraewMember(Person):
    def __init__(self, name, ID, role):
        super().__init__(name, ID)
        self.role = role

    def show_crewinfo(self):
        self.show_details()
        print(f"role {self.role}" )


class Pilot(CraewMember):
    def __init__(self, name, ID, role, license_number, rank):
        super().__init__(name, ID, role)
        self.license_number = license_number
        self.rank = rank

    def show_pilotinfo(self):
        self.show_details()
        self.show_crewinfo()
        print(f"license_number {self.license_number}, rank {self.rank}" )
    

pilot = Pilot("Santhosh", "P0001", "Tech", "License_001", "Captain")
pilot.show_pilotinfo()

# Create a base class Service, and derive two classes: SecurityService and BaggageService.
# Requirements:
# -Service class has a method service_info().
# -Derived classes override or extend this to describe their own service.
class Service:
    def service_info(self):
        print("Method service_info from Service Class")


class SecurityService(Service):
    def service_info(self):
        print("SecurityService overriden from Service")

class BaggageService(Service):
    def service_info(self):
        print("BaggageService overriden from Service")      

service = Service()
service.service_info()

secService = SecurityService()  
secService.service_info()

bagService = BaggageService()  
bagService.service_info()
 
# Create one class PassengerDetails and another class TicketDetails. Create a new class Booking that inherits from both.
# Requirements:
# - PassengerDetails has name, age.
# - TicketDetails has ticket number, seat number.
# - Booking shows all information.

class PassengerDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class TicketDetails:
    def __init__(self, ticket_number, seat_number):
        self.ticket_number = ticket_number
        self.seat_number = seat_number

class Booking(PassengerDetails, TicketDetails):
    def __init__(self, name, age, ticket_number, seat_number):
        PassengerDetails.__init__(self, name, age)
        TicketDetails.__init__(self, ticket_number, seat_number)

    def show_details(self):
        print(f"name {self.name}, age {self.age}, ticket_number {self.ticket_number}, seat_number {self.seat_number}")

    
booking = Booking("Santhosh", 25, "AI001", 1)
booking.show_details()

