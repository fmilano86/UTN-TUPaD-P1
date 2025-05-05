#Ejercicio 1

for i in range(101):
    print(i)

#Ejercicio 2

num = int(input("Ingrese un numero para verificar cuantos digitos contiene"))
n = abs(num)
contador = 0

if num == 0:
    print(f"El numero ingresado: {num} tiene 1 digito")
else:
    while n != 0 :
        contador += 1
        n = n // 10


print(f"El numero ingresado: {num} tiene {contador} digitos")

#Ejercicio 3

print("El sistema le pedira dos numeros y calculara la suma de todos los numeros enteros que estan entre ellos, sin incluirlos")

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
resultado = 0

if num1 < num2:
    for i in range((num1 + 1),num2):
        resultado += i
elif num1 > num2:
    for i in range((num2 + 1),num1):
        resultado += i

print("El resultado de la suma de los numeros enteros que estan entre los ingresados es",resultado)

#Ejercicio 4

SALIDA = 0
resultado = 0

print("El sistema ira sumando los numeros que usted ingrese hasta que ingrese el numero", SALIDA)

num = int(input("Ingrese un numero: "))

while num != 0:
    resultado += num
    num = int(input("Ingrese otro numero: "))

print ("El resultado de la suma de los numeros ingresados es:", resultado)

#Ejercicio 5

from random import randint

num = randint(0,9)

adiv = int(input("Adivine el numero entre el 0 y el 9 elegido al azar por la maquina: "))

while adiv != num:
    adiv = int(input("Incorrecto. Ingrese otro numero: "))

print("Correcto! El numero es:",num)

#Ejercicio 6

for i in range(100,-1,-2):
    print(i)

#Ejercicio 7

resultado = 0
num = int(input("Ingrese un numero entero positivo, el sistema sumara los numeros que hay entre el y el 0: "))

while num <= 0:
    num = int(input("El numero ingresado es incorrecto. Ingrese un numero entero positivo"))

for i in range(num):
    resultado += i

print("La suma de los numeros entre el ingresado y 0 es:",resultado)

#Ejercicio 8

CANT_NUM = 100
cont_par = 0
cont_impar = 0

print("El programa le pedira una serie de numeros. Luego evaluara cuantos numeros pares y cuantos impares ha ingresado")

for i in range(CANT_NUM):
    num = int(input("Ingrese un numero: "))
    
    if num == 0:
        continue
    elif num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

print(f"Usted ingreso {cont_par} numeros pares y {cont_impar} numeros impares")

#Ejercicio 9

CANT_NUM = 100
acum = 0

print("El sistema le pedira una serie de numeros enteros y calculara su promedio")

for i in range(CANT_NUM):
    num = int(input("Ingrese un numero: "))
    acum += num

promedio = acum / CANT_NUM
print("El promedio de los numeros ingresados es:", promedio)

#Ejercicio 10

invertido = 0
numero = int(input("Ingrese un numero entero y el sistema invertira sus digitos: "))

if numero < 0:
    signo = -1
elif numero > 0:
    signo = 1

num = abs(numero)

if num == 0:
    invertido = 0
else: 
    while num > 0:
        digito = num % 10
        invertido = (invertido * 10) + digito
        num = num // 10

resultado = invertido * signo

print("El numero ingresado fue:",numero,".Si lo invertimos, nos queda", resultado)



