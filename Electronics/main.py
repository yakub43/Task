import logging as lg

lg.basicConfig(filename="Electronics.log",format="%(asctime)s %(message)s",level=lg.INFO)

class Electronics:
    lg.info("Creating Electronics Object...")
    __count = 0

    def __init__(self,item,price,watt,warranty,origin):
        self.item = item
        self.price = price
        self.watt = watt
        self.warranty = warranty
        self.origin = origin

    def info(self):
        lg.info("This is " + self.item + " which costs " + str(self.price))
        lg.info(self.item + " has " + str(self.warranty) + " years of warranty")

    def power_consume(self):
        lg.info("Power consumtion is " + str(self.watt))

    def country_of_origin(self):
        lg.info("The country of origin is " + self.origin)
