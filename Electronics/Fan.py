from main import Electronics
import logging as lg

lg.basicConfig(filename="Fan.log", format="%(asctime)s %(message)s", level=lg.INFO)

try:
    class Fan(Electronics):
        lg.info("Creating object of Fan...")

        def speed(self, rotation):
            lg.info("This can have maximum speed of " + str(rotation))

        def fan_type(self, type):
            lg.info("This fan is " + type)

    fan = Fan("fan",3000,250,2,"India")
    fan.info()
    fan.speed(3000)
    fan.fan_type("ceiling fan")

    fan1 = Fan("Fan",2500,250,1,"India")
    fan1.country_of_origin()
    fan1.power_consume()
    fan1.fan_type("Table Fan")

except Exception as e:
    lg.error(e)