#Ejercicio 1

#edad=int(input("Ingrese su edad: "))

#if edad >= 18:
    #print("Es mayor de edad")

#Ejercicio 2

#nota=int(input("Ingrese su nota: "))

#if nota>=6:
    #print("Aprobado")
#else:
    #print("Desaprobado")

#Ejercicio 3

#numero=int(input("Ingrese un numero par: "))

#if numero%2==0:
    #print("Ha ingresado un numero par")
#else:
    #print("Por favor, ingrese un numero par")

#Ejercicio 4

#edad=int(input("Ingrese su edad: "))

#if edad<12:
    #print("Niño/a")
#elif edad>=12 and edad<18:
    #print("Adolescente")
#elif edad>=18 and edad<30:
    #print("Adolto/a joven")
#elif edad>=30:
    #print("Adulto/a")

#Ejercicio 5

#contrasenia=input("Ingrese una contraseña que tenga entre 8 y 14 caracteres: ")

#if len(contrasenia)>=8 and len(contrasenia)<=14:
    #print("Ha ingresado una contraseña correcta")
#else:
    #print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6

#from statistics import mode, median, mean 

#import random 

#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#media=mean(numeros_aleatorios)
#mediana=median(numeros_aleatorios)
#moda=mode(numeros_aleatorios)
#print(f"La media es: {media}")
#print(f"La mediana es: {mediana}")
#print(f"La moda es: {moda}")

#if media>mediana>moda:
    #print("Sesgo positivo a la derecha")
#elif moda>mediana>media:
    #print:("Sesgo positivo a la izquierda")
#elif moda==mediana==media:
    #print("Sin sesgo")

#Ejercicio 7

# 1. Pido la frase al usuario
#frase = input("Ingresá una palabra o frase: ")

# 2. Defino el conjunto de vocales
#vocales = "aeiouAEIOU"

# 3. Compruebo que la frase no esté vacía
#if len(frase) > 0:
    # Selecciono el último carácter con índice -1
    #ultimo = frase[-1]

    # 4. Si es vocal, añado '!' al final
    #if ultimo in vocales:
        #frase = frase + "!"

# 5. Imprimo el resultado
#print(frase)

#Ejercicio 8

# 1. Pedimos datos al usuario
#nombre = input("Ingresá tu nombre: ")
#opcion = input("Elegí opción \n1=TODO MAYUSCULA \n2=todo minuscula \n3=Primeras mayyusculas \n")

# 2. Transformamos según la opción
#if opcion == "1":
    #resultado = nombre.upper()
#elif opcion == "2":
    #resultado = nombre.lower()
#elif opcion == "3":
    #resultado = nombre.title()
#else:
    #resultado = nombre
    #print("Opción no válida; mostrando sin cambios.")

# 3. Mostramos el nombre transformado
#print("Resultado:", resultado)

#Ejercicio 9

#magnitud=float(input("Ingrese la magnitud del terremoto: "))

#if magnitud<3:
   #print("Muy leve (imperceptible)")
#elif magnitud>=3 and magnitud<4:
    #print("Leve (ligeramente perceptible)")
#elif magnitud>=4 and magnitud<5:
 #   print("Moderado (sentido por personas, pero generalmente no causa daños)")
#elif magnitud>=5 and magnitud<6:
 #   print("Fuerte (puede causar daños en estructuras débiles)")
#elif magnitud>=6 and magnitud<7:
#    print("Muy Fuerte (puede causar daños significativos)")
#elif magnitud>=7:
#    print("Extremo (puede causar graves daños a gran escala)")

#Ejercicio 10

hemiN=("Nn")
hemiS=("sS")
hemisferio=input("Ingrese el hemisferio N/S: " )
mes=int(input("Ingrese el mes en formato numero: "))
dia=int(input("Ingrese el dia: "))

if hemisferio in hemiS:
    if mes==1 or mes==2 or (mes==12 and dia>=21) or (mes==3 and dia<=20):
        print("Es verano")
    elif mes==4 or mes==5 or (mes==3 and dia>=21) or (mes==6 and dia<=20):
        print("Es otonio")
    elif mes==7 or mes==8 or (mes==6 and dia>=21) or (mes==9 and dia<=20):
        print("Es invierno")
    elif mes==10 or mes==11 or (mes==9 and dia>=21) or (mes==12 and dia<=20):
        print("Es primavera")

elif hemisferio in hemiN:
    if mes==1 or mes==2 or (mes==12 and dia>=21) or (mes==3 and dia<=20):
        print("Es verano")
    elif mes==4 or mes==5 or (mes==3 and dia>=21) or (mes==6 and dia<=20):
        print("Es otonio")
    elif mes==7 or mes==8 or (mes==6 and dia>=21) or (mes==9 and dia<=20):
        print("Es invierno")
    elif mes==10 or mes==11 or (mes==9 and dia>=21) or (mes==12 and dia<=20):
        print("Es primavera")