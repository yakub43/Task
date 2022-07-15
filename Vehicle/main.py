import logging as lg
lg.basicConfig(filename="Vehicle.log", format="%(asctime)s %(message)s", level=lg.INFO)

class Vehicle:
    """
    This is the vehicle class which accepts 7 arguments brand, model, engine
    engine_model, year, millege and price.
    The class contains 5 methods from which one is protected method _engine_model().
    """
    Price = 0
    def __init__(self, brand, model, engine, engine_model, year, milege, price):
        lg.info("The objet of vehicle is created...")
        self.brand = brand
        self.model = model
        self.engine = engine
        self._engine_model = engine_model
        self.year = year
        self.milege = milege
        self.price = price
        Price = price

    def info(self):
        lg.info("This is " + self.brand + " " + self.model + " launched in " + str(self.year) + " with engine type " + self.engine)

    def v_brand(self):
        lg.info("The vehicle is of " + self.brand)

    def v_milege(self):
        lg.info("The milege of vehicle is " + str(self.milege))

    def v_price(self):
        lg.info("The price of " + self.brand + self.model + " is " + str(self.price))

    def _engine_model(self):
        lg.warning("The engine model is " + self._engine_model)