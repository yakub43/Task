from main import Electronics
import logging as lg

lg.basicConfig(filename="TV.log", format="%(asctime)s (message)s",level=lg.INFO)

try:
    class TV(Electronics):
        lg.info("Creating object of TV")

        def Size(self,inch):
            lg.info("The size of TV is " + str(inch))

        def Resolution(self, res):
            lg.info("The resolution of TV is "+ str(res))

        def Fragile(self):
            lg.warning("Handle with care...")


    samsung = TV("TeleVision",50000,240,1,"India")
    samsung.info()
    samsung.Fragile()
    samsung.Resolution("4k")
    samsung.power_consume()


except Exception as e:
    lg.error(e)