# creando una lista (se pueden modificar)
lista = ["Jhonas Muñoz", "KlandeMC", True, 1.75]

# creando una lista (no se pueden modificar)
tupla = ("Jhonas Muñoz", "KlandeMC", True, 1.75)

# esto es valido
lista[3] = "Maquinola"

# esto no es valido
#tupla[3] = "Maquinola"

# creando un conjunto (set) (no accede a elementos por su indice, no almacena datos duplicados)
conjunto = {"Jhonas Muñoz", "KlandeMC", True, "KlandeMC"}

# print(conjunto[3]) -> no puede acceder al ultimo elemento porque se repite

# creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
  'nombre': "Jhonas Muñoz",
  'canal': "KlandeMC",
  'esta_emocionado': True,
  'altura': 1.85,
  'dato_duplicado': "Klande MC"
}

print(diccionario["altura"])
print(lista[3])