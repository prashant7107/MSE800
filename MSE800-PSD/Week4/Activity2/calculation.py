class RectangleLand:
#  A class to represent a rectangular plot of land.

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        # Calculates the area (L * W).
        return self.length * self.width

    def calculate_perimeter(self):
        #Calculates the perimeter (2 * (L + W)).
        return 2 * (self.length + self.width)