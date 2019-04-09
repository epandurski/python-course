import math


class Vector:
    """Two-dimensional vector."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vector(- self.x, - self.y)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return other * self

    def __truediv__(self, other):
        return (1 / other) * self

    def __rmul__(self, number):
        return Vector(number * self.x, number * self.y)

    def __abs__(self):
        return math.sqrt(self * self)

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    def rotate90(self):
        return Vector(-self.y, self.x)


class Courtyard:
    """Rectangular area, containing objects, surrounded by a fence."""

    def __init__(self, width, height):
        """Initializes an empty courtyard with size `width` by `height` meters.

        ----------------
        |              |
        |  Courtyard   | height (y-axis)
        |              |
        ----------------
         width (x-axis)
        """

        self.width = width
        self.height = height
        self._objects = set()

        # Put a fence around the courtyard.
        self._objects.add(Fence(0, 0, width, 0))
        self._objects.add(Fence(width, 0, width, height))
        self._objects.add(Fence(width, height, 0, height))
        self._objects.add(Fence(0, height, 0, 0))

    def add_object(self, obj):
        """Add immovable object in the courtyard.

        The passed `obj` must have a `calc_distance(x, y)` method,
        which returns the distance between the point with coordinates
        (x, y) and the object.
        """

        self._objects.add(obj)

    def calc_min_distance(self, x, y):
        """Calculate the distance from point (x, y) to the nearest object."""

        assert 0 <= x <= self.width
        assert 0 <= y <= self.height
        return min(
            [obj.calc_distance(x, y) for obj in self._objects],
            default=math.inf,
        )

    def find_freest_place():
        """Return the coordinates of the point with the most free space around.

        Example:

        >>> cy = Courtyard(20, 20)
        >>> cy.find_freest_place()
        (10.0, 10.0)
        """

        # TODO!


class Fence:
    """A straight-line object, like a flat wall."""

    def __init__(self, x1, y1, x2, y2):
        self.a = Vector(x1, y1)
        self.b = Vector(x2, y2)

    def calc_distance(self, x, y):
        v = Vector(x, y)

        # Check if `a` is the nearest point.
        a_v = v - self.a
        a_b = self.b - self.a
        if a_v * a_b <= 0:
            return abs(a_v)

        # Check if `b` is the nearest point.
        b_v = v - self.b
        b_a = self.a - self.b
        if b_v * b_a <= 0:
            return abs(b_v)

        # Calculate the distance to the nearest point on the line.
        normal_to_a_b = a_b.rotate90()
        normal_to_a_b /= abs(normal_to_a_b)
        return abs(a_v * normal_to_a_b)


class Post:
    """A small structure with fixed coordinates, like a lamp post."""

    def __init__(self, x, y):
        self.position = Vector(x, y)

    def calc_distance(self, x, y):
        return abs(self.position - Vector(x, y))


class Tree(Post):
    """A tree with fixed coordinates and given crown radius."""

    def __init__(self, x, y, radius=0.0):
        assert radius >= 0.0
        super().__init__(x, y)
        self.radius = radius

    def calc_distance(self, x, y):
        trunk_distance = super().calc_distance(x, y)
        return trunk_distance - self.radius


class RectangularBuilding:
    """A solid rectangular building."""

    # TODO!
