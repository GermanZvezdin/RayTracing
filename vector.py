import math
class vector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    def magnitude(self):
        return math.sqrt(self.dot_product(self))
    def __mul__(self, other):
        return vector(self.x * other.x, self.y * other.y, self.z * other.z)
    def __rmul__(self, other):
        return vector(self.x * other.x, self.y * other.y, self.z * other.z)
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        return vector(self.x * other, self.y * other, self.z * other)
    def __truediv__(self, other):
        return vector(self.x / other, self.y / other, self.z / other)
    def normolize(self):
        return self / self.magnitude()
