a = float(input("Ingresar a: "))
b = float(input("Ingresar b: "))
c = float(input("Ingresar c: "))

x1= (-b + (b*b - 4*a*c)**0.5)/(2*a)
x2= (-b - (b*b - 4*a*c)**0.5)/(2*a)
print(x1, '  ', x2)