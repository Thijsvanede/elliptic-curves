import math

class Point(object):

    def __init__(self, x, y, curve):
        self.curve = curve
        self.x     = x
        self.y     = y

    ########################################################################
    #                       Define division on curve                       #
    ########################################################################

    def div(self, x, y):
        """Division of two integers on the curve."""
        # For the regular case, return division
        if self.curve.n is None:
            return x / y
        # For the modular case, return inverse
        else:
            return (x * pow(y, -1, self.curve.n)) % self.curve.n

    ########################################################################
    #                         Arithmatic relations                         #
    ########################################################################

    def __eq__(self, other):
        # Check if points are equivalent
        return isinstance(other, Point) and\
            self.curve == other.curve   and\
            self.x     == other.x       and\
            self.y     == other.y

    def __neg__(self):
        # -O == O
        if self == self.curve.O:
            return self

        # Return -P
        else:
            return Point(
                x     =  self.x,
                y     = -self.y if self.curve.n is None else self.curve.n - self.y,
                curve =  self.curve,
            )

    def __add__(self, other):
        # Special cases
        if self  == self.curve.O: return other        # O +  P = P
        if other == self.curve.O: return self         # P +  O = P
        if self  == -other      : return self.curve.O # P + -P = O

        # Compute the slope if P.x != Q.x
        if self.x != other.x:
            # Compute the slope using division/inversion for modular arithmatic
            try:
                slope = self.div(
                    self.y - other.y,
                    self.x - other.x,
                )
            except ValueError:
                raise ValueError(
                    "Could not add, curve order is not smooth enough."
                )


        # Compute the slope if P.x == Q.x
        else:
            try:
                # Compute the slope using division/inversion for modular arithmatic
                slope = self.div(
                    3*pow(self.x, 2) + self.curve.a,
                    2*self.y,
                )
            except ValueError:
                raise ValueError(
                    "Could not add, but found a non-trivial factor of {}: {}"
                    .format(self.curve.n, math.gcd(2*self.y, self.curve.n))
                )

        # Compute new x coordinate
        x = pow(slope, 2) - self.x - other.x
        # Compute modular x if necessary
        if self.curve.n: x %= self.curve.n

        # Compute y coordinate
        y = self.y + slope*(x - self.x)
        # Compute modular x if necessary
        if self.curve.n: y %= self.curve.n

        # Return new point
        return -Point(
            x = x,
            y = y,
            curve = self.curve,
        )

    def __rmul__(self, other):
        assert isinstance(other, int) and other > 0

        # Initialise variables
        result   = self.curve.O # Initialise to O
        doubling = self         # Get doubling term

        # Double and add (if binary place contains a 1)
        i = 1
        while True:
            # Add if binary place contains a 1
            if i & other != 0:
                result += doubling

            # Increment i
            i <<= 1
            # Break if i > other
            if i > other: break

            # Double result
            doubling += doubling

        # Return result
        return result


    ########################################################################
    #                            String method                             #
    ########################################################################

    def __str__(self):
        # Get point as string
        if self == self.curve.O:
            return "[Curve {}] O".format(self.curve)
        else:
            return "[Curve {}] Point({}, {})".format(self.curve, self.x, self.y)
