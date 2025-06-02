# Trabajo Práctico - Funciones en Python
# Tecnicatura Universitaria en Programación

# 1. imprimir_hola_mundo
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

# 2. saludar_usuario(nombre)
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("\nIngresá tu nombre: ")
print(saludar_usuario(nombre))

# 3. informacion_personal(nombre, apellido, edad, residencia)
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("\nNombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

# 4. calcular_area_circulo y calcular_perimetro_circulo
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("\nIngresá el radio del círculo: "))
print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

# 5. segundos_a_horas(segundos)
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("\nIngresá la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"Equivale a {horas:.2f} horas.")

# 6. tabla_multiplicar(numero)
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("\nIngresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

# 7. operaciones_basicas(a, b)
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    producto = a * b
    division = a / b if b != 0 else "Infinito (división por cero)"
    return (suma, resta, producto, division)

a = float(input("\nIngresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
suma, resta, producto, division = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Producto: {producto}, División: {division}")

# 8. calcular_imc(peso, altura)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("\nIngresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")

# 9. celsius_a_fahrenheit(celsius)
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("\nIngresá la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")

# 10. calcular_promedio(a, b, c)
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("\nPrimer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio es: {promedio:.2f}")
