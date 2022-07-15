from main import Flat
import logging as lg

#lg.basicConfig(filename="Flat1.txt", format="%(asctime)s %(message)s", level=lg.INFO)

try:

    class Flat1(Flat):

        def __init__(self,f_size,no_of_room,no_of_washroom,floor,price,city):
            lg.info("The Flat1 object is created...")
            super().__init__(f_size,no_of_room,no_of_washroom,floor,price)
            self.city = city

        def flat_city(self):
            lg.info("The flat is in " + self.city + " city")

        def furnished(self, bool):
            if(bool == "yes"):
                lg.info("Yes the flat is furnished")
            else:
                lg.warning("The flat is not furnished.")


    flat = Flat1(1500,5,3,2,24000,"Pune")
    flat.furnished("yes")
    flat.flat_info()
    flat.flat_city()
    flat.flat_size()
except Exception as e:
    print(e)
    lg.exception(e)