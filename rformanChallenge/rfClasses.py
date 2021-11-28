# file for classes for encore coding challenge

class TempTracker:
    """
    A class to represent a collection of temperature readings
    ...
    Attributes
    __________
    temps : list
        a list of temperatures

    Methods
    _______
    insert(temp)
        records a new temperature
    get_max()
        returns the highest temp we've seen so far.
    get_min()
        returns the lowest temp we've seen so far
    get_mean()
        returns the mean of all temps we've seen so far
    """

    def __init__(self, temps=[]):
        if temps != []:
            for temp in temps:
                temp = int(temp)
        self.temps = temps

    # instance method
    def insert(self, temp):
        self.temps.append(int(temp))
        return "temps now = ", self.temps

    # instance method
    def get_max(self):
        return max(self.temps)

    # instance method
    def get_min(self):
        return min(self.temps)

    # instance method
    def get_mean(self):
        return float((sum(self.temps) / len(self.temps)))
