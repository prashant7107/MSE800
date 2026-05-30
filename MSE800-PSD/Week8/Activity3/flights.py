from datetime import datetime

#Paren class Flight
class Flight:
    def __init__(self, flight_number: str, origin: str, destination: str, 
                 aircraft_type: str, base_price: float, scheduled_departure: datetime, 
                 scheduled_arrival: datetime, flight_status: str, total_seats: int):
      
       # Initializes all private attributes.
        self._flight_number = flight_number
        self._origin = origin
        self._destination = destination
        self._aircraft_type = aircraft_type
        self._base_price = float(base_price)
        
        # Default document required for a general/international flight
        self._required_document = "Passport"
        
        self._scheduled_departure = scheduled_departure
        self._scheduled_arrival = scheduled_arrival
        self._flight_status = flight_status # Scheduled / Delayed / Active
        self._total_seats = total_seats

    #  Public Methods 
    
    def display_basic_info(self):
        """Prints general details of the flight."""
        print(f"\n Flight Info [{self._flight_number}] ")
        print(f"Route:       {self._origin} -> {self._destination}")
        print(f"Aircraft:    {self._aircraft_type}")
        print(f"Status:      {self._flight_status}")
        print(f"Departure:   {self._scheduled_departure.strftime('%Y-%m-%d %H:%M')}")
        print(f"Arrival:     {self._scheduled_arrival.strftime('%Y-%m-%d %H:%M')}")
        print(f"Base Price:  ${self._base_price:.2f}")

    def check_visa_requirement(self):
        
        print(f" Checking visa for {self._destination}")
        print(f" A visa is mandatory")
        return True

    def verify_identity(self, document_type):
        
        if document_type.strip().lower() == "passport":
            print(f" Identity verified using valid Passport.")
            return True
        else:
            print(f" Identity verification FAILED. '{document_type}' is invalid. A {self._required_document} is required.")
            return False


# SubClass DomestricFlight
class DomesticFlight(Flight):
    def __init__(self, flight_number: str, origin: str, destination: str, 
                 aircraft_type: str, base_price: float, scheduled_departure: datetime, 
                 scheduled_arrival: datetime, flight_status: str, total_seats: int,
                 domestic_terminal: str, baggage_allowance_domestic: str, fare_product: str):
        
        # Constructor for the Domestic Flight class.

        # Initialize all inherited parent attributes safely via the super constructor

        super().__init__(flight_number, origin, destination, aircraft_type, base_price, 
                         scheduled_departure, scheduled_arrival, flight_status, total_seats)
        
        # Initialize private attributes unique to domestic operations

        self._domestic_terminal = domestic_terminal
        self._baggage_allowance_domestic = baggage_allowance_domestic
        self._fare_product = fare_product # Seat / Seat+Bag / Flexi
        
        # Attribute Overriding: change the parent's default document requirement
        self._required_document = "Any Valid Photo ID"

    # Subclass Specific Method
    
    def apply_domestic_discount(self) -> None:
        # Reduces the base price of the domestic flight.
        discount_amount = self._base_price * 0.15
        self._base_price -= discount_amount
        print(f"\n 15% Air NZ domestic discount applied! New Fare: ${self._base_price:.2f}")

    #  Overridden Methods 

    def check_visa_requirement(self) -> bool:
        
        print(f" Flight {self._flight_number} stays within New Zealand borders.")
        print(f" International visa checks not required")
        return False

    def verify_identity(self, document_type):
        # local validation options (Driver License, etc.)
        # List of acceptable domestic forms of identity
        acceptable_ids = ["driver license", "passport", "national id"]
        
        if document_type.strip().lower() in acceptable_ids:
            print(f" Identity verified. '{document_type}' ")
            return True
        else:
            print(f" '{document_type}' is not a recognized identity. Must be {self._required_document}.")
            return False


# Execution
if __name__ == "__main__":
    # Mocking execution times
    departure_time = datetime(2026, 12, 15, 8, 30)
    arrival_time = datetime(2026, 12, 15, 9, 45)

    print("\n" + "International Flight")
    # Instantiating a general flight configuration
    intl_flight = Flight("NZ2", "Auckland", "Los Angeles", "Boeing 787", 1450.00, 
                         departure_time, arrival_time, "Scheduled", 302)
    
    intl_flight.display_basic_info()
    intl_flight.check_visa_requirement()
    # Testing identity checks against parent constraints
    intl_flight.verify_identity("Driver License")  # Will fail
    intl_flight.verify_identity("Passport")        # Will pass

    print("\n" + "Next Domestic Flight")
   
    # Instantiating the domestic flight
    nz_domestic = DomesticFlight(
        flight_number="NZ401", 
        origin="Auckland", 
        destination="Wellington", 
        aircraft_type="Airbus A320", 
        base_price=180.00, 
        scheduled_departure=departure_time, 
        scheduled_arrival=arrival_time, 
        flight_status="Active", 
        total_seats=171,
        domestic_terminal="Terminal A (Domestic)", 
        baggage_allowance_domestic="1x 23kg", 
        fare_product="Seat+Bag"
    )

    # Calling inherited
    nz_domestic.display_basic_info()
    
    # overridden checking logic
    nz_domestic.check_visa_requirement()
    
    # identity checks
    nz_domestic.verify_identity("Driver License")  # Will pass 
    nz_domestic.verify_identity("Library Card")    # Will fail 
    
    # subclass-specific behavior
    nz_domestic.apply_domestic_discount()