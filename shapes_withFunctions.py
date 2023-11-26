def rectangleArea (length, width):
    rectangleArea = length * width
    print(f"The rectangle area with length {length} and width {width} is: {rectangleArea}")

rectangleArea(3, 5)    


import math
def circle_area(circle_radius):
    circle_area = round(math.pi * pow(circle_radius, 2),2)
    print(f"The area of a circle with radius {circle_radius} is {circle_area}")

circle_area(8)

def tringleArea(triangleBase, triangleHeight):
    triangleArea = triangleBase * triangleHeight
    print(f"The triangle area with base {triangleBase} and height {triangleHeight} is: {triangleArea}")

tringleArea(6, 4)