#Calculadora de notas
nombre = input("Nombre del estudiante:")

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"\nEstudiantes: {nombre}")

print(f"Promedio: {promedio:.1f}")

if promedio >= 3.0:
    print("Estado: Aprobado")
else: 
    print("Estado: Reprobado")
