import random

class Insect:

    def __init__(self, w, l, n):
        self.wings = w
        self.legs = l
        self.flight = 0
        self.__name = n


    def flightlength(self):
        self.flight = random.randrange(1,11)


    def get_miles(self):
        return self.flight
    
    def get_name(self):
        return self.__name



