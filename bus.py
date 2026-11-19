class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0
        self.fare = 500

    # avalable_seat = totla_seats - booked_seats.

    def available_seats(self):
        return self.total_seats - self.booked_seats   
      

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            print ("!! Seat Booked Successfully !!")
            return True
        else:
            print("No Seats Avaiblable")
            return False
        