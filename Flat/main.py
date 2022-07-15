import logging as lg

lg.basicConfig(filename="Flat.log",format="%(asctime)s %(message)s",level=lg.INFO)

class Flat:
    """
    This is the Flat class which includes init method with 5 arguments
    This class include 6 methods flat_size, no_of_rooms, no_of washroom
    no_of_floor, flat_price and flat_info
    """

    def __init__(self,f_size,no_of_room,no_of_washroom,floor,price):
        lg.info("Creating object of Flat...")
        self.f_size = f_size
        self.no_of_room = no_of_room
        self.no_of_washroom = no_of_washroom
        self.floor = floor
        self.price = price

    def flat_size(self):
        lg.info("The size of flat is " + str(self.f_size))

    def no_of_room(self):
        lg.info("The number of room is " + str(self.no_of_room))

    def no_of_washroom(self):
        lg.info("The number of washroom is " + str(self.no_of_washroom))

    def no_of_floor(self):
        lg.info("The number of floor is " + str(self.floor))

    def flat_price(self):
        lg.info("The starting price is " + str(self.price))

    def flat_info(self):
        lg.info("The flat size is "+ str(self.f_size) + " with total "+ str(self.no_of_room) + " staring prrice is " + str(self.price))


