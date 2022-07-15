from main import Flat
import logging as lg

try:

    class Flat2(Flat):

        def __init__(self,f_size,no_of_room,no_of_washroom,floor,price,city):
            lg.info("The Flat1 object is created...")
            super().__init__(f_size,no_of_room,no_of_washroom,floor,price)
            self.city = city

        def flat_city(self):
            lg.info("The flat is in " + self.city + " city")

    flat2 = Flat2(4000, 5, 3, 3,30,"Surat")
    flat2.flat_info()
    flat2.flat_city()
    flat2.flat_size()

except Exception as e:
    print(e)