class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point2D):
            return NotImplemented

        return self.x == other.x and self.y == other.y

if __name__ == "__main__":
    p1 = Point2D(3, 5)
    p2 = Point2D(10, -2)

    print(f"Point p1 is: {p1}")
    print(f"Point p2 is: {p2}")

    p1.x = 7
    print(f"\nAfter changing p1.x, p1 is now: {p1}")

    p3 = Point2D(7, 5)

    print(f"\nIs p1 the same as p2? {p1 == p2}")
    print(f"Is p1 the same as p3? {p1 == p3}")
