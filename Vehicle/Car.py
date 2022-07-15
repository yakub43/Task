from main import Vehicle
import logging as lg

try:
    class Car(Vehicle):
        """
        This is car class which is child clss of Vehicle class
        this class include one variable city and one method whcich ovverrides
        the parent class methods v_price
        """
        __TAX = Vehicle.Price * 23.3 * 10000

        def __init__(self, brand, model, engine, engine_model, year, milege, price, city):
            super().__init__(brand, model, engine, engine_model, year, milege, price)
            self.city = city

        def v_price(self):
            lg.info("The final price of vehivle is " + str(Vehicle.Price + self.__TAX))

        def Edition(self, ans):
            lg.info("This is the " + ans + " edition")

    car =  Car("hyundai", "verna", "diesel", "ch20213", 2012, 35, 5.5, "Ahmedabad")
    car.info()
    car.Edition("First")
    car.milege
    car.model

except Exception as e:
    lg.error(e)