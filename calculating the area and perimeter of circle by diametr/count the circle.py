class CIRCLE:
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius

    def get_perimetr(self):
        return self.radius * 2 * CIRCLE.PI

    def get_area(self):
        return self.radius ** 2 * CIRCLE.PI

circle1 = CIRCLE(5)
print(circle1.get_perimetr())
print(circle1.get_area())