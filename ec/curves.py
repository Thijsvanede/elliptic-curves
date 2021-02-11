from points import Point

class Curve(object):
    """Defines a curve as y² = x³ + a*x + b (mod n)."""

    def __init__(self, a, b, n=None):
        """Initialise curve as y² = x³ + a*x + b (mod n).

            Parameters
            ----------
            a : float
                a value for curve y² = x³ + a*x + b (mod n)

            b : float
                b value for curve y² = x³ + a*x + b (mod n)

            n : int, optional
                n value for curve y² = x³ + a*x + b (mod n).
                If n is given, the curve is defined as a field and the values
                for a and b should be integers as well.
            """
        # Check if n None or all values a, b, n are integers
        assert n is None or (
            isinstance(n, int) and
            isinstance(a, int) and
            isinstance(b, int)
        )

        # Set variables
        self.a = a
        self.b = b
        self.n = n

    ########################################################################
    #                        Define points on curve                        #
    ########################################################################

    @property
    def O(self):
        """Defines the O of the curve as Point(None, None)."""
        return Point(None, None, self)

    def point(self, x, y):
        """Returns a given point on the curve, specified by x and y.

            Parameters
            ----------
            x : float
                x coordinate of point on curve.

            y : float
                y coordinate of point on curve.

            Returns
            -------
            point : Point
                Point on curve.
            """
        # Initialise point on curve
        point = Point(
            x     = x,
            y     = y,
            curve = self,
        )

        # Check if point is on curve
        if not point in self:
            raise ValueError("Point({}, {}) not on curve {}".format(x, y, self))

        # Return point
        return point

    ########################################################################
    #                            Object methods                            #
    ########################################################################

    def __eq__(self, other):
        """Check whether two curves are equivalent."""
        # Check if curves are equivalent
        return isinstance(other, Curve) and\
                self.a == other.a       and\
                self.b == other.b       and\
                self.n == other.n

    def __hash__(self, other):
        """Returns the hash of all parameters of curve."""
        # Return the hash of all parameters
        return hash((self.a, self.b, self.n))

    def __contains__(self, point):
        """Checks if a point is on the curve."""
        # Ensure point is of class Point
        assert isinstance(point, Point)

        # The O point is always on the curve
        if point == self.O: return True

        # Check if y² = x³ + a*x + b
        y2  = pow(point.y, 2, self.n)
        rhs = pow(point.x, 3, self.n) + self.a*point.x + self.b
        if self.n: rhs %= self.n

        # Return whether y² = x³ + a*x + b
        return y2 == rhs

    ########################################################################
    #                            String method                             #
    ########################################################################

    def __str__(self):
        """Returns the curve as a string."""

        # Get curve as string
        curve = "y² = x³ + {}x + {}".format(self.a, self.b)

        # Add modular if necessary
        if self.n is not None:
            curve = "{} mod {}".format(curve, self.n)

        # Return curve
        return curve
