#Area of a rectangle
#https://www.codewars.com/kata/580a0347430590220e000091

import math

def rectangle_area(diagonal, side):
    if diagonal <= side:
        return "This is not a rectangle."
    
    other_side = math.sqrt(diagonal**2 - side**2)
    
    area = side * other_side
    
    return round(area, 2)

print(rectangle_area(11, 5))  
print(rectangle_area(90, 101)) 
print(rectangle_area(43, 27)) 
print(rectangle_area(16, 16)) 
print(rectangle_area(61, 31))   

#This function sets the formula to calculate a side of a triangle.
#It also determines whether the result will not be a rectangle.
#Once started, the function will reveal the area of the rectangles based on the diagonal and given side.
#It also rounds each result to two decimal points.