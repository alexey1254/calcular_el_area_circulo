# Para calcular el radio de un círculo importamos pi, desde el modulo math y ponemos la fórmula pi*r^2 (el {} debe estar
# entre comillas, si no, parece que no funciona xd)

r=float(input("pon el radio del circulo aquí: "))
from math import pi
area= (pi * r**2)
print(("El área del círculo es {}") .format(area))
