from bus import Bus
from passenger import Passenger

class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []

    
    def add_bus (self, number, route, seats):
        for bus in self.buses:
            if bus.number == number:
                print("Bus Number Already Exists.")
                return
            
        bus = Bus(number, route, seats)
        self.buses.append(bus)
        print("!! Bus added Successfully !!")


    def book_ticket(self, bus_number, name, phone):
        for bus in self.buses:
            if bus.number == bus_number:
                if bus.book_seat():
                    passenger = Passenger(name, phone, bus)
                    self.passengers.append(passenger)

                    print("!! Ticket booked successfully !!")
                    print("Passenger name: ", name)
                    print("Phone: ", phone)
                    print("Bus Number: ", bus.number)
                    print("Route: ", bus.route)
                    print("Ticket Fare tk: ", bus.fare)
                    return
        print("Bus not found")

    
    def show_buses(self):
        if not self.buses:
            print("No Buses Avaliable!")
            return

        print("\n===== Bus List =====")
        print("-"* 65)  #heading
        print("Number\tRoute\t\tTotal Seats\tAvailable Seats")
        print("-"*65)

        for bus in self.buses:
            print(f"{bus.number}\t{bus.route}\t{bus.total_seats}\t\t{bus.available_seats()}")
        print("-"* 65)