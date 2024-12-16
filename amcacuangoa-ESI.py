def cifrar_mensaje(mensaje):
    try:
        # Para reemplazar los espacios con "-"
        mensaje = mensaje.replace(" ", "-")
        # Número de filas
        filas = 5
        
        # Calcular el número de columnas necesarias
        columnas = (len(mensaje) + filas - 1) // filas
        
        # Rellenar el mensaje con "*" 
        mensaje_relleno = mensaje.ljust(filas * columnas, "*")
        
        # Crea la matriz de cifrado (5 filas)
        matriz = [list(mensaje_relleno[i:i+columnas]) for i in range(0, len(mensaje_relleno), columnas)]
        
        # Muestra el mensaje original
        print(f"Mensaje original: {mensaje}")
        
        # Muestra la matriz de cifrado
        print("\nMatriz de cifrado:")
        for fila in matriz:
            print("".join(fila))
        

        matriz_permutada = matriz         
        # Generar el mensaje cifrado
        mensaje_cifrado = "".join("".join(fila) for fila in matriz_permutada)
        
        # Mostrar el mensaje cifrado
        print(f"\nMensaje cifrado: {mensaje_cifrado}")
        
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Introducir el mensaje a cifrar
mensaje = input("Introduce el mensaje a cifrar: ")

# Llama a la función de cifrado
cifrar_mensaje(mensaje)
