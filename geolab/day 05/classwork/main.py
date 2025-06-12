class polygon:
    def __init__(self, *sides):
        self.sides = sides

    def perimeter (self):
        return sum(self.sides)
    
class quadrangle(polygon):
    def area(self):
        return self.sides[0] * self.sides[1]
    

pentagon = polygon(1,2,3,4,5)

quadrangle1 = quadrangle(1,2)

print(quadrangle1.area())