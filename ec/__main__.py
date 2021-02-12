from curves import Curve
from points import Point

if __name__ == "__main__":
    curve = Curve(
        a =  497,
        b = 1768,
        n = 9739,
    )

    # Point Negation
    p = curve.point(8045, 6936)
    print(-p)

    # Point Addition
    p = curve.point(493, 5564)
    q = curve.point(1539, 4742)
    r = curve.point(4403, 5202)
    print(p+p+q+r)

    # Scalar Multiplication
    p = curve.point(2339, 2213)
    print(7863*p)

    # Curves and Logs
    Qa = curve.point(815, 3190)
    S  = 1829*Qa
    from hashlib import sha1
    print(sha1(str(S.x).encode('utf-8')).hexdigest())

    # Compute coordinates
    x = 4726
    y2, (ya, yb) = curve.get_coordinate_y(x)
    p1 = curve.point(x, ya)
    p2 = curve.point(x, yb)

    S1 = 6534*p1
    S2 = 6534*p2
