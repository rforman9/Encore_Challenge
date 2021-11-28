# file for classes for encore coding challenge

class TempTracker:
    def __init__(self, temps=[]):
        self.temps = temps

    # instance method
    def insert(self, temp):
        self.temps.append(temp)
        return "temps now = ", self.temps

    # instance method
    def get_max(self):
        return max(self.temps)

    # instance method
    def get_min(self):
        return min(self.temps)

    # instance method
    def get_mean(self):
        return (sum(self.temps) / len(self.temps))
