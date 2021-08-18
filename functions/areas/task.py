import math

def square(a):
    """Finds the area of a square"""
    return a*a

def rectangle(a,b):
    """Finds the area of a rectangle"""
    return a*b

def triangle(a,b):
    """Finds the area of a triangle"""
    return (a*b)/2

def circle(a):
    """Finds the area of a circle"""
    return math.pi*a*a

print(square(2))
print(rectangle(3,6))
print(triangle(3,4))
print(circle(2))
