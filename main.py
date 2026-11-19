from buss_system import BusSystem
from admin import Admin

system = BusSystem()
admin = Admin()

def admin_menu():
        
    while True:
        print("\n----- Admin Menu ------")
        print("1. Add Bus")
        print("2. View All Buses")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                number = int(input("Enter Bus Number: "))
                route = input("Enter Route: ")
                seats = int(input("Enter Total Seats: "))

                if number <= 0 or seats <=0 or not route:
                    print("Invalid Bus Information.")
                    continue

                system.add_bus(number, route, seats)
            except ValueError:
                print("Please Enter Valid Numbers.")
                
        elif choice == '2':
            system.show_buses()

        elif choice == '3':
            print("Admin Logged Out")
            break
        else:
            print("Invalid Choice!")


while True:
    print("\n------ Bus Managment System ------")
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. view Buses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if admin.login(username, password):
            admin_menu()


    elif choice == '2':

        try:
            bus_number = int(input("Enter Bus Number: "))
            name = input("Enter Passenger Name: ").strip()
            phone = input("Enter Phone Number: ").strip()

            if bus_number <= 0 or not name or not phone:
                print("Invalid Passenger Information.")
                continue   
            system.book_ticket(bus_number, name, phone)
        except ValueError:
            print("Please Enter a Valid Bus Number.")         
            
    elif choice == '3':
        system.show_buses()

    elif choice == '4':
            print("Thank you for using Bangladesh Bus Ticket System")
            break
    else: 
        print("Invalid Choice.")