# Reto día 2
# Escribe un rpograma que clasdifique las calificaciones en una escala (0 a 100) como A,B,C,D o F
# Clasificando notas

calificacion = float(input("Ingrese la calificación (0 a 100): "))

# Creando las condiciones

if calificacion <= 25:
    print("F")
elif 25 < calificacion <= 50:
    print("D")
elif 50 < calificacion <= 75:
    print("C")
elif 75 < calificacion <= 90:
    print("B")
else:
    print("A")
    

#Fin del desafio