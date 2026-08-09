def rect (length, width):
    area = length * width
    per = (length + width)* 2
    print (f"The area of the rectange is {area} and the perimeter is {per}")

def circle(radius):
    import math
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference