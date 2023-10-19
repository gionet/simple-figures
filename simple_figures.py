import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self, angle, origin=(0, 0)):
        angle_radians = math.radians(angle)
        ox, oy = origin
        adjusted_x = (self.x - ox)
        adjusted_y = (self.y - oy)
        new_x = ox + adjusted_x * math.cos(angle_radians) - adjusted_y * math.sin(angle_radians)
        new_y = oy + adjusted_x * math.sin(angle_radians) + adjusted_y * math.cos(angle_radians)
        self.x, self.y = new_x, new_y

    def __str__(self):
        return f"Point({self.x:.1f}, {self.y:.1f})"


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def move(self, dx, dy):
        self.start.move(dx, dy)
        self.end.move(dx, dy)

    def rotate(self, angle, origin):
        self.start.rotate(angle, origin)
        self.end.rotate(angle, origin)

    def __str__(self):
        return f"Line({self.start}, {self.end})"


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def move(self, dx, dy):
        self.center.move(dx, dy)

    def rotate(self, angle, origin):
        self.center.rotate(angle, origin)

    def __str__(self):
        return f"Circle({self.center}, {self.radius})"


class Aggregation:
    def __init__(self, figures):
        self.figures = figures

    def move(self, dx, dy):
        for figure in self.figures:
            figure.move(dx, dy)

    def rotate(self, angle, origin):
        for figure in self.figures:
            figure.rotate(angle, origin)

    def __str__(self):
        return f"Aggregation({self.figures})"

# Modify variables (origin, point, line, circle)
pivot = (2, 1)
point = Point(-3, 5)
line = Line(Point(-3, 5), Point(-1, 3))
circle = Circle(Point(7, 8), 9)

aggregation = Aggregation([point, line, circle])

# Move aggrgation
aggregation.move(0, 0)

# Rotate all figures by "X" degrees.
aggregation.rotate(90, pivot)

# Print the new positions of all figures.
print(point)
print(line)
print(circle)
