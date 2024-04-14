a = float(input())
b = float(input())
c = float(input())

D = (b**2)-(4*a*c)

sqrt_D = D**0.5

x1 = (-b-sqrt_D)/2*a
x2 = (-b+sqrt_D)/2*a

print("x1="+format(x1,".1f"))
print("x2="+format(x2,".1f"))