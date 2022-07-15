from main import Vehicle
import logging as lg

try:
    class Bike(Vehicle):
        """
        This is bike class which is child class of Vehicle.
        """
        def __init__(self, brand, model, engine, engine_model, year, milege, price, type_of_bike):
            super().__init__(brand, model, engine, engine_model, year, milege, price)
            self.type_of_bike = type_of_bike

        def bike_type(self):
            lg.info("This is "+ self.type_of_bike)


    hero = Bike("Hero", "Passion","Patro","450cc", 2020, 65, 65000, "Normal")
    hero.bike_type()
    hero.v_price()
    hero.info()

    bmw = Bike("BMW", "BMW1", "patrol", "6hkhg00", 2021, 30, 500000, "Racing")
    bmw.v_brand()
    bmw.info()
    bmw.v_milege()

except Exception as e:
    print(e)