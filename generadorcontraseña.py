import random
import string

def generar_contraseña(longitud, solo_numeros=False):
    # Caracteres permitidos en la contraseña
    caracteres = string.digits if solo_numeros else string.ascii_letters + string.digits + string.punctuation

    # Generar contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contraseña

def guardar_en_archivo(contraseñas, nombre_archivo):
    with open(nombre_archivo, "w") as archivo:
        for contraseña in contraseñas:
            archivo.write(contraseña + "\n")

def generar_contraseñas_cantidad(cantidad, longitud, solo_numeros=False):
    contraseñas = [generar_contraseña(longitud, solo_numeros) for _ in range(cantidad)]
    return contraseñas

def main():
    print("Generador de Contraseñas")
    
    # Obtener la longitud deseada de las contraseñas
    longitud_contraseña = int(input("Ingrese la longitud deseada de las contraseñas: "))
    
    # Preguntar si las contraseñas deben ser solo números
    solo_numeros = input("¿Desea que las contraseñas sean solo números? (Sí/No): ").lower() == 'si'

    print("Ingrese posibles palabras clave (separadas por espacios):")

    # Obtener palabras clave del usuario
    palabras_clave = input().split()

    # Agregar las palabras clave a la lista de caracteres permitidos
    caracteres = string.digits if solo_numeros else string.ascii_letters + string.digits + string.punctuation
    caracteres += ''.join(palabras_clave)

    # Solicitar al usuario la cantidad de contraseñas a generar
    cantidad_contraseñas = int(input("Ingrese la cantidad de contraseñas a generar: "))
    
    # Generar y mostrar las contraseñas
    contraseñas = generar_contraseñas_cantidad(cantidad_contraseñas, longitud_contraseña, solo_numeros)

    # Solicitar al usuario el nombre del archivo
    nombre_archivo = input("Ingrese el nombre del archivo para guardar las contraseñas: ")

    # Guardar las contraseñas en el archivo especificado
    guardar_en_archivo(contraseñas, nombre_archivo)
    print(f"{cantidad_contraseñas} contraseñas de longitud {longitud_contraseña} guardadas en el archivo '{nombre_archivo}'.")

if __name__ == "__main__":
    main()
