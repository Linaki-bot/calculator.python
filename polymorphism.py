
class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

sh = Shape()
sh.draw()

re = Rectangle()
re.draw()

cir = Circle()
cir.draw()