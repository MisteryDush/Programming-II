from taxi import Taxi


class SilverServiceTaxi(Taxi):

    flagfall = 4.5

    def __init__(self, name, fuel, price_per_km, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = price_per_km * fanciness
