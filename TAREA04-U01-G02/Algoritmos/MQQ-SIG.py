import random
import time
import json

# Función para leer el archivo de texto
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.read()

# Función para generar las claves (pública y privada)
def generar_claves_mqq():
    clave_privada = [random.randint(1, 100) for _ in range(10)]
    clave_publica = [x ** 2 + 5 * x + 17 for x in clave_privada]  # Relación más compleja
    return clave_privada, clave_publica

# Función para cifrar el texto
def cifrar_mqq(texto, clave_publica):
    suma_clave_publica = sum(clave_publica) % 256
    texto_cifrado = [(ord(c) + suma_clave_publica) % 256 for c in texto]
    return texto_cifrado

# Función para descifrar el texto
def descifrar_mqq(texto_cifrado, clave_privada):
    suma_clave_privada = sum([x ** 2 + 5 * x + 17 for x in clave_privada]) % 256
    texto_descifrado = ''.join(
        chr((c - suma_clave_privada) % 256) for c in texto_cifrado
    )
    return texto_descifrado

# Función principal
def main():
    archivo = 'C://Users//dell7320//Downloads//TAREA04-U01-G02//cambios//TAREA04-U01-G02//txt//100000.txt'
    texto = leer_archivo(archivo)

    print("Texto a Cifrar:")
    print(texto[:100] + '...')  # Muestra los primeros 100 caracteres

    clave_privada, clave_publica = generar_claves_mqq()

    # Cifrado
    start_time = time.perf_counter()
    texto_cifrado = cifrar_mqq(texto, clave_publica)
    tiempo_cifrado = time.perf_counter() - start_time

    # Guardar texto cifrado
    with open("texto_cifrado.json", "w", encoding="utf-8") as archivo_cifrado:
        json.dump(texto_cifrado, archivo_cifrado)

    # Descifrado
    start_time = time.perf_counter()
    texto_descifrado = descifrar_mqq(texto_cifrado, clave_privada)
    tiempo_descifrado = time.perf_counter() - start_time

    # Resultados
    print("\nTexto Descifrado:")
    print(texto_descifrado[:100] + '...')  # Muestra los primeros 100 caracteres
    print("\nClave Privada:", clave_privada)
    print("Clave Pública:", clave_publica)
    print(f"Tiempo para cifrar: {tiempo_cifrado:.9f} segundos")
    print(f"Tiempo para descifrar: {tiempo_descifrado:.9f} segundos")
    print(f"Número de caracteres cifrados: {len(texto_cifrado)}")

    if texto == texto_descifrado:
        print("\nEl texto descifrado coincide con el original.")
    else:
        print("\nError: El texto descifrado no coincide con el original.")

if __name__ == '__main__':
    main()
