nombre= input("¿Cual es tu Nombre?")
edad= input("¿Cual es tu Edad?")
a= float(input("¿Cual es tu nota en Apreciacion?"))
d= float(input("¿Cual es tu nota en Diarias?"))
p= float(input("¿Cual fue tu nota en Parcial?"))
promedio=(a+d+p)/3
print("Tu Promedio es:",promedio)

if promedio >= 71:
    print("Aprobado")
else:
    print("Reprobado")
