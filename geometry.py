"""A package that adds various math operations that are not included in the included math library"""
import math


def pythag(a: float, b: float):
    """Performs the Pythagorean Theorem \n
     Defined as: c² = a² + b²

    Keyword arguments:
        a: the length of side A
        b: the length of side B

    Returns:
        The length of the squared hypotenuse ( c² )
    """
    return a**2 + b**2


def dist(x1: float, y1: float, x2: float, y2: float):
    """Calculates the distance between two 2D vector positions using the Pythagorean Theorem

    Keyword arguments:
        x1: the x position of the first point
        y1: the y position of the first point
        x2: the x position of the second point
        y2: the y position of the second point

    Returns:
        the distance between point1 and point2

    See:
        pythag()
    """
    width = x2 - x1
    height = y2 - y1

    c_squared = pythag(width, height)

    c = math.sqrt(c_squared)

    return c
