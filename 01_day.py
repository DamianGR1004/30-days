# Reto #1
#Variables y Tipos de Datos
# Enunciado: Crea un programa que calcule el IMC (Índice de Masa Corporal) del usuario.

# Fórmula del IMC: peso (kg) / altura (m)²
# - Pide al usuario su peso (en kg) y su altura (en metros).

#Interacción con el usuario
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

# Cálculo del IMC
imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Estás por debajo del peso normal.")
elif 18.5 <= imc < 24.9:
    print("Tienes un peso normal.")
else:
    print("Es probable que tengas sobrepeso, si tienes posibilidad, consulta a un profesional de la salud.")
# Fin del programa
# Fin del reto

