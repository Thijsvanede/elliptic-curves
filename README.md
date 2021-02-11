# elliptic-curves
Implementation of Elliptic Curves - used for crypto CTFs.

```
This is a disclaimer that I shouldn't have to make, but please don't use this implementation for actual cryptographic products.
It is simply an implementation for me (and others interested in Elliptic Curve crypto) to toy with.
```

## Installation
Currently, installation is only possible by downloading this github repository and performing the install locally.

To download the repository:

Using HTTPS:
```
git clone https://github.com/Thijsvanede/elliptic-curves.git
```

Using SSH:
```
git clone git@github.com:Thijsvanede/elliptic-curves.git
```

Once downloaded, you can install the module using pip:
```
pip3 install -e <path/to/directory/containing/setup.py>
```

## Usage
To create a curve use the following code snippet
```python
# Import
from ec.curves import Curve

# Create curve y² = x³ + ax + b (mod n, optional)
curve = Curve(
    a =  497,
    b = 1768,
    n = 9739,
)

# Show curve
print(curve) # y² = x³ + 497x + 1768 mod 9739
```

We can now create points on the curve and perform arithmetic operations on those points:
```python
# Point Negation
p = curve.point(8045, 6936)
print(p)  # [Curve y² = x³ + 497x + 1768 mod 9739] Point(8045, 6936)
print(-p) # [Curve y² = x³ + 497x + 1768 mod 9739] Point(8045, 2803)

# Point Addition
p = curve.point(493, 5564)
q = curve.point(1539, 4742)
r = curve.point(4403, 5202)
print(p+p+q+r) # [Curve y² = x³ + 497x + 1768 mod 9739] Point(4215, 2162)

# Scalar Multiplication
p = curve.point(2339, 2213)
print(7863*p) # [Curve y² = x³ + 497x + 1768 mod 9739] Point(9467, 2742)
```
