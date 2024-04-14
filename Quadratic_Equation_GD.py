import math
 
a = float(input())
b = float(input())
c = float(input())
 
discriminant = b**2 - 4*a*c
 
x1 = (-b - math.sqrt(discriminant)) / (2*a)
x2 = (-b + math.sqrt(discriminant)) / (2*a)
 
formatted_x1 = f"{x1.real:.1f}" if x1.real != 0 else "0.0"
formatted_x2 = f"{x2.real:.1f}" if x2.real != 0 else "0.0"
 
print(f"x1={formatted_x1}")
print(f"x2={formatted_x2}")