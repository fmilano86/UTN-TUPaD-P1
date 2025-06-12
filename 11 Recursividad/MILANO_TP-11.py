#Ejercicio 1) Crea una función recursiva que calcule el factorial de un número. 
#Luego, utiliza esa función para calcular y mostrar en pantalla el factorial 
#de todos los números enteros entre 1 y el número que indique el usuario

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

num= int(input("Ingrese un número entero positivo: "))
for i in range(1, num + 1):
    print(f"El factorial de {i} es {factorial(i)}")

# Ejercicio 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci 
# en la posición indicada. Posteriormente, muestra la serie completa hasta la posición 
# que el usuario especifique.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num_fib = int(input("Ingrese la posición en la serie de Fibonacci: "))
print("Serie de Fibonacci hasta la posición", num_fib, ":")
for i in range(num_fib + 1):
    print(fibonacci(i))

#Ejercicio 3) Crea una función recursiva que calcule la potencia de un número base 
#elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). 
#Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base} elevado a {exponente} es {potencia(base, exponente)}")

#Ejercicio 4) Crear una función recursiva en Python que reciba un número entero positivo 
#en base decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero_decimal = int(input("Ingrese un número entero positivo en base decimal: "))
if numero_decimal == 0:
    print("La representación en binario es: 0")
else:
    binario = decimal_a_binario(numero_decimal)
    print(f"La representación en binario de {numero_decimal} es: {binario}")

#Ejercicio 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto 
#sin espacios ni tildes y devuelva True si es un palíndromo o False si no lo es.

def es_palindromo(palabra):
    palabra = palabra.lower()  
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False    
    return es_palindromo(palabra[1:-1])  

palabra = input("Ingrese una palabra o frase sin espacios ni tildes: ")

#Ejercicio 6) Escribí una función recursiva en Python llamada suma_digitos(n) 
#que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
#No se puede convertir el número a string.
#Usá operaciones matemáticas (%, //) y recursión.

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

numero = int(input("Ingrese un número entero positivo: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")

#Ejercicio 7) Un niño está construyendo una pirámide con bloques. 
#En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), 
#y así sucesivamente hasta llegar al último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques 
#en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(n):
    if n <= 0:
        return 0
    else:
        return n + contar_bloques(n - 1)

numero_bloques = int(input("Ingrese el número de bloques en el nivel más bajo: "))
total_bloques = contar_bloques(numero_bloques)
print(f"El total de bloques necesarios para construir la pirámide es: {total_bloques}")

#8) Escribí una función recursiva llamada contar_digito(numero, digito) 
#que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), 
#y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 1 if digito == 0 else 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
    
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito (0-9): "))

if 0 <= digito <= 9:
    cantidad = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")
else:
    print("El dígito debe estar entre 0 y 9.")

