
print("** Calificaciones **")

calificacion = float(input("Ingresa calificación: "))

if calificacion==100:
    print("¡Excelente!")
elif calificacion>=90 and calificacion<=100:
    print("¡Muy bien!")
elif calificacion>=80 and calificacion<=90:
    print("¡Bien!")
elif calificacion>=70 and calificacion<=80:
    print("¡Regular!")
elif calificacion>=60 and calificacion<=70:
    print("¡Suficiente!")
elif calificacion>=0 and calificacion<=60:
    print("¡Mala!")
else:
    print("Error:Calificación erronea")