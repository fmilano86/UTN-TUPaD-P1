# Trabajo Práctico 6: Estructuras de Datos Complejas

# 1) Diccionario de precios
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Lista de frutas
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

# 4) Agenda telefónica
agenda = {}
for i in range(5):
    nombre = input(f"Nombre del contacto {i+1}: ")
    telefono = input(f"Número de {nombre}: ")
    agenda[nombre] = telefono
consulta = input("¿A quién desea consultar?: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Contacto no encontrado.")

# 5) Palabras únicas y recuento
frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
print("Palabras únicas:", palabras_unicas)
print("Recuento de palabras:", recuento)

# 6) Notas de alumnos
alumnos = {}
for i in range(3):
    nombre = input(f"Nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")

# 7) Aprobados
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}
ambos = parcial1 & parcial2
solo_uno = (parcial1 ^ parcial2)
total = parcial1 | parcial2
print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", total)

# 8) Stock de productos
stock = {'Leche': 10, 'Pan': 5, 'Huevos': 30}
producto = input("Ingrese el nombre del producto: ")
if producto in stock:
    print(f"Stock de {producto}: {stock[producto]}")
    agregar = int(input("Ingrese cantidad a agregar: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input(f"{producto} no existe. Ingrese stock inicial: "))
    stock[producto] = nuevo_stock
print("Stock actualizado:", stock)

# 9) Agenda con tuplas
agenda_eventos = {('Lunes', '10:00'): 'Reunión', ('Martes', '14:00'): 'Clases'}
dia = input("Día a consultar: ")
hora = input("Hora a consultar: ")
clave = (dia, hora)
if clave in agenda_eventos:
    print(f"Actividad: {agenda_eventos[clave]}")
else:
    print("No hay actividad programada.")

# 10) Invertir diccionario
paises = {'Argentina': 'Buenos Aires', 'Brasil': 'Brasilia', 'Chile': 'Santiago'}
capitales = {capital: pais for pais, capital in paises.items()}
print("Capitales como claves:", capitales)