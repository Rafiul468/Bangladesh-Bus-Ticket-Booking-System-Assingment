from buss_system import BusSystem

class Admin:

    def __init__(self):
        self.username = 'admin'
        self.password = '1234'
        
    def login(self, username, password):
        if self.username == username and self.password == password:
            print("!! Login Successfully !!")
            return True
        else:
            print("!! Invalid Username or Password !!")
            return False

