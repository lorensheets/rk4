import math


class Vector3D(object):

    def __init__(self, points = [0.0, 0.0, 0.0]):
        self.points = points
        self.x = self.points[0]
        self.y = self.points[1]
        self.z = self.points[2]

    def add(self, vector):
        new = [x+y for x, y in zip(self.points, vector.points)]
        return Vector3D( new )

    def subtract(self, vector):
        new = [x-y for x, y in zip(self.points, vector.points)]
        return Vector3D( new )

    def multiply(self, scalar):
        for x in range(len(self.points)):
            self.points[x] *= scalar
        self.__init__(self.points)

    def divide(self, scalar):
        for x in range(len(self.points)):
            self.points[x] /= scalar
        self.__init__(self.points)

    def dot(self, vector):
        new = sum([x*y for x, y in zip(self.points, vector.points)])
        return new

    def cross(self, vector):
        x = self.y * vector.z - self.z * vector.y
        y = self.z * vector.x - self.x * vector.z
        z = self.x * vector.y - self.y * vector.x
        return Vector3D( [x,y,z] )

    def copy(self):
        return Vector3D( self.points )

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
