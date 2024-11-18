import hashlib
import random

# Función para generar claves públicas y privadas
def generar_claves():
    clave_privada = [random.randint(1, 100) for _ in range(10)]
    clave_publica = [x * 3 + 7 for x in clave_privada]  # Relación derivada (simulación)
    return clave_privada, clave_publica

# Función para firmar un mensaje
def firmar_mensaje(mensaje, clave_privada):
    # Crear un hash del mensaje
    hash_mensaje = hashlib.sha256(mensaje.encode()).hexdigest()
    
    # Firmar el hash usando la clave privada
    firma = [ord(c) + sum(clave_privada) % 256 for c in hash_mensaje]
    return firma

# Función para verificar la firma
def verificar_firma(mensaje, firma, clave_publica):
    # Crear un hash del mensaje
    hash_mensaje = hashlib.sha256(mensaje.encode()).hexdigest()
    
    # Verificar si la firma corresponde al hash y la clave pública
    firma_calculada = [ord(c) + sum([x * 3 + 7 for x in clave_publica]) % 256 for c in hash_mensaje]
    return firma == firma_calculada

# Ejemplo principal
def main():
    # Generar claves
    clave_privada, clave_publica = generar_claves()
    
    # Mensaje a firmar
    mensaje = "Este es un mensaje de prueba para la firma digital."
    print("Mensaje original:", mensaje)
    
    # Firmar el mensaje
    firma = firmar_mensaje(mensaje, clave_privada)
    print("\nFirma generada:", firma)
    
    # Verificar la firma
    es_valida = verificar_firma(mensaje, firma, clave_publica)
    print("\n¿La firma es válida?", "Sí" if es_valida else "No")

if __name__ == "__main__":
    main()
