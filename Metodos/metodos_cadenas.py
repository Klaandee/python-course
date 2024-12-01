# Estructura: variable.metodo() <- función

cadena1 = "Hola,Maquinola,Soy,Jhonas"
cadena2 = "Bienvenido maquinola"

# convierte a mayuscula
mayusc = cadena1.upper()

# convierte a minuscula
minusc = cadena1.lower()

# primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

# buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("hola")

# buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepción
busqueda_index = cadena1.index("H")

# si es numerico devolvemos true, si no dolvemos false
es_numerico = cadena1.isnumeric()

# si es alfanumerico devolvemos true, si no devolvemos false
es_alfanumerico = cadena1.isalpha()

# contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("x")

# contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1) # ES UNA FUNCIÓN

# verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("h")

# verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("s")

# reemplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace("Jhonas","Lucas")

# separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(cadena_separada[3])